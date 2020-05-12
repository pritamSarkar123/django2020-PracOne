from django import forms
from django.core import validators


# def check_name_p(value):
#     if value[0].lower() != 'p':
#         raise forms.ValidationError('Name must starts with p or P')


# class FormName(forms.Form):
#     name = forms.CharField(required=True, validators=[check_name_p])
#     email = forms.EmailField(required=True)
#     text = forms.CharField(widget=forms.Textarea, required=True)
#     botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
#                                  validators=[validators.MaxLengthValidator(0)])

#     # def clean_botcatcher(self):
#     #     botcatcher = self.cleaned_data.get('botcatcher')
#     #     if len(botcatcher) > 0:
#     #         raise forms.ValidationError('GOTCHA BOT!')
#     #     return botcatcher

def mail_function(email, vmail):
    if email != vmail:
        raise forms.ValidationError('Correct your Email')


def name_function(name):
    if name[0].lower() != 'p':
        raise forms.ValidationError('Name must starts with P or p')


def bot_function(botchecker):
    if len(botchecker) > 0:
        raise forms.ValidationError('GOTCHA Fucking BOT!!!')


class FormName(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    vmail = forms.EmailField(required=True)
    text = forms.CharField(widget=forms.Textarea, required=True)
    botcatcher = forms.CharField(widget=forms.HiddenInput, required=False)

    def clean(self):
        all_cleaned_data = super().clean()

        # email varification
        email = all_cleaned_data.get('email')
        vmail = all_cleaned_data.get('vmail')
        mail_function(email, vmail)

        # name varification
        name = all_cleaned_data.get('name')
        name_function(name)

        # bot checker
        botchecker = all_cleaned_data.get('botcatcher')
        bot_function(botchecker)
