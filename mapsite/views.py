from django.views.generic import TemplateView, View
from django.shortcuts import render, render_to_response
from .forms import DataForm


class IndexView(TemplateView):
    template_name = 'mapsite/index.html'


def upload_data(request):
    if request.method == 'POST':
        form = DataForm(request.POST, request.FILES)

        if form.is_valid():
            map_name = request.POST['map_name']
            #print(request.FILES['data'])
            return render_to_response('mapsite/map.html', {'map_name': map_name})
    else:
        form = DataForm()

    return render(request, 'mapsite/upload.html', {'form': form})