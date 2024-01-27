from django.forms import ModelForm, Textarea

from .models import Comment, Exercise


class CommentForm(ModelForm):
    """Form to ask for details of a comment."""

    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields["text"].widget.attrs.update({"class": "form-control"})
        self.fields["rating"].widget.attrs.update({"class": "form-control"})

    class Meta:
        model = Comment
        fields = ["text", "rating"]
        widgets = {
            "text": Textarea(attrs={"rows": 4}),
        }


class ExerciseForm(ModelForm):
    """Form to ask for details of a physical exercise for training."""

    class Meta:
        model = Exercise
        fields = [
            "title",
            "body",
            "soccer_skills",
            "for_adults",
            "for_jun_a",
            "for_jun_b",
            "for_jun_c",
            "for_jun_d",
            "for_jun_e",
            "for_jun_f",
            "for_jun_g",
            "image",
            "pdf",
            "youtube_link",
            "rating",
        ]
        labels = {
            "title": "Titel",
            "body": "Kurzbeschreibung",
            "soccer_skills": "Trainingsfokus",
            "for_adults": "Erwachsene",
            "for_jun_a": "A-Jun",
            "for_jun_b": "B-Jun",
            "for_jun_c": "C-Jun",
            "for_jun_d": "D-Jun",
            "for_jun_e": "E-Jun",
            "for_jun_f": "F-Jun",
            "for_jun_g": "G-Jun",
            "image": "Bild",
            "pdf": "pdf-Datei",
            "youtube_link": "Link zu Video",
            "rating": "Bewertung",
        }
