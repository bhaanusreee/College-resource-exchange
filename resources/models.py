from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('Book', 'Book'),
    ('Notes', 'Notes'),
    ('Stationery', 'Stationery'),
    ('Lab Kit', 'Lab Kit'),
    ('Calculator', 'Calculator'),
    ('Electronics', 'Electronics'),
    # Add more as needed
]

CONDITION_CHOICES = [
    ('New', 'New'),
    ('Good', 'Good'),
    ('Used', 'Used'),
    ('Broken', 'Broken'),
]

ACTION_CHOICES = [
    ('Donate', 'Donate'),
    ('Exchange', 'Exchange'),
    ('Request', 'Request'),
    ('Sell', 'Sell'),
]

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    year = models.CharField(max_length=20, blank=True)
    branch = models.CharField(max_length=50, blank=True)
    college = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.username

class Resource(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    condition = models.CharField(max_length=10, choices=CONDITION_CHOICES)
    image = models.ImageField(upload_to='resources/', blank=True, null=True)
    action_type = models.CharField(max_length=10, choices=ACTION_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True, help_text="Price in currency (required if selling)")
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class ResourceRequest(models.Model):
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    requester = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(blank=True)
    status = models.CharField(max_length=20, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Declined', 'Declined')], default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

class RequestBoardPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
