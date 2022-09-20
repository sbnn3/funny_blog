from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import Guitars
from .forms import SubmitGuitarForm


class GuitarsPage(generic.ListView):
    model = Guitars
    queryset = Guitars.objects.filter(status=1).order_by('-created_on')
    template_name = 'guitars.html'
    paginate_by = 6


def submit_guitar(request):
    if request.method == 'POST':
        submission_form = SubmitGuitarForm(request.POST, request.FILES)
        if submission_form.is_valid():
            submission_form.instance.artist = request.user
            submission_form.save()
            messages.success(
                request, "Well done! Please, wait for approval :)")
            return redirect('guitars')
        else:
            submission_form = SubmitGuitarForm()
    
    return render(
        request, 
        'submit-guitar.html', 
        {
            'submission_form': SubmitGuitarForm(),
        },  
    )

def edit_guitar_post(request, slug):
    guitars = get_object_or_404(Guitars, slug=slug)
    edit_form = SubmitGuitarForm(request.POST or None, instance=guitars)
    context = {
        'edit_form': edit_form,
        'guitars': guitars
    }

    if request.method == 'POST':
        edit_form = SubmitGuitarForm(
            request.POST, request.FILES, instance=guitars)
        if edit_form.is_valid():
            guitars = edit_form.save(commit=False)
            guitars.artist = request.user
            guitars.save()
            return redirect('guitars')
    else:
        edit_form = SubmitGuitarForm(instance=guitars)

    return render(request, 'edit-guitar.html', context)


def delete_guitar_post(request, slug):
    guitars = get_object_or_404(Guitars, slug=slug)
    guitars.delete()
    return redirect('guitars')


class GuitarsPagePost(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Guitars.objects.filter(status=1)
        guitars = get_object_or_404(queryset, slug=slug)
        liked = False
        if guitars.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request, 
            "guitars-post.html",
            {
                "guitars": guitars,
                "liked": liked,
            },
        )


class LikeGuitarPost(View):

    def post(self, request, slug):
        guitars = get_object_or_404(Guitars, slug=slug)

        if guitars.likes.filter(id=request.user.id).exists():
            guitars.likes.remove(request.user)
        else:
            guitars.likes.add(request.user)

        return HttpResponseRedirect(reverse('guitars-post', args=[slug]))
