
from django.contrib import admin
from django.urls import path,include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

schema_view = get_schema_view(
    openapi.Info(
        title="My API",
        default_version='v1',
        description="My API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="Awesome License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('v1/admin/', admin.site.urls),
    path('v1/auth/', include('authentification.urls')),
    path('v1/base/', include('base.urls')),
    path('v1/achat/', include('achats.urls')),
    path('v1/vente/', include('ventes.urls')),
    path('v1/paiment/', include('paiments.urls')),
    path('v1/depense/', include('depense.urls')),




    path('v1/swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += [path('silk/', include('silk.urls', namespace='silk'))]
