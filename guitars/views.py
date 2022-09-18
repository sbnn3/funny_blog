from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Guitars


class GuitarsPage(generic.ListView):
    model = Guitars
    queryset = Guitars.objects.filter(status=1).order_by('-created_on')
    template_name = 'guitars.html'
    paginate_by = 6


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
        guitars = get_object_or_404(GuitarsPage, slug=slug)

        if guitars.likes.filter(id=request.user.id).exists():
            guitars.likes.remove(request.user)
        else:
            guitars.likes.add(request.user)

        return HttpResponseRedirect(reverse('guitars-post', args=[slug]))
