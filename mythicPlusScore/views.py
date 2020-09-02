from django.shortcuts import render, redirect
from .models import PostCharacterInfo
from .form import CharacterInput


def search_new(request):

    if request.method == 'POST':
        form = CharacterInput(request.POST)
        if form.is_valid():
            PostCharacterInfo.name = form['name']
            PostCharacterInfo.realm=form['realm']
            PostCharacterInfo.server=form['server']
            PostCharacterInfo.save()

            return redirect('form')

    else:
        form = CharacterInput()

    recent2 = PostCharacterInfo.objects.all
    context = {'form': form, 'recent2': recent2}

    return render(request, 'mythicPlusScore/past_list.html', context, )
