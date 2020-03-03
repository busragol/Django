from django.shortcuts import render,redirect,get_object_or_404
from .AddUser_models import AddUser
from .AddUser_forms import AddUserForm

def UserList_create(request,*args,**kwargs):
    list_of_user=AddUser.objects.all()


    context={
        'list_of_user':list_of_user,
    }
    return render(request,'UserList.html',context)


def UserList_update(request,id,*args,**kwargs):
    user= get_object_or_404(AddUser, id=id)
    form=AddUserForm(request.POST or None,instance=user)

    if form.is_valid():
        form.save()
        return redirect('UserListcreate')
    context = {
        'form': form,
    }
    return render(request,'UpdateUser.html',context)



