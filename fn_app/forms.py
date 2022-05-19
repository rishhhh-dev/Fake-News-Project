from django import forms


class Article_Form(forms.Form):
    title =forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class': 'form-control',
                'placeholder':'Enter the title'
            }
        )
    )
    content = forms.CharField(
            widget=forms.Textarea(
                attrs={
                    'class':'form-control',
                    'placeholder':'Enter the Content'
                }
            )
        )
    author = forms.CharField(
        widget= forms.TextInput(
            attrs={
            'class' : 'form-control',
                'placeholder':'Enter the author name'
            }
        )
    )



class TitleForm(forms.Form):

    title = forms.CharField(
        widget= forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter the Title'
            }
        )
    )