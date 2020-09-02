from django.shortcuts import render, redirect, get_object_or_404
from .models import PostCharacterInfo
from .form import CharacterInput


def search_new(request):

    if request.method == 'POST':
        model_instance = PostCharacterInfo()
        form = CharacterInput(request.POST, instance=model_instance)
        print(model_instance)
        if form.is_valid():
            model_instance.save()
            return redirect('post_detail',pk=model_instance.pk)
    else:
        form = CharacterInput()
    # recent2 = PostCharacterInfo.objects.all
    context = {'form': form, }
    return render(request, 'mythicPlusScore/search_new.html', context, )


def view_prior(request):
    recent2 = PostCharacterInfo.objects.all
    return render(request, 'mythicPlusScore/past_list.html', {'recent2': recent2})


def post_detail(request, pk):
    recent2 = get_object_or_404(PostCharacterInfo, pk=pk)
    return render(request, 'mythicPlusScore/post_detail.html', {'recent2': recent2})
