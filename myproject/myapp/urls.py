from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
 
app_name='myapp'

urlpatterns = [
    path('',views.IndexView.as_view(),name='index'),
    path('detail/<int:pk>/',views.DetailView.as_view(),name='detail'),
    path('employee/add/',views.employeeCreateView.as_view(),name='employee-add'),
    path('employee/update/<int:pk>/',views.employeeUpdateView.as_view(),name='employee-update'),
    path('employee/delete/<int:pk>/',views.employeeDeleteView.as_view(),name='employee-delete'),
    path('register/',views.UserFormView.as_view(),name='register'),
    path('logout/',views.logout_view,name='logout'),
]

if settings.DEBUG:
	urlpatterns +=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
	urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)