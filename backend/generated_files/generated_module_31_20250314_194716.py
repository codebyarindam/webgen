Based on the provided data, I'll create a Django model and views to manage groups and their contacts. Here's an example code:

**models.py**
```python
from django.db import models
from django.utils import timezone

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
```

**views.py**
```python
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView
from .models import Group, Contact
from .forms import GroupForm, ContactForm

class GroupListView(ListView):
    model = Group
    template_name = 'groups/index.html'

class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/create.html'
    success_url = '/groups/'

class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'groups/update.html'
    success_url = '/groups/'

def view_group(request, pk):
    group = Group.objects.get(pk=pk)
    contacts = group.contacts.all()
    return render(request, 'groups/view.html', {'group': group, 'contacts': contacts})

def create_contact(request, pk):
    group = Group.objects.get(pk=pk)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.group = group
            contact.save()
            return redirect('view_group', pk=pk)
    else:
        form = ContactForm()
    return render(request, 'groups/create_contact.html', {'form': form, 'group': group})

def update_contact(request, pk, contact_pk):
    group = Group.objects.get(pk=pk)
    contact = Contact.objects.get(pk=contact_pk)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('view_group', pk=pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'groups/update_contact.html', {'form': form, 'group': group, 'contact': contact})
```

**forms.py**
```python
from django import forms
from .models import Group, Contact

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name', 'description')

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('name', 'email', 'phone')
```

**urls.py**
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.GroupListView.as_view(), name='index'),
    path('create/', views.GroupCreateView.as_view(), name='create_group'),
    path('<pk>/update/', views.GroupUpdateView.as_view(), name='update_group'),
    path('<pk>/view/', views.view_group, name='view_group'),
    path('<pk>/create_contact/', views.create_contact, name='create_contact'),
    path('<pk>/update_contact/<contact_pk>/', views.update_contact, name='update_contact'),
]
```

**templates/groups/index.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Groups</h1>
  <ul>
    {% for group in group_list %}
      <li>
        {{ group.name }}
        <a href="{% url 'view_group' group.pk %}">View</a>
        <a href="{% url 'update_group' group.pk %}">Edit</a>
      </li>
    {% endfor %}
  </ul>
  <a href="{% url 'create_group' %}">Create new group</a>
{% endblock %}
```

**templates/groups/create.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Create Group</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Create</button>
  </form>
{% endblock %}
```

**templates/groups/view.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ group.name }}</h1>
  <p>{{ group.description }}</p>
  <h2>Contacts</h2>
  <ul>
    {% for contact in contacts %}
      <li>
        {{ contact.name }}
        <a href="{% url 'update_contact' group.pk contact.pk %}">Edit</a>
      </li>
    {% endfor %}
  </ul>
  <a href="{% url 'create_contact' group.pk %}">Create new contact</a>
{% endblock %}
```

This code provides basic CRUD (Create, Read, Update, Delete) functionality for groups and contacts. It uses Django's built-in generic views and forms to simplify the process. Note that you'll need to create the templates and URLs to match the views and models.

To use this code, make sure to:

1. Create a new Django project and app.
2. Copy the code into the respective files (models.py, views.py, forms.py, urls.py, templates/).
3. Run `python manage.py makemigrations` and `python manage.py migrate` to create the database tables.
4. Create a superuser and log in to the admin interface to create groups and contacts.

This is just a starting point, and you'll likely need to customize the code to fit your specific requirements.