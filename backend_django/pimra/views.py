from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse

from pimra.forms import DumpForm
from pimra.scripts.pimraNFC import nfc_dump


class IndexTemplateView(TemplateView):



    def get_context_data(self, **kwargs):
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['dumpform'] = DumpForm

        return context
    template_name = 'pimra/index.html'


def dump_nfc(request):

    dumpform = DumpForm(request.POST)
    if dumpform.is_valid():

        nfc_dump(dumpform.cleaned_data['filename'])

    return HttpResponse('Dump made')


