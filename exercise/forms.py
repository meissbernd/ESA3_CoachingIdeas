from django.forms import ModelForm, Textarea
from .models import Comment


class CommentForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args,
                                        **kwargs)
        self.fields['text'].widget.attrs.update({'class': 'form-control'})
        self.fields['rating'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Comment
        fields = ['text', 'rating']
        widgets = {
            'text': Textarea(attrs={'rows': 4}),
        }
