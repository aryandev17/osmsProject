from django import forms
from .models import Contact
from dashboard.models import UserReview

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
        widgets = {
            "name" : forms.TextInput(attrs={"placeholder": "Your Name"}),
            "email" : forms.EmailInput(attrs={"placeholder": "Your Email"}),
            "message": forms.Textarea(attrs={"placeholder":"Your Message"})
        }

class UserReviewForm(forms.ModelForm):
    review = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"Write your review here.."}))
    review_title = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Review Title"}))
    class Meta:
        model = UserReview
        fields = ("review_title","review",)
