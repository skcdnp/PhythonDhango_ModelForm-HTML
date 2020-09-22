#sample code to take advantage of bootstrap and modelform to create a little more visually appealing forms.

from django.forms import ModelForm

classTestRequestForm(ModelForm):

    class Meta:
        model = YourModel
        fields = ['field1', 'field2', 'field3', ] #fields that make sense to your model
        widgets = {
            'field1': forms.TextInput(attrs={'class': 'form-control',}), # using bootstrap now this field will be represeted as textinput
            'field2': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Please enter valid email address (john@gmail.com)'}),# using bootstrap now this field will be represeted as emailinput
            'field3': forms.Select(attrs={'class': 'form-control'}), # using bootstrap now this field will be represeted as selection

        }


