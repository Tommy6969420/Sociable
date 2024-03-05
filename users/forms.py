from django import forms
from.models import User, Post
class DateInput(forms.DateInput):
    input_type='date'
class UserForm(forms.ModelForm):
    #to apply certain changes to all fields
    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update({'class': 'form-control'})
    class Meta:
        model=User
        fields="__all__"
        widgets={
            'password':forms.PasswordInput(attrs={"placeholder":"keep it secret and strong",}),
            'username':forms.TextInput(attrs={"placeholder":"Should be unique for this application"}),
            'date_of_birth': forms.DateInput(format="%d/%m/%Y",attrs={'placeholder':"dd/mm/yyyy", }),  #'min':'01/01/1950',max:"31/12/2010",
            'gender':forms.RadioSelect(attrs={"class":"genderBtn"})
        }
class PostForm(forms.ModelForm):
    class Meta:
        model= Post
        fields = ["description", "image",]
        widgets={
            'description':forms.TextInput(attrs={"placeholder":"Your thoughts here"}),
        }
