from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemRequest
from django.views.generic import ListView, DetailView, CreateView, UpdateView

# Create your views here
# def index(request):
#     context = {
#        'items': Item.objects.all()
#     }
#     return render(request, 'index.html', context)

class IndexListView(ListView):
    model = Item
    template_name = 'index.html'
    context_object_name = 'items'


class FoodDetailView(DetailView):
    model = Item
    template_name = 'details.html'

# def details(request, item_id:int):
#     context = {
#         'item': Item.objects.get(pk=item_id)
#     }
#     return render(request, 'details.html', context)


class FoodCreateView(CreateView):
    model = Item
    form_class = ItemRequest
    template_name = 'create_item.html'
    context_object_name = 'form'

    def form_valid(self, form):
        form.instance.user_id = self.request.user
        return super().form_valid(form)

# def create(request):
#     form = ItemRequest(request.POST or None)
#
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#
#     return render(request, 'create_item.html', {'form': form})


class FoodUpdateView(UpdateView):
    model = Item
    template_name = 'create_item.html'
    form_class = ItemRequest
    context_object_name = 'form'
#
# def edit(request, id:int):
#     item = Item.objects.get(pk=id)
#     form = ItemRequest(request.POST or None, instance=item)
#
#     if form.is_valid():
#         form.save()
#         return redirect('food:index')
#
#     return render(request, 'create_item.html', {'form': form})
#

def delete(request, id: int):
    Item.objects.filter(id=id).delete()
    return redirect('food:index')