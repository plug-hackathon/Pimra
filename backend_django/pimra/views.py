from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import HttpResponse


import os
from os import listdir
from os.path import isfile, join

from pimra.forms import DumpForm, WriteForm
from pimra.scripts import pimraNFC


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))+'/dumps/full/')

class IndexTemplateView(TemplateView):

    def getWriteForms(self):
        writeforms = [f for f in listdir(BASE_DIR) if isfile(join(BASE_DIR, f))]
        print(writeforms)
        return_forms = []
        for file in writeforms:
            form = WriteForm()
            form.fields['filename'].initial = file
            return_forms.append(form)

        return return_forms

    def get_context_data(self, **kwargs):

        context = super(IndexTemplateView, self).get_context_data(**kwargs)
        context['dumpform'] = DumpForm
        context['writeform'] = self.getWriteForms()

        return context

    template_name = 'pimra/index.html'


def view_dump_nfc(request):

    dumpform = DumpForm(request.POST)
    if dumpform.is_valid():
        print(dumpform.cleaned_data['filename'])
        dump_path = BASE_DIR + "/full/"
        pimraNFC.nfc_dump(dump_path, dumpform.cleaned_data['filename'])

    return HttpResponse('Running: view_dump_nfc')


def view_dump_mfoc(request):

    dumpform = DumpForm(request.POST)
    if dumpform.is_valid():
        dump_path = BASE_DIR + "/mfoc/"
        pimraNFC.mfoc_dump(dump_path, dumpform.cleaned_data['filename'])

    return HttpResponse('Running: view_dump_mfoc')


def view_nfc_poll(request):

    dumpform = DumpForm(request.POST)
    if dumpform.is_valid():
        dump_path = BASE_DIR + "/poll/"
        pimraNFC.nfc_poll(dump_path, dumpform.cleaned_data['filename'])

    return HttpResponse('Running: view_nfc_poll')


def view_nfc_write(request):

    writeform = WriteForm(request.POST)
    if writeform.is_valid():
        print("Form is valid")
        dump_path = BASE_DIR
        print('basedir: '+BASE_DIR)
        
        print(dump_path+'/'+writeform.cleaned_data['filename'])
        pimraNFC.nfc_write(dump_path+'/'+writeform.cleaned_data['filename'])

    else:
        print('form not valid')
    return HttpResponse('Add card to reader.')

