from django import forms
from .models import User

class RegisterForm(forms.ModelForm):
    
    password_confirm = forms.CharField(
        label="Parolni tasdiqlang",
        widget=forms.PasswordInput()
    )

    class Meta:
        model = User
        fields = ["username", "email", "password", "is_teacher"]
        
        widgets = {
            'password': forms.PasswordInput(),
        }

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({"class": "form-control", "placeholder": "Foydalanuvchi nomi"})
        self.fields["email"].widget.attrs.update({"class": "form-control", "placeholder": "example@gmail.com"})
        self.fields["password"].widget.attrs.update({"class": "form-control", "placeholder": "Parol kiriting"})
        self.fields["password_confirm"].widget.attrs.update({"class": "form-control", "placeholder": "Parolni qayta kiriting"})
        
    
        self.fields["is_teacher"].widget.attrs.update({"class": "form-check-input"})

    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Kiritilgan parollar bir-biriga mos kelmadi!")
        return cleaned_data