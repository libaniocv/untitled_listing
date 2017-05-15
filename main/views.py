from django.shortcuts import render
from django.http import HttpResponse
from . import forms

# Create your views here.

def index(request):
    context={}
    return render(request,'index.html',context)

def registrar(request):
    registrado=False
    if request.method=='POST':
        user_form=forms.UserForm(data=request.POST)


        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()

            registrado=True

        else:
            print user_form.errors
    else:
        user_form=forms.UserForm

    context={
        'user_form':user_form,
        'registered':registrado
    }
    return render(request,'registrar.html',context)

def adicionarmat(request):
    if request.method=='POST':
        form=forms.AddMatForm(request.POST)

        if form.is_valid():
            print(form.data['nome'])
            print(form.data)
            #form.save()
            temp=form.data['nome']
            temp2=models.Licaoo(nome=temp,curriculos=models.Curriculo.objects.get(id=id_curriculo))
            temp2.save()

            return HttpResponse("Lição salva com sucesso")
        else:
            print form.errors
    else:
        form=forms.FormLicao()

    context={'form':form,
             'id_curriculo':id_curriculo}

    return render()


#TODO terminar esta view
def pesquisar(request,termo):


    return