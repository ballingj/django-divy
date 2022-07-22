from django.db import models
import uuid

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)    # max_length is a required parameter for Charfield
    description = models.TextField(null=True, blank=True)   # null = allows null value in dbase; blank = means blank form is allowed in django
    demo_link = models.CharField(max_length=2000, null=True, blank=True)  
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    tags = models.ManyToManyField('Tag', blank=True) # the 'Tag' here is quoted because this class comes before the Tag class: if the Tag was defined first, remove the quotes 
    vote_total = models.IntegerField(default=0, null=True, blank=True)  # counts the number of votes this object received
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)  #calculates the ratio
    created = models.DateTimeField(auto_now_add=True)   # generate the datetime stamp automatically
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)    # override django id with uuid 

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
    project = models.ForeignKey(Project, on_delete=models.CASCADE)     # what project this review is associated : CASCADE will delete the review when associated data in project is deleted
    body = models.TextField(null=True, blank=True)
    value = models.CharField(max_length=2000, choices=VOTE_TYPE)    # gives a dropdown list of vote choices
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    
    def __str__(self):
        return self.value

'''
this table is going to store tags for a project. this is a many-to-many relationship so multiple projects can be associated
with multiple tags and vise-versa:  django provides the intermediary table to link the project table and tags table together using their
unique IDs: the key is in the projects model with the method models.ManyToManyField()
'''
class Tag(models.Model):
    name = models.CharField(max_length=200)    # max_length is a required parameter for Charfield
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name
