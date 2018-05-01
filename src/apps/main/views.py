import hashlib
import os
import shutil
import subprocess

from django.views import generic
from django.template.response import TemplateResponse

from src.apps.main.forms import BinaryViewForm


class HomepageView(generic.FormView):
    template_name = 'main/homepage.html'
    form_class = BinaryViewForm

    def form_valid(self, form):
        COMMANDS = [
            ('Readelf: file header', 'file-header'),
            ('Readelf: program headers', 'program-headers'),
            ('LDD', 'ldd'),
            ('Sha512', 'sha512'),
        ]

        input_data = self.request.FILES['binary'].read()
        temporary_binary_path = os.path.join('/tmp/', hashlib.sha256(('makrela-' + form.cleaned_data['binary'].name).encode('utf-8')).hexdigest())

        with open(temporary_binary_path, 'wb') as f:
            f.write(input_data)

        analysis_results = []
        
        for header, command_name in COMMANDS:
            analysis_results.append((
                header,
                subprocess.check_output([
                    os.path.join(os.path.dirname(__file__), '..', '..', 'analyze.sh'),
                    command_name,
                    temporary_binary_path,
                ])
            ))

        return TemplateResponse(
            self.request,
            'main/homepage.html',
            {'analysis_results': analysis_results}
        )
