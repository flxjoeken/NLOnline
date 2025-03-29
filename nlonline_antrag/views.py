import os.path

from django.conf import settings
from django.http import HttpResponse, Http404, FileResponse
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.clickjacking import xframe_options_sameorigin
from django.views.generic import DetailView, ListView

from nlonline_antrag.forms import RegisterForm, NLForm
from nlonline_antrag.models import NLOnlineAntrag


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('ok')
        else:
            return render(request, 'nlonline_antrag/register.html', {'form': form})
    form = RegisterForm()
    return render(request, 'nlonline_antrag/register.html', {'form': form})


def new_application(request):
    if (request.method == 'POST'):
        form = NLForm(request.POST, request.FILES)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponse("Danke für Ihre Anfrage. Wir werden uns in Kürze bei Ihnen melden.")
        else:
            print(form.errors)
            return render(request, 'new_application.html', {"form": form})
    else:
        form = NLForm()
        return render(request, 'new_application.html', {"form": form})


class AntragDetailView(DetailView):
    model = NLOnlineAntrag

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class AntragListView(ListView):
    model = NLOnlineAntrag

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


@xframe_options_sameorigin
def mediaView(request, path=''):
    if not request.user.is_authenticated:
        raise Http404()

    file_path = os.path.join(settings.MEDIA_ROOT, path)

    if not os.path.exists(file_path):
        raise Http404("File not found.")

    return FileResponse(open(file_path, 'rb'))
