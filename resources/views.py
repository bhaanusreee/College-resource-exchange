from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import Resource, ResourceRequest, RequestBoardPost, UserProfile
from .forms import ResourceForm, ResourceRequestForm, RequestBoardPostForm, UserRegisterForm, UserProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponseForbidden

# Beautiful homepage
def home(request):
    # Get some featured resources for the homepage
    featured_resources = Resource.objects.all().order_by('-created_at')[:6]
    stats = {
        'total_resources': Resource.objects.count(),
        'selling_resources': Resource.objects.filter(action_type='Sell').count(),
        'donation_resources': Resource.objects.filter(action_type='Donate').count(),
        'exchange_resources': Resource.objects.filter(action_type='Exchange').count(),
    }
    return render(request, 'resources/home.html', {
        'featured_resources': featured_resources,
        'stats': stats
    })

# List all resources (separate page)
def resource_list(request):
    action_filter = request.GET.get('action_type', '')
    if action_filter:
        resources = Resource.objects.filter(action_type=action_filter).order_by('-created_at')
    else:
        resources = Resource.objects.all().order_by('-created_at')
    return render(request, 'resources/resource_list.html', {'resources': resources, 'action_filter': action_filter})

# Resource detail view
def resource_detail(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    return render(request, 'resources/resource_detail.html', {'resource': resource})

# Upload a new resource
@login_required
def resource_upload(request):
    if request.method == 'POST':
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            resource = form.save(commit=False)
            resource.owner = request.user
            resource.save()
            return redirect('resource_list')
    else:
        form = ResourceForm()
    return render(request, 'resources/resource_upload.html', {'form': form})

# Request a resource
@login_required
def resource_request(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if request.method == 'POST':
        form = ResourceRequestForm(request.POST)
        if form.is_valid():
            req = form.save(commit=False)
            req.resource = resource
            req.requester = request.user
            req.save()
            return redirect('resource_detail', pk=pk)
    else:
        form = ResourceRequestForm()
    return render(request, 'resources/resource_request.html', {'form': form, 'resource': resource})

# Request board (list and post requests)
def request_board(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = RequestBoardPostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.user = request.user
                post.save()
                return redirect('request_board')
        else:
            return redirect('login')
    else:
        form = RequestBoardPostForm()
    posts = RequestBoardPost.objects.all().order_by('-created_at')
    return render(request, 'resources/request_board.html', {'form': form, 'posts': posts})

# User registration
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        profile_form = UserProfileForm(request.POST)
        if form.is_valid() and profile_form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()
            login(request, user)
            return redirect('resource_list')
    else:
        form = UserRegisterForm()
        profile_form = UserProfileForm()
    return render(request, 'resources/register.html', {'form': form, 'profile_form': profile_form})

# User profile (view and edit)
@login_required
def profile(request):
    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = UserProfileForm(instance=user_profile)
    return render(request, 'resources/profile.html', {'form': form})

# Sell resources page
def sell_resources(request):
    selling_resources = Resource.objects.filter(action_type='Sell').order_by('-created_at')
    return render(request, 'resources/sell_resources.html', {'resources': selling_resources})

def resource_delete(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if not request.user.is_authenticated or request.user != resource.owner:
        return HttpResponseForbidden("You are not allowed to delete this resource.")
    if request.method == 'POST':
        resource.delete()
        messages.success(request, 'Resource deleted successfully.')
        return redirect('resource_list')
    return render(request, 'resources/resource_confirm_delete.html', {'resource': resource})
