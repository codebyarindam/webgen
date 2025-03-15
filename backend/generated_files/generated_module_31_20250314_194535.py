Based on the provided data, I will create a Django model and views to manage groups and their contacts. Here's an example of how you could structure your code:

**models.py**
```python
from django.db import models
from django.utils import timezone

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Contact(models.Model):
    id = models.AutoField(primary_key=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='contacts')
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

**views.py**
```python
from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Group, Contact
from .forms import GroupForm, ContactForm

class GroupListView(ListView):
    model = Group
    template_name = 'groups/index.html'

class GroupDetailView(DetailView):
    model = Group
    template_name = 'groups/detail.html'

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

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/create.html'
    success_url = '/groups/{group_id}/'

    def dispatch(self, request, *args, **kwargs):
        self.group_id = kwargs['group_id']
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.group_id = self.group_id
        return super().form_valid(form)

class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contacts/update.html'
    success_url = '/groups/{group_id}/'

    def dispatch(self, request, *args, **kwargs):
        self.group_id = kwargs['group_id']
        return super().dispatch(request, *args, **kwargs)
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
    path('groups/', views.GroupListView.as_view(), name='group_list'),
    path('groups/<int:pk>/', views.GroupDetailView.as_view(), name='group_detail'),
    path('groups/create/', views.GroupCreateView.as_view(), name='group_create'),
    path('groups/<int:pk>/update/', views.GroupUpdateView.as_view(), name='group_update'),
    path('groups/<int:group_id>/contacts/create/', views.ContactCreateView.as_view(), name='contact_create'),
    path('groups/<int:group_id>/contacts/<int:pk>/update/', views.ContactUpdateView.as_view(), name='contact_update'),
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
        (<a href="{% url 'group_detail' group.pk %}">View</a>)
        (<a href="{% url 'group_update' group.pk %}">Edit</a>)
      </li>
    {% empty %}
      <li>No groups available.</li>
    {% endfor %}
  </ul>
  <p><a href="{% url 'group_create' %}">Create a new group</a></p>
{% endblock %}
```

**templates/groups/detail.html**
```html
{% extends 'base.html' %}

{% block content %}
  <h1>{{ group.name }}</h1>
  <p>{{ group.description }}</p>
  <h2>Contacts</h2>
  <ul>
    {% for contact in group.contacts.all %}
      <li>
        {{ contact.name }}
        (<a href="{% url 'contact_update' group.pk contact.pk %}">Edit</a>)
      </li>
    {% empty %}
      <li>No contacts available.</li>
    {% endfor %}
  </ul>
  <p><a href="{% url 'contact_create' group.pk %}">Add a new contact</a></p>
{% endblock %}
```

This is a basic implementation and you can customize it according to your requirements. You'll also need to create the templates for the create and update views.