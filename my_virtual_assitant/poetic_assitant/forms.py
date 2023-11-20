from django import forms

class Prompts_Form(forms.Form):
    user_entery = forms.CharField(max_length=50, 
                        widget=forms.TextInput(attrs={
                            'class': 'w3-button w3-border  w3-round-xlarge',
                            'placeholder': 'Introduz o nome do topíco...'
                        }))