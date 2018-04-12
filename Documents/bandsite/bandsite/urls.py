"""bandsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

import bandlistmaker.views as bandlistmaker_view

urlpatterns = [
	path('admin/', admin.site.urls),
	path('register_member/', bandlistmaker_view.members_models, name="members_models"),
	path('register_band/', bandlistmaker_view.bands_models, name="bands_models"),
	path('register_season/', bandlistmaker_view.seasons_models, name="seasons_models"),
	path('member_list/', bandlistmaker_view.MemberListView.as_view(),name="member_list"),
	path('band_list/', bandlistmaker_view.BandListView.as_view(),name="band_list"),
	path('season_list/', bandlistmaker_view.SeasonListView.as_view(),name="season_list"),
	path('band_member_list/<int:pk>/', bandlistmaker_view.BandMemberListView.as_view(),name="band_member"),
	path('edit_member/update/<int:pk>/', bandlistmaker_view.edit_members_models, name="edit_member"),
	path('edit_band/update/<int:pk>/', bandlistmaker_view.edit_bands_models, name="edit_band"),
	path('edit_season/update/<int:pk>/', bandlistmaker_view.edit_seasons_models, name="edit_season"),
	path('add_band_member/<int:pk>/', bandlistmaker_view.add_band_member_models, name="add_band_member"),
	path('delete_band_member/<int:pk>/', bandlistmaker_view.delete_band_member_models, name="delete_band_member"),
	path('', bandlistmaker_view.TopView.as_view()),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]