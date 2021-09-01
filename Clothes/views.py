from django.db.models import Sum, Count
from django.shortcuts import render, redirect
from django.forms import inlineformset_factory
from .models import *
from .forms import *
from .filters import *
from django.contrib.auth.decorators import login_required
from .decorators import *

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def shoez(request, pk_shoe):
    shoe = Shoes.objects.get(id=pk_shoe)
    runs = shoe.runs_set.all()
    rfilter = RunFilter(request.GET, queryset=runs)
    
    

    return render(request, 'Clothes/shoez.html',{
        # "Counties" : County.objects.all(),
        # "Sumup" : sum([list(a[i].values())[0] for i in range(len(a))])
        "Run_count" : runs.count,
        "Shoes" : shoe,
        "filter" : rfilter,
        "Runs" : rfilter.qs
    })
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def modify_run(request, pk_run):
    run = Runs.objects.get(id=pk_run)
    Form = RunForm(instance=run)
    if request.method == 'POST':
        Form = RunForm(request.POST, instance=run)
        if Form.is_valid():
            Form.save()
        return redirect('shoez', pk_shoe = Shoes.objects.get(nameS=run.shoe).id)

    return render(request, 'Clothes/run_formM.html',{
        "Form" : Form,
    })
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def dashboard(request):
    return render(request, 'Clothes/dashboard.html',{
        "Shoe" : Shoes.objects.all(),
        "Runs" : Runs.objects.all(),
        "Esy_Run" : Runs.objects.filter(target__nameT="Esy").count(),
        "Miles" : Runs.objects.aggregate(Sum('mileage'))
    })
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def add_run(request, pk_shoe):
    shoe = Shoes.objects.get(id=pk_shoe)
    RunFormSet = inlineformset_factory(Shoes, Runs,
        fields='__all__',
        widgets={'duration':SelectDateWidget()},
        extra=6
        )
    formset = RunFormSet(queryset=Runs.objects.none(),instance=shoe)
    if request.method == 'POST':
        formset = RunFormSet(request.POST,instance=shoe)
        if formset.is_valid():
            formset.save()
            return redirect('shoez', pk_shoe = shoe.id)

    return render(request, 'Clothes/run_formA.html',{
        'formset' : formset
    } )
@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def retire_shoe(request,pk_shoe):
    shoe = Shoes.objects.get(id=pk_shoe)
    if request.method == 'POST':
        shoe.delete()
        return redirect('shoez', pk_shoe = shoe.id)

    return render(request, 'Clothes/delete.html', {
        'saygoodbye' : shoe
    })

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def create_run(request):
    # RunFormSet = inlineformset_factory(Shoes, Runs
    #     ,extra=5
    #     ,widgets={'duration':SelectDateWidget()}
    #     ,form=RunFormM)
    # formset = RunFormSet()
    # if request.method == 'POST':
    #     formset = RunFormSet(request.POST)
    #     if formset.is_valid():
    #         formset.save()
    #         return redirect('dashboard')
    Optimal_Num = 6

    if request.method == 'POST':
        # print(request.POST)
        formSet = [RunForm(request.POST, prefix=i) for i in range(Optimal_Num)]
        if any(form.is_valid() for form in formSet):
            formSet.save()
            return redirect('/')
    else:
        formSet = [RunForm(prefix=i) for i in range(Optimal_Num)]
    return render(request, 'Clothes/run_form.html',{
        "Forms" : formSet
    })

@login_required(login_url='login')
@allowed_users(allowed_roles=['viewer','admin'])
def userPage(request):
    try:
        runs = request.user.clothets.runs_set
        return render(request, 'Clothes/user.html', {
            "Runs" : runs.all(),
            "Esy_Run" : runs.filter(target__nameT="Esy").count(),
            "Miles" : runs.aggregate(Sum('mileage'))
        })
    except Clothets.DoesNotExist:
        return redirect('clothset_info')
        # render({
        #     "Message" : 'Please fill in the form'
        # }))

@login_required(login_url='login')
@allowed_users(allowed_roles=['viewer','admin'])
def clothsetInfo(request):
    try:
        form = ClothsetForm(instance=request.user.clothets)
        if request.method == 'POST':
            form = ClothsetForm(request.POST, request.FILES, instance=request.user.clothets)
            if form.is_valid():
                form.save()
    except Clothets.DoesNotExist:
        form = ClothsetForm()
    return render(request, 'Clothes/clothset_info.html', {
        "Form" : form
    })