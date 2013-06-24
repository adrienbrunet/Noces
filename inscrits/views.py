from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from .models import Inscrits
from inscrits.forms import InscritsForm


def NocesRegistration(request):
    if request.method == 'POST':
        form = InscritsForm(request.POST)
        if form.is_valid():
            inscrits = Inscrits(FamilyName=form.cleaned_data['FamilyName'], NbPersonneFamille=form.cleaned_data['NbPersonneFamille'], PresenceNoce=form.cleaned_data['PresenceNoce'], PresenceFeteFamille=form.cleaned_data['PresenceFeteFamille'])
            inscrits.save()
            return HttpResponseRedirect('/inscrits')
        else:
            return render_to_response('register.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = InscritsForm()
        context = {'form': form}
        return render_to_response('register.html', context, context_instance=RequestContext(request))


def Home(request):
    return render(request, 'home.html',)


def Plan(request):
    return render(request, 'plan.html',)


def Nouic(request):
    return render(request, 'nouic.html',)


def InscritsList(request):
    liste1 = Inscrits.objects.filter(PresenceNoce=True)
    liste2 = Inscrits.objects.filter(PresenceFeteFamille=True)
    context = {'liste1': liste1, 'liste2': liste2}
    return render_to_response('inscrits.html', context, context_instance=RequestContext(request))
