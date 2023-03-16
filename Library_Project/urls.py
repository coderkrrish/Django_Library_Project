"""Library_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from Library_Web_App import views
from Users_Activity import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Welcome/', views.Home ,name = "Home_Page"),
    path("Books/", views.Display_Books, name = "All_Active_Books"),
    path("Update/<int:pk>" ,views.Update_Book, name = "Update_Book"),
    path("Delete/<int:pk>", views.Delete_Book, name = "Delete"),
    path("Soft-Delete/<int:pk>", views.Soft_Delete , name = "Soft_Delete"),
    path("Inactive-book/" , views.Inactive_Book, name = "Inactive"),
    path("Restore/<int:pk>", views.Restore_Book , name = "Restore"),
    path("book-form/" ,views.book_form ,name = "book_form"),
    path("crispy/" , views.Crispy_form , name = "Crispy_form"), 
       
    path("index/",views.index, name = "index"),
    # path('__debug__/',include('debug_toolbar.urls')),


    #Users Urls
   
    path("register/" , user_views.register_request , name = "register"),
    path("login/" , user_views.login_request , name = "login_user"),
    path("logout/"  ,user_views.logout_request, name = "logout_user"),
    path("create-csv/",views.create_csv,name = "create_csv"),
    path("upload-csv/",views.upload_csv,name = "upload_csv"),

    

    #How to add the url for class based views
    path("cbv/", views.NewView.as_view(), name = "class_based_view"),

    path('cbv-create-book/', views.BookCreate.as_view(), name = 'book_create'),

    path('retrieve/', views.BookRetrieve.as_view(), name = 'bookretrieve'),

    path('retrieve/<int:pk>', views.BookDetail.as_view(), name = 'bookdetail') , 

    path('update/<int:pk>', views.BookUpdate.as_view(), name = 'Bookupdate'),  

    path('delete/<pk>', views.BookDelete.as_view(), name = 'bookdelete'), 

]

