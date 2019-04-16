from django.shortcuts import render
from .models import contact
# Create your views here.
def home(request):
    context={
        'contacts':contact.objects.all(),
        
    }#basically here all the obects from the models field are passed as obect from views to templates
    return render(request,'index.html', context) #it helps in rendering the page


def detail(request,id):
    context={'contacts':get_object_or_404(contact,pk=id),
    }
    return render(request,'detail.html',context)


