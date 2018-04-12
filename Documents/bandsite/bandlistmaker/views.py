from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from .models import *
from .forms import *

class TopView(TemplateView):
	template_name = "top.html"
	
	def get(self, request, *args, **kwargs):
		return render(self.request, self.template_name)
		
		
class MemberListView(TemplateView):
	template_name = "member_list.html"
	
	def get(self, request, *args, **kwargs):
		name = "MelodyUnion"
		context = super(MemberListView, self).get_context_data(**kwargs)
		members = Members.objects.all()
		context = {
			'members' : members,
			'name' : name
		}
		return render(self.request, self.template_name, context)
		
class BandMemberListView(TemplateView):
	template_name = "band_member_list.html"
	
	def get(self, request, *args, **kwargs):
		context = super(BandMemberListView, self).get_context_data(**kwargs)
		band=Bands.objects.get(id=self.kwargs['pk'])
		name=band.name
		members = band.members.all()
		context = {
			'members' : members,
			'band':band,
			'name' : name
		}
		return render(self.request, self.template_name, context)


class BandListView(TemplateView):
	template_name = "band_list.html"
	
	def get(self, request, *args, **kwargs):
		context = super(BandListView, self).get_context_data(**kwargs)
		bands = Bands.objects.all()
		context['bands'] = bands

		return render(self.request, self.template_name, context)
		
		
class SeasonListView(TemplateView):
	template_name = "season_list.html"
	
	def get(self, request, *args, **kwargs):
		context = super(SeasonListView, self).get_context_data(**kwargs)
		seasons = Seasons.objects.all()
		context['seasons'] = seasons

		return render(self.request, self.template_name, context)


	
def bands_models(request):
	form  = BandsForm(request.POST or None)
	if form.is_valid():
		Bands.objects.create(**form.cleaned_data)
		return redirect('/register_band/')
 
	context = {
		'form' : form,
		'band_qs': Bands.objects.all().order_by('-id')[0],
	}
	return render(request, 'register_band.html', context)


def edit_bands_models(request,pk):
	band = get_object_or_404(Bands, pk=pk)
	if request.method == 'POST':
		if 'send' in request.POST:
			form  = BandsForm(request.POST or None)
			if form.is_valid():
				band.name = form.cleaned_data['name']
				band.video_url = form.cleaned_data['video_url']
				band.seasons = form.cleaned_data['seasons']
				band.save()
				
		if 'delete' in request.POST:
			band.delete()
		return redirect('band_list')
	else:
	# GETリクエスト（初期表示）時はDBに保存されているデータをFormに結びつける
		form  = BandsForm({'id': band.id,'name':band.name,'video_url':band.video_url,'seasons':band.seasons})
	context = {'form': form,'band':band}
	return render(request, 'edit_band.html', context)
	
def members_models(request):
    form  = MembersForm(request.POST or None)
    if form.is_valid():
        Members.objects.create(**form.cleaned_data)
        return redirect('/register_member/')
 
    context = {
        'form' : form,
        'members_qs': Members.objects.all().order_by('-id')[0],
    }
    return render(request, 'register_member.html', context)
	
def edit_members_models(request,pk):
	member = get_object_or_404(Members, pk=pk)
	if request.method == 'POST':
		if 'send' in request.POST:
			form  = EditMembersForm(request.POST or None)
			if form.is_valid():
				member.name = form.cleaned_data['name']
				member.email = form.cleaned_data['email']
				member.save()
		if 'delete' in request.POST:
			member.delete()
		return redirect('member_list')
	else:
	# GETリクエスト（初期表示）時はDBに保存されているデータをFormに結びつける
		form  = EditMembersForm({'id': member.id,'name':member.name,'email':member.email})
	context = {'form': form,'member':member}
	return render(request, 'edit_member.html', context)

def add_band_member_models(request,pk):
	band = get_object_or_404(Bands, pk=pk)
	members = Members.objects.all()
	form = AddBandMemberForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			picked = form.cleaned_data.get('members')
			for x in picked:
				band.members.add(x)
		return redirect('band_list')
	
	context = {
		'form' : form,
		'members':members,
		'band':band
	}
	return render(request, 'add_band_member.html', context)

def delete_band_member_models(request,pk):
	band = get_object_or_404(Bands, pk=pk)
	members = band.members.all()
	form = AddBandMemberForm(request.POST or None)
	if request.method == 'POST':
		if form.is_valid():
			picked = form.cleaned_data.get('members')
			for x in picked:
				band.members.remove(x)
		return redirect('band_list')
	
	context = {
		'form' : form,
		'members':members,
		'band':band
	}
	return render(request, 'delete_band_member.html', context)
	
def delete_members_models(request,pk):
	member = get_object_or_404(Members, pk=pk)
	def get(self, request, *args, **kwargs):
		member.delete()
		return redirect('member_list')

def seasons_models(request):
	form  = SeasonsForm(request.POST or None)
	if form.is_valid():
		Seasons.objects.create(**form.cleaned_data)
		return redirect('/register_season/')
 
	context = {
		'form' : form,
	}
	return render(request, 'register_season.html', context)
	
def edit_seasons_models(request,pk):
	season = get_object_or_404(Seasons, pk=pk)
	if request.method == 'POST':
		if 'send' in request.POST:
			form  = SeasonsForm(request.POST or None)
			if form.is_valid():
				season.name = form.cleaned_data['name']
				season.year = form.cleaned_data['year']
				season.save()
		if 'delete' in request.POST:
			season.delete()
		return redirect('season_list')
	else:
	# GETリクエスト（初期表示）時はDBに保存されているデータをFormに結びつける
		form  = SeasonsForm({'id': season.id,'name':season.name,'year':season.year})
	context = {'form': form,'season':season}
	return render(request, 'edit_season.html', context)
	
	
	
	
	
	
	
	

