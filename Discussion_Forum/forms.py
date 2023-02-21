from django.forms import ModelForm
from .models import *

class CreateInForum(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateInForum, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs = {
            'id':'name',
            'class':'form-control'
        }
        self.fields['email'].widget.attrs = {
            'id':'email',
            'class':'form-control'
        }
        self.fields['topic'].widget.attrs = {
            'id':'topic',
            'class':'form-control'
        }
        self.fields['description'].widget.attrs = {
            'id':'description',
            'class':'form-control'
        }
        self.fields['link'].widget.attrs = {
            'id':'link',
            'class':'form-control'
        }

    class Meta: 
        model = Forum
        fields = '__all__'

 
class CreateInDiscussion(ModelForm):
    def __init__(self, *args, **kwargs):
        super(CreateInDiscussion, self).__init__(*args, **kwargs)
        self.fields['forum'].widget.attrs = {
            'id':'forum',
            'class':'form-control'
        }
        self.fields['discuss'].widget.attrs = {
            'id':'discuss',
            'class':'form-control'
        }
    class Meta:
        model= Discussion
        fields = "__all__"