
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from orderappp import views as signview
#from teacher import views as tv
#from student import views as sv

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', signview.index, name="index"),
    path('accounts/login/', signview.index, name="index"),
    path("signup/", signview.signupviewfunc, name="signup"),
    path("logout/",signview.logout_user, name='logout'),
    path("dashboard/", signview.dashboardfunc, name="dashboard"),
    path("order/", signview.orderfunc, name="order"),
    path("add_product/", signview.add_product, name="add_product"),
    path("u_product/<int:id>", signview.edit_product, name="edit_product"),
    path("update_product/<int:id>", signview.update_product, name="update_product"),
    path("delete_product/<int:id>", signview.delete_product, name="delete_product"),
    path("profile/", signview.showprofile, name="profile"),
    path("user_register/", signview.user_register, name="user_register"),
    #path("notice/<int:id>", nv.notice_details, name="notice_details"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
