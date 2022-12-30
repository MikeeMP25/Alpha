from django import forms


class ContactFrom(forms.Form):
    name = forms.CharField(label="Nombre", required=True, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingrese su nombre completo'}
    ), min_length=3, max_length=100)
    email = forms.EmailField(label="Correo", required=True, widget=forms.EmailInput(
        attrs={'class': 'form-control', 'placeholder': 'Ingrese su e-mail'}
    ), min_length=3, max_length=100)
    content = forms.CharField(label="Contenido", required=True, widget=forms.Textarea(
        attrs={'class': 'form-control', 'placeholder': 'Ingrese su mensaje', 'rows': 3}
    ), min_length=10, max_length=1000)
