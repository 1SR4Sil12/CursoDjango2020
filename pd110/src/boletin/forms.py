from django import forms

from .models import Registrado

class RegModelForm(forms.ModelForm):
	class Meta:
		model = Registrado
		fields = ["nombre", "email"]

	def clean_email(self):
		email = self.cleaned_data.get("email")
		email_base, proveedor = email.split("@")
		dominio, extension = proveedor.split(".")
		if not dominio == "iesfernandoaguilar":
			raise forms.ValidationError("Por favor, utiliza un email con el dominio iesfernandoaguilar")
		return email

	def clean_nombre(self):
		nombre = self.cleaned_data.get("nombre")
		return nombre

class RegForm(forms.Form):
	nombre = forms.CharField(max_length=100)
	email = forms.EmailField()