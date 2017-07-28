"""dhl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.auth import views as authentication

from track import views as track
from django.views.generic import RedirectView


from zinnia.sitemaps import TagSitemap
from zinnia.sitemaps import EntrySitemap
from zinnia.sitemaps import CategorySitemap
from zinnia.sitemaps import AuthorSitemap
from django.contrib.sitemaps import views as contribSitemaps
from zinnia.views.channels import EntryChannel
from django_xmlrpc import views as django_xmlrpc


from axes.decorators import watch_login
from allauth.account.views import login




admin.autodiscover()




urlpatterns = [
    url(r'^admin/tools/', include('admin_tools.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    
    url(r'^accounts/login/$', watch_login(login)),
    url(r'^accounts/logout/$', authentication.logout, {'next_page': '/'}),
    url(r'^accounts/', include('allauth.urls')),

    url(r'^accounts/$', RedirectView.as_view(url='/accounts/login/')),
    url(r'^login/$', RedirectView.as_view(url='/accounts/login/')),
    url(r'^logout/$', RedirectView.as_view(url='/accounts/logout/')),
    url(r'^signup/$', RedirectView.as_view(url='/accounts/signup/')),
    #url(r'^crispies/', include('crispy_forms_foundation_demo.urls')),

    #url(r'^home/', include('home.urls')),
    url(r'^blog/', include('zinnia.urls')),
    url(r'^comments/', include('django_comments.urls')),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    #url(r'^tickets/', include('tickets.urls', namespace='tickets')),
    url(r'^tracking/', include('track.urls')),
    url(r'^dhlavenues/', include('webhook.urls')),
    url(r'^$', RedirectView.as_view(url='/blog/')),
]

urlpatterns += staticfiles_urlpatterns()




sitemaps = {'tags': TagSitemap,
            'blog': EntrySitemap,
            'authors': AuthorSitemap,
            'categories': CategorySitemap,}

urlpatterns += [
    url(r'^sitemap.xml$', contribSitemaps.index, {'sitemaps': sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$', contribSitemaps.sitemap, {'sitemaps': sitemaps}),
    url(r'^xmlrpc/$', django_xmlrpc.handle_xmlrpc),
    url(r'^blog/$', EntryChannel.as_view(query='category:python OR category:django')),
    url(r'^blog/', include('zinnia.urls', namespace='blog')),
]





from django.conf import settings
from django.views import static

if settings.DEBUG :
    urlpatterns += [
        url(r'^media/(?P<path>.*)$', static.serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    ]
if settings.DEBUG :
    urlpatterns += [
        url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT, 'show_indexes': True}),
    ]







# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer












from zinnia.models import Entry

class EntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Entry
        """
            HyperlinkedModel
        """
        fields = ('title',
                    'slug',
                    'status',
                    'publication_date',
                    'start_publication',
                    'end_publication',
                    'creation_date',
                    'last_update',
                    'content',
                    'comment_enabled',
                    'pingback_enabled',
                    'trackback_enabled',
                    'comment_count',
                    'pingback_count',
                    'trackback_count',
                    'lead',
                    'excerpt',
                    'image',
                    'image_caption',
                    'featured',
                    'authors',
                    'categories',
                    'tags',
                    'login_required',
                    'password',
                    'content_template',
                    'detail_template',
                    )



class EntryViewSet(viewsets.ModelViewSet):
    queryset = Entry.objects.all()
    serializer_class = EntrySerializer





"""
from zinnia import models_bases
class RelatedEntrySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models_bases.RelatedEntry
        fields = ('related',)

# ViewSets define the view behavior.
class RelatedEntryViewSet(viewsets.ModelViewSet):
    queryset = RelatedEntry.objects.all()
    serializer_class = RelatedEntrySerializer
"""



from zinnia.models.author import Author
class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class AuthorViewSet(viewsets.ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer




from zinnia.models.category import Category
class CategorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Category
        fields = ('title','slug','description','parent')

# ViewSets define the view behavior.
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer










# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'entry', EntryViewSet)
#router.register(r'related', RelatedEntryViewSet)
router.register(r'authors', AuthorViewSet)
router.register(r'categories', CategoryViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns += [
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
