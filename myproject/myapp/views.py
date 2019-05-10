from django.views import generic
from .models import employee
from django.urls import reverse_lazy
from django.shortcuts import redirect,render
from django.contrib.auth import authenticate,login,logout
from .forms import UserForms


# Create your views here.




class IndexView(generic.ListView):
	template_name='myapp/index.html'
	context_object_name='employee_list'

	def get_queryset(self):
		return employee.objects.all()

class DetailView(generic.DetailView):
	model=employee
	template_name='myapp/detail.html'

class employeeCreateView(generic.CreateView):
	model=employee
	fields=['name','designation','gender','dp', 'video']


class employeeUpdateView(generic.UpdateView):
    model = employee
    fields=['name','designation','gender','dp']
    


class employeeDeleteView(generic.DeleteView):

	model = employee
	success_url = reverse_lazy('myapp:index')
	def get(self, request, pk):
		return self.post(request)

		

class UserFormView(generic.View):
	form_class = UserForms
	template_name = 'myapp/registration_form.html'

	#display blank form
	def get(self,request):
		form = self.form_class(None)
		return render(request, self.template_name,{'form':form})

	def post(self,request):
		form = self.form_class(request.POST)

		if form.is_valid():
			
			user = form.save(False)

			#cleaned data
			username=form.cleaned_data['username']
			password=form.cleaned_data['password']
			user.set_password(password)
			user.save()


			user =authenticate(username=username,password=password)

			if user is not None:

				if user.is_active:
					login(request,user)
					return redirect('myapp:index')

		return render(request, self.template_name,{'form':form})

def logout_view(request):
	logout(request)
	return redirect('myapp:index')