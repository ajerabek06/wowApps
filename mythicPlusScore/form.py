from django.forms import ModelForm
from .models import PostCharacterInfo


class CharacterInput(ModelForm):

    class Meta:
        model = PostCharacterInfo
        fields = ['name', 'realm', 'server']
