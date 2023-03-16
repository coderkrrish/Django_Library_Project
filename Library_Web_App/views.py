from django.shortcuts import render,HttpResponse,redirect
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
@csrf_exempt
@login_required
def Home(request):
     
    if request.method == "POST":
        data = request.POST
        # print(request.POST)  #TO get query parameters
        bid = data.get("Book_id")
        name = data.get("Book_Name")
        price = data.get("Book_Price")
        author = data.get("Book_Author")
        genere = data.get("Book_Genre")
        is_pub = data.get("Book_is_pub")
        print(name, price, author, genere, is_pub)
        if is_pub == "Yes":
            is_pub = True
        else:
            is_pub = False

        if not bid:

            Book.objects.create(Book_Name = name, Book_Price = price, Book_Author = author, Book_Genere = genere, Is_Published = is_pub)
        
        else:
            book_obj = Book.objects.get(id = bid)
            book_obj.Book_Name = name
            book_obj.Book_Price = price
            book_obj.Book_Author = author
            book_obj.Book_Genere = genere
            book_obj.Is_Published = is_pub
            book_obj.save()


        return redirect("Home_Page")

        # return HttpResponse("Success")
    elif request.method == "GET":
       
        return render(request, "Home1.html")

@login_required
def Display_Books(request):
    return render(request , "DisplayBooks.html", {"All_Books" : Book.objects.filter(Is_Active = True) , "active" : True})

@login_required
def Update_Book(request,pk):
    book_obj = Book.objects.get(id=pk)

    return render(request,"Home.html", context = {"Single_Book" : book_obj})

@login_required
def Delete_Book(request,pk):
        Book.objects.get(id=pk).delete()
        return redirect("All_Active_Books")

@login_required
def Soft_Delete(request,pk):
    book_obj = Book.objects.get(id = pk)
    book_obj.Is_Active = False
    book_obj.save()
    return redirect("All_Active_Books")


@login_required
def Inactive_Book(request):
    
  return render(request , "DisplayBooks.html", {"All_Books" : Book.objects.filter(Is_Active = False),"inactive" : True})

@login_required
def Restore_Book(request, pk):
    book_obj = Book.objects.get(id = pk)
    book_obj.Is_Active = True
    book_obj.save()
    return redirect("All_Active_Books")

from .Django_Forms import BookForm,AddressForm

from django.contrib.auth.forms import UserCreationForm 
def book_form(request):

    form = BookForm()

    if request.method == 'POST':
        
        if form.is_valid():
            form.save()
            return HttpResponse("Successfully Registered!!!")
    else:

        context = {'form':form}
        return render (request  ,"book_form.html", context=context)
    
    # return render(request, 'users/register.html',context)
   

@login_required
def Crispy_form(request):
    return render(request , "Crispy_sibtc.html" , {"form" : AddressForm()})



from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    books_list = Book.objects.all()
    page = request.GET.get('page', 1)

    paginator = Paginator(books_list, 2)
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)

    return render(request, 'index.html', { 'All_Books': books })


from django.http import HttpResponse  
from django.views import View  
class NewView(View):  
    def get(self, request):  #In class based views the name of the method should be "get" only.Method name other than "get" will not load the page 
        # View logic will place here  
        return HttpResponse('In Class Based Views')



from django.views.generic.edit import CreateView 
class BookCreate(CreateView):  
    model = Book  
  
    fields = '__all__'  
    success_url = '/cbv-create-book/'



from django.views.generic.list import ListView  
  
class BookRetrieve(ListView):  
    model = Book 

    context_object_name = "All_Books"


from django.views.generic.detail import DetailView  
  
class BookDetail(DetailView):  
    model = Book  

    http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']

from django.views.generic.edit import UpdateView  
class BookUpdate(UpdateView):  
    model = Book  

    fields = "__all__"



from django.views.generic.edit import DeleteView  
  
class BookDelete(DeleteView):  
    model =  Book 
  
    # here we can specify the URL   
    # to redirect after successful deletion  
    success_url = '/Books/' 



from django.views.generic import FormView 
class Form(FormView):
    pass
    


from django.http import HttpResponse
import csv
from .models import Book

def create_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="Books_Data.csv"'

    writer = csv.writer(response)
    writer.writerow(['Book_Name','Book_Price','Book_Author','Book_Genere','Is_Published'])

    books= Book.objects.all().values_list('Book_Name','Book_Price','Book_Author','Book_Genere','Is_Published')
    for book in books:
        writer.writerow(book)
 
    return response

def upload_csv(request):
    file = request.FILES["CSV_File"]
    print(file)
    return HttpResponse


