Here's a possible implementation of the requirement using Django, assuming a model for Contact and a view to handle the contact details page:

### models.py
```python
from django.db import models

class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    phone_numbers = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    address = models.TextField()
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.full_name
```

### views.py
```python
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from .forms import ContactForm

def contact_details(request, pk):
    """
    Display detailed information for a specific contact.

    Allow users to edit contact details.
    """
    contact = Contact.objects.get(pk=pk)

    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contact details updated successfully.')
            return redirect('contact_details', pk=pk)
    else:
        form = ContactForm(instance=contact)

    return render(request, 'contact_details.html', {'form': form, 'contact': contact})
```

### forms.py
```python
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('full_name', 'phone_numbers', 'email', 'address', 'notes')
```

### templates/contact_details.html
```html
{% extends 'base.html' %}

{% block content %}
  <h1>Contact Details</h1>
  <form method="post">
    {% csrf_token %}
    {{ form.as_p }}
    <button type="submit">Update</button>
  </form>

  <h2>Contact Information</h2>
  <p>Full Name: {{ contact.full_name }}</p>
  <p>Phone Numbers: {{ contact.phone_numbers }}</p>
  <p>Email: {{ contact.email }}</p>
  <p>Address: {{ contact.address }}</p>
  <p>Notes: {{ contact.notes }}</p>
{% endblock %}
```

### tests.py
```python
from django.test import TestCase
from selenium import webdriver
from django.urls import reverse

class ContactDetailsTest(TestCase):
    def setUp(self):
        self.contact = Contact.objects.create(
            full_name='John Doe',
            phone_numbers='1234567890',
            email='john@example.com',
            address='123 Main St',
            notes='This is a note'
        )

    def test_contact_details_page(self):
        url = reverse('contact_details', args=[self.contact.pk])
        self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.assertEqual(self.driver.title, 'Contact Details')

        # Test editing contact details
        form = self.driver.find_element_by_tag_name('form')
        full_name_input = self.driver.find_element_by_name('full_name')
        full_name_input.clear()
        full_name_input.send_keys('Jane Doe')
        form.submit()

        self.driver.refresh()
        self.assertEqual(self.driver.title, 'Contact Details')
        self.assertEqual(self.driver.find_element_by_tag_name('h1').text, 'Contact Details')
        self.assertEqual(self.driver.find_element_by_name('full_name').get_attribute('value'), 'Jane Doe')

        self.driver.quit()
```

Note that this is a simplified example and you may need to add more functionality and error handling to your actual code.

Also, the selenium test is just an example and you may need to adjust it according to your actual use case.

To use the selenium test, you need to have the selenium package installed. You can install it using pip:
```bash
pip install selenium
```
You also need to have the Chrome driver installed on your system. You can download it from the official Chrome driver website:
https://chromedriver.chromium.org/downloads

After installing the Chrome driver, you need to add the path to the driver to your system's PATH environment variable.

Make sure to replace the `contact_details` url in the `tests.py` file with the actual url name from your `urls.py` file.

Make sure to run the tests using the `python manage.py test` command.