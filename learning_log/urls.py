from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
	re_path(r'^admin/', admin.site.urls),
	re_path(r'^users/', include(('users.urls', 'users'), namespace='users')),
	re_path(r'', include(('learning_logs.urls', 'learning_logs'), namespace='learning_logs')),
]
