"""
NurProject1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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

# Uncomment next two lines to enable admin:
#from django.contrib import admin
#from django.urls import path
from pet import views
from django.urls import path

urlpatterns = [
    # Uncomment the next line to enable the admin:
    #path('admin/', admin.site.urls)
    path('abt', views.about, name = 'abt'),
    path('next', views.blog, name = 'blog'),
    path('go', views.contact, name = 'contact'),
    path('', views.index, name = 'index'),
    path('pro', views.showproduct, name = 'pro'), 
    path('let', views.random),
    path('two', views.service, name = 'service' ),
    path('why', views.team, name = 'team'),
    path('who', views.testimonial, name = 'test'),\
    path('Add',views.ProductAdd),
    path('delete/<int:PK>',views.deleteData,name='delete'),
    path('update/<int:PK>',views.updateData,name='update'),
    path('Sign', views.SignUp,name='Sign'),
    path('Log', views.Login,name='Log'),
    path('cart', views.viewCart,name='cart'),
    path('Acart/<int:pid>', views.addcart, name='Acart'),
    
]
