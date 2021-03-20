from django import forms


class ContactForm(forms.Form):
    fullName = forms.CharField(widget=forms.TextInput(
        attrs={"class": "form-control", "id": "form_full_name", "placeholder": "Your Full Name"}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={"class": "form-control", "id": "email", "placeholder": "Email"}))
    content = forms.CharField(widget=forms.Textarea(attrs={"class": "form-control", "placeholder": "Your Message"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
