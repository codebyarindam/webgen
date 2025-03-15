Based on the provided data, I will create a Django model and view to display a list of existing groups and provide options to create a new group or select an existing group to view/edit contacts.

### models.py
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
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
```

### views.py
```python
from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, DetailView, UpdateView
from .models import Group, Contact
from .forms import GroupForm, ContactForm

class GroupListView(ListView):
    model = Group
    template_name = 'group_list.html'

class GroupCreateView(CreateView):
    model = Group
    form_class = GroupForm
    template_name = 'group_form.html'
    success_url = '/groups/'

class GroupDetailView(DetailView):
    model = Group
    template_name = 'group_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contacts'] = Contact.objects.filter(group=self.object)
        return context

class GroupUpdateView(UpdateView):
    model = Group
    form_class = GroupForm
    template_name = 'group_form.html'
    success_url = '/groups/'

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_form.html'

    def form_valid(self, form):
        form.instance.group_id = self.kwargs['pk']
        return super().form_valid(form)

    def get_success_url(self):
        return f'/groups/{self.kwargs["pk"]}/'

class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact_form.html'

    def get_success_url(self):
        return f'/groups/{self.object.group.id}/'
```

### forms.py
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

### urls.py
```python
from django.urls import path
from . import views

urlpatterns = [
    path('groups/', views.GroupListView.as_view(), name='group_list'),
    path('groups/create/', views.GroupCreateView.as_view(), name='group_create'),
    path('groups/<pk>/', views.GroupDetailView.as_view(), name='group_detail'),
    path('groups/<pk>/update/', views.GroupUpdateView.as_view(), name='group_update'),
    path('groups/<pk>/contacts/create/', views.ContactCreateView.as_view(), name='contact_create'),
    path('contacts/<pk>/update/', views.ContactUpdateView.as_view(), name='contact_update'),
]
```

### templates/group_list.html
```html
<h1>Group List</h1>
<ul>
    {% for group in group_list %}
        <li>
            {{ group.name }}
            <a href="{% url 'group_detail' group.pk %}">View</a>
            <a href="{% url 'group_update' group.pk %}">Edit</a>
        </li>
    {% endfor %}
</ul>
<a href="{% url 'group_create' %}">Create New Group</a>
```

### templates/group_detail.html
```html
<h1>Group Detail</h1>
<h2>{{ group.name }}</h2>
<p>{{ group.description }}</p>
<h3>Contacts:</h3>
<ul>
    {% for contact in contacts %}
        <li>
            {{ contact.name }}
            <a href="{% url 'contact_update' contact.pk %}">Edit</a>
        </li>
    {% endfor %}
</ul>
<a href="{% url 'contact_create' group.pk %}">Create New Contact</a>
```

### templates/group_form.html
```html
<h1>Create/Edit Group</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```

### templates/contact_form.html
```html
<h1>Create/Edit Contact</h1>
<form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Submit</button>
</form>
```
This code provides the basic functionality for creating, reading, updating, and deleting groups and contacts. You may need to modify the templates and views to fit your specific requirements. Additionally, you will need to create a database and run migrations to create the tables for the models.