from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse

import os
from os import listdir
from os.path import isfile, join

from pimra.forms import DumpForm, WriteForm
from pimra.scripts import pimraNFC


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


class IndexTemplateView(TemplateView):

    def get_context_data(self, **kwargs):

        onlyfiles = [f for f in listdir(BASE_DIR) if isfile(join(BASE_DIR, f))]
        print(onlyfiles)
        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['dumpform'] = DumpForm
        context['onlyfiles'] = onlyfiles

        return context

    template_name = 'pimra/index.html'


def view_dump_nfc(request):

    dumpform = DumpForm(request.POST)
    if dumpform.is_valid():

        pimraNFC.nfc_dump(dumpform.cleaned_data['filename'])

    return HttpResponse('Running: view_dump_nfc')


def view_dump_mfoc(request):

    dumpform = DumpForm(request.POST)
    if dumpform.is_valid():

        pimraNFC.mfoc_dump(dumpform.cleaned_data['filename'])

    return HttpResponse('Running: view_dump_mfoc')


def view_nfc_poll(request):

    dumpform = DumpForm(request.POST)
    if dumpform.is_valid():

        pimraNFC.nfc_poll(dumpform.cleaned_data['filename'])

    return HttpResponse('Running: view_nfc_poll')


