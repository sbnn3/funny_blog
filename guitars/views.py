from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from .models import Guitars


class GuitarsPage(generic.ListView):
    model = Guitars
    queryset = Guitars.objects.filter(status=1).order_by('-created_on')
    template_name = 'guitars.html'
    paginate_by = 6


class GuitarsPagePost(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Guitars.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
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
