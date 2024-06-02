from django import forms


from pet.models import AddProduct
class newProduct(forms.ModelForm):
    class Meta:
        model = AddProduct
        fields = '__all__'