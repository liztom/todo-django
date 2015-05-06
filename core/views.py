from django.shortcuts import render_to_response, render, redirect
from django.views.generic import ListView, DetailView

from .models import List, Item


class ListView(ListView):
    template_name = "all_lists.html"
    model = List

class ListDetailView(DetailView):
    template_name = "list_detail.html"
    model = List



    
# def all_lists(request):
#     lists = List.objects.all()
    
#     return render(request, 'all_lists.html',  { 'lists': lists })

# def new_list(request):
#     if request.method == "POST" and request.POST['list_name']:
#         list_name = request.POST['list_name']
#         List(name=list_name).save()
#         lists = List.objects.all()
#         return redirect('all_lists')

#     else:
#         lists = List.objects.all()
#         return render(request, 'all_lists.html', {'lists': lists, 'error_message': "You didn't enter a name."})

# def delete_list(request, list_id):
#     delete_list = List.objects.get(pk=list_id)
#     delete_list.delete()
    
#     lists = List.objects.all()
#     return render(request, 'all_lists.html', {'lists': lists})

# def detail_list(request, list_id):
#     single_list = List.objects.get(pk=list_id)
  
#     return render(request, 'list_detail.html', {'list': single_list})

# def edit_list(request, list_id):
#     pass

# def new_item(request, list_id):
#     single_list = List.objects.get(pk=list_id)
#     item_name = request.POST['item_name']
#     Item(name=item_name, todolist_id=list_id).save()
    
#     return render(request, 'list_detail.html', {'list': single_list})

# def delete_item(request, item_id):
#     item = Item.objects.get(pk=item_id)
#     single_list = List.objects.get(pk=item.todolist_id)
#     item.delete()

#     return render(request, 'list_detail.html', {'list': single_list})

