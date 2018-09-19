from django import forms
from django.core import validators

#def check_for_z(value):
    #if value[0].lower()!='z':
    #    raise forms.ValidationError("name needs to start with z")


class Formname(forms.Form):
    name=forms.CharField()
    email=forms.EmailField()
    verify=forms.EmailField(label='confirm email')
    text=forms.CharField(widget=forms.Textarea)
    bot=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    #def clean_bot(self):
        #bot=self.cleaned_data['bot']
    #    if len(bot)>0:
        #    raise forms.ValidationError("gotcha bot")
    #    return bot

    def clean(self):
        all_clean=super().clean()
        email=all_clean['email']
        vmail=all_clean['verify']

        if email != vmail :
            raise forms.ValidationError("make sure this coderuns")
