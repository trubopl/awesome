from django.conf.urls import url, include
from django.conf import settings
from django.contrib import admin
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from django.conf.urls.static import static

from core.views import Index, PaydayLoans, FirstFreeLoan, SingleCompany,\
    Companies, Blog, BlogPosts
from core.sitemaps import StaticSitemap, PostsSitemap, SingleCompanySitemap


sitemaps = {
    'static': StaticSitemap,
    'posts:': PostsSitemap,
    'companies': SingleCompanySitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    url(r'^$', Index.as_view(), name='index'),
    url(r'^kalkulator-wyniki/', Index.as_view(), name='generate'),
    url(r'^chwilowki/', PaydayLoans.as_view(), name='payday_loans'),
    url(r'^blog/$', Blog.as_view(), name="blog"),
    url(r'^blog/(?P<post>[\w-]+)/$', BlogPosts.as_view(), name="blog_posts"),
    url(r'^darmowe-pozyczki/', FirstFreeLoan.as_view(), name='first_free_loan'),
    url(r'^firmy/$', Companies.as_view(), name='companies'),
    url(r'^firmy/(?P<page>.+)$', SingleCompany.as_view(), name='single_company'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

