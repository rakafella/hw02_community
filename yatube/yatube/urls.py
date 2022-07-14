from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    # импорт правил из приложения posts
    path('', include('posts.urls', namespace='posts')),
    path('group/<slug:slug>/', include('posts.urls')),
    path('admin/', admin.site.urls),
]
