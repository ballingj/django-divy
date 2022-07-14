
# Setting up sqlite3
## Overview
1. Initiate the sqllite db the first time with migrate: this will create an empty db
2. Create a superuser
3. Create the Model
4. Prep the migrations
5. Execute the migrations
6. Register the model in admin.py
7. Verify App is registered in settings.py


## Expanded Procedures - Commands

### Initiate the sqlite3 db with migrate - this will create an empty db
```sh
python manage.py migrate
```

### Create a superuser
```sh
python manage.py createsuperuser
```

### Create Models
Example
```sh
from django.db import models
import uuid

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    """
    After creating the table the Admin Panel shows objects instead of something meaningful.  
    This method will adds the title of the object
    """
    def __str__(self):
        return self.title
```

### Prep the migration - this will create the migrations folder
```sh
python manage.py makemigrations
```

### Execute migrations - this will create the database table
```sh
python manage.py migrate
```

### Register the model in admin.py - needed to see in Admin Page
```sh
from django.contrib import admin

# Register your models here.
from .models import Project


admin.site.register(Project)

```

### Verify App is registered in settings.py
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projects',     # add the new app
]
```