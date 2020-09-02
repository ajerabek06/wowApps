from django.shortcuts import render, redirect
from .models import PostCharacterInfo
from .form import CharacterInput


def search_new(request):

    if request.method == 'POST':
        model_instance = PostCharacterInfo()
        form = CharacterInput(request.POST, instance=model_instance)
        print(model_instance)
        if form.is_valid():
            model_instance.save()

            return redirect('form')

    else:
        form = CharacterInput()

    recent2 = PostCharacterInfo.objects.all
    context = {'form': form, 'recent2': recent2}

    return render(request, 'mythicPlusScore/past_list.html', context, )
