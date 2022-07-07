from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)    # max_length is a required parameter for Charfield
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True) # the 'Tag' here is quoted because this class comes before the Tag class: if the Tag was defined first, remove quotes 
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    """
    After creating the table the Admin Panel shows objects instead of something meaningful.  
    This method will adds the title of the object
    """
    def __str__(self):
        return self.title

class Review(models.Model):
    VOTE_TYPE = (
        ('up', 'Up Vote'),
        ('down', 'Down Vote')
    )
    # owner =
    project = models.ForeignKey(Project, on_delete=models.CASCADE)     # what project this review is associated : CASCADE will delete the review
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=2000, choices=VOTE_TYPE)    # gives a dropdown list of vote choices
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.value


class Tag(models.Model):
    name = models.CharField(max_length=200)    # max_length is a required parameter for Charfield
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
