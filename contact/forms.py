from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Create a form for the contact model
    """
    class Meta:
        """
        Display the required fields
        """
        model = Contact
        fields = "__all__"

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)
        """
        Add Placeholder to form fields
        """
        placeholders = {
            'name': 'Name',
            'email': 'Email Address',
            'phone': 'Phone number',
            'location': 'Your Location',
            'message': 'Your Message',
        }

        for field in self.fields:
            if field != 'topic':
                if self.fields[field].required:
                    placeholder = f'{placeholders[field]} *'
                else:
                    placeholder = placeholders[field]
                self.fields[field].widget.attrs['placeholder'] = placeholder
            self.fields[field].label = False
            # add class to fields
            self.fields[field].widget.attrs['class'] = 'my-2'
