from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import BlogEntry

class BlogEntryListView(ListView):
    model = BlogEntry
    template_name = 'blog/blogentry_list.html'

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        return queryset.filter(is_published=True)

class BlogEntryDetailView(DetailView):
    model = BlogEntry
    template_name = 'blog/blogentry_detail.html'

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

class BlogEntryCreateView(CreateView):
    model = BlogEntry
    fields = ['title', 'content', 'preview', 'is_published']
    success_url = reverse_lazy('blog:list')

class BlogEntryUpdateView(UpdateView):
    model = BlogEntry
    fields = ['title', 'content', 'preview', 'is_published']

    def get_success_url(self):
        return reverse_lazy('blog:detail', kwargs={'pk': self.object.pk})

class BlogEntryDeleteView(DeleteView):
    model = BlogEntry
    success_url = reverse_lazy('blog:list')
