from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from inscrits.models import Inscrits
from inscrits.forms import InscritsForm
from inscrits.models import Transport
from inscrits.forms import TransportForm


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


def Cadeau(request):
    return render(request, 'cadeau.html',)


def Plan(request):
    return render(request, 'plan.html',)


def Nouic(request):
    return render(request, 'nouic.html',)


def InscritsList(request):
    liste1 = Inscrits.objects.filter(PresenceNoce=True)
    liste2 = Inscrits.objects.filter(PresenceFeteFamille=True)
    context = {'liste1': liste1, 'liste2': liste2}
    return render_to_response('inscrits.html', context, context_instance=RequestContext(request))


def AskTransport(request):
    if request.method == 'POST':
        form = TransportForm(request.POST)
        if form.is_valid():
            transport = Transport(Nom=form.cleaned_data['Nom'], Nombre=form.cleaned_data['Nombre'], Ville=form.cleaned_data['Ville'], Date=form.cleaned_data['Date'],Contact=form.cleaned_data['Contact'], Remarque=form.cleaned_data['Remarque'])
            transport.save()
            return HttpResponseRedirect('/transport')
        else:
            return render_to_response('asktransport.html', {'form': form}, context_instance=RequestContext(request))
    else:
        form = TransportForm()
        context = {'form': form}
        return render_to_response('asktransport.html', context, context_instance=RequestContext(request))


def ChoixTransport(request):
    return render(request, 'choixtransport.html',)


def TransportListe(request):
    liste = Transport.objects.all()
    context = {'liste': liste}
    return render_to_response('transport.html', context, context_instance=RequestContext(request))
