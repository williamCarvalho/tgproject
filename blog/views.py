# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Post

from .models import Consulta
from .forms import PostForm
import pandas as pd
import numpy as np
import string
from django.template import RequestContext

# from django.http import HttpResponse
# from django.http import HttpResponseRedirect

# Create your views here.

def simple(request):
    import random
    import django
    import datetime

    from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
    from matplotlib.figure import Figure
    from matplotlib.dates import DateFormatter

    fig=Figure()
    ax=fig.add_subplot(111)
    x=[]
    y=[]
    now=datetime.datetime.now()
    delta=datetime.timedelta(days=1)
    for i in range(10):
        x.append(now)
        now+=delta
        y.append(random.randint(0, 1000))
    ax.plot_date(x, y, '-')
    ax.xaxis.set_major_formatter(DateFormatter('%Y-%m-%d'))
    fig.autofmt_xdate()
    canvas=FigureCanvas(fig)
    response=django.http.HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response

def grafico():
    fixed_df = pd.read_csv('comptagevelo20162.csv', sep=',', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date') 
    return fixed_df['Berri1'].plot()

def obtem_dados():
    from lxml import etree
    import requests
    import json
    import urllib

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    fields = {'id':'32539','form_id':'902634','dia_inicial':'01','mes_inicial':'08','ano_inicial':'2017','dia_final':'31','mes_final':'08','ano_final':'2017'}

    r = requests.post('http://sinda.crn2.inpe.br/PCD/SITE/novo/site/historico/action.php', fields)

    html = etree.HTML(r.text)

    tr_nodes = html.xpath('//table/tr')

    tr_nodes_titulo = html.xpath('//table/tr/td/b')

    tr_header = html.xpath('//table/caption/center/font')

    header = [te.text for te in tr_header[0:]]

    tr_titulo = [to.text for to in tr_nodes_titulo[0:]]

    th_content = [i[0].text for i in tr_nodes[0].xpath("th")]

    td_content = [[td.text for td in tr.xpath('td')] for tr in tr_nodes[1:]]

    header = header[0].split(',')

    print ("HEADER:")
    print(header)

    print ("\nTITULO:")
    print(tr_titulo)

    print ("\nDADOS:")
    td_content
    
    s = pd.Series(td_content)
    return s

def dados(estado, datIni, datFim):
    from lxml import etree
    import requests
    import json
    import urllib

    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt
    
    # variaveis controle
    form_id = '902634'
    uf = estado
    dataIni = string.split(str(datIni), "-")
    dia_inicial = dataIni[2]
    mes_inicial = dataIni[1]
    ano_inicial = dataIni[0]
    dataFim = string.split(str(datFim), "-")
    dia_final = dataFim[2]
    mes_final = dataFim[1]
    ano_final = dataFim[0]
    
    fields = {'id':uf,'form_id':form_id,'dia_inicial':dia_inicial,'mes_inicial':mes_inicial,'ano_inicial':ano_inicial,'dia_final':dia_final,'mes_final':mes_final,'ano_final':ano_final}
    
    r = requests.post('http://sinda.crn2.inpe.br/PCD/SITE/novo/site/historico/action.php', fields)
    
    html = etree.HTML(r.text)
    tr_nodes = html.xpath('//table/tr')
    tr_nodes_titulo = html.xpath('//table/tr/td/b')
    tr_header = html.xpath('//table/caption/center/font')

    header = [te.text for te in tr_header[0:]]

    tr_titulo = [to.text for to in tr_nodes_titulo[0:]]
    # th_content = [i[0].text for i in tr_nodes[0].xpath("th")]
    td_content = [[td.text for td in tr.xpath('td')] for tr in tr_nodes[1:]]
    # header = header[0].split(',')

    return tr_titulo, td_content,
    
def consulta(request):
    form = PostForm()
    return render(request, 'blog/consulta.html', {'form': form})

def resultado(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            # post = form.save(commit=False)
            estado = form.cleaned_data['estado']
            dataIni = form.cleaned_data['data_inicio']
            dataFim = form.cleaned_data['data_fim']
            # dados(estado,dataIni,dataFim)
            # g = grafico()
            res = dados(estado,dataIni,dataFim)
            # res = obtem_dados()
            # res[1] = grafico
            return render(request, 'blog/resultado.html', {'header': res[0], 'dados': res[1], 'w': "TESTE"},  RequestContext(request))
    else:
        return render(request, 'blog/resultado.html')

# Create your views here.

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})