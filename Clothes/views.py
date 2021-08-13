from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *
from .forms import *


# Create your views here.

# a = Shoes.objects.all()
def shoez(request, pk_shoe):
    shoe = Shoes.objects.get(id=pk_shoe)
    run = shoe.runs_set.all()

    

    return render(request, 'Clothes/shoez.html',{
        # "Counties" : County.objects.all(),
        # "Sumup" : sum([list(a[i].values())[0] for i in range(len(a))])
        "Shoes" : shoe,
        "Runs" : run
    })

def dashboard(request):
    return render(request, 'Clothes/dashboard.html',{
        "Shoe" : Shoes.objects.all(),
        "Run" : Runs.objects.all()
    })

def create_run(request):
    RunFormSet = inlineformset_factory(Shoes, Runs
        ,fields= '__all__'
        ,extra=5
        ,widgets={'duration':SelectDateWidget()}
        ,form=RunForm)
    formset = RunFormSet()
    if request.method == 'POST':
        formset = RunFormSet(request.POST,instance=formset.instance)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    # Optimal_Num = 6

    # if request.method == 'POST':
    #     # print(request.POST)
    #     formSet = [RunForm(request.POST, prefix=i) for i in range(Optimal_Num)]
    #     if any(form.is_valid() for form in formSet):
    #         formSet.save()
    #         return redirect('/')
    # else:
    #     formSet = [RunForm(prefix=i) for i in range(Optimal_Num)]
    return render(request, 'Clothes/run_form.html',{
        "Forms" : formset
    })


def clothset(request):
    return render(request, 'Clothes/clothset.html',{
        "Clothset" : Clothets.objects.all()
    })

