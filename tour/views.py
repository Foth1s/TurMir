from audioop import reverse
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Tour

class HomePageView(ListView):
    model = Tour
    template_name = 'index.html'

class PodborView(CreateView):
    model = Tour
    template_name = 'podbor.html'
    fields = '__all__'

class KontaktView(ListView):
    model = Tour
    template_name = 'kontakt.html'

class OtziviView(ListView):
    model = Tour
    template_name = 'otzivi.html'

class OplataView(ListView):
    model = Tour
    template_name = 'oplata.html'

class LogView(ListView):
    model = Tour
    template_name = 'log.html'

class RegView(ListView):
    model = Tour
    template_name = 'reg.html'

class OaaView(ListView):
    model = Tour
    template_name = 'oaa.html'

class Oaa1View(ListView):
    model = Tour
    template_name = 'oaa1.html'

class Oaa2View(ListView):
    model = Tour
    template_name = 'oaa2.html'

class Oaa3View(ListView):
    model = Tour
    template_name = 'oaa3.html'

class ChernogView(ListView):
    model = Tour
    template_name = 'chernog.html'

class Chernog1View(ListView):
    model = Tour
    template_name = 'chernog1.html'

class Chernog2View(ListView):
    model = Tour
    template_name = 'chernog2.html'

class Chernog3View(ListView):
    model = Tour
    template_name = 'chernog3.html'

class OplatiView(ListView):
    model = Tour
    template_name = 'oplati.html'

class SeulView(ListView):
    model = Tour
    template_name = 'seul.html'

class Seul1View(ListView):
    model = Tour
    template_name = 'seul1.html'

class Seul2View(ListView):
    model = Tour
    template_name = 'seul2.html'

class Seul3View(ListView):
    model = Tour
    template_name = 'seul3.html'

class MaldivView(ListView):
    model = Tour
    template_name = 'maldiv.html'

class Maldiv1View(ListView):
    model = Tour
    template_name = 'maldiv1.html'

class Maldiv2View(ListView):
    model = Tour
    template_name = 'maldiv2.html'

class Maldiv3View(ListView):
    model = Tour
    template_name = 'maldiv3.html'

class ChexView(ListView):
    model = Tour
    template_name = 'chex.html'

class Chex1View(ListView):
    model = Tour
    template_name = 'chex1.html'

class Chex2View(ListView):
    model = Tour
    template_name = 'chex2.html'

class Chex3View(ListView):
    model = Tour
    template_name = 'chex3.html'

class KonecoplatView(ListView):
    model = Tour
    template_name = 'konecoplat.html'

class HomeePageView(ListView):
    model = Tour
    template_name = 'index1.html'

class KontakttView(ListView):
    model = Tour
    template_name = 'kontakt1.html'

class OplataaView(ListView):
    model = Tour
    template_name = 'oplata1.html'

class OtziviiView(ListView):
    model = Tour
    template_name = 'otzivi1.html'