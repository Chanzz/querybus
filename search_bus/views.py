from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import query
from .form import SearchForm
# from .models import BusNOHistory
import re


# Create your views here.
def search(request):
    q_form = SearchForm(data=request.POST)
    if q_form.is_valid():
        q = q_form.cleaned_data['busno']
        # q = request.POST.get('busno')
        if re.match('\d', q):  # 判断q是否为纯数字的字符串，以后再改
            # BusNOHistory.objects.create(BusNO=q)
            request.session['BuoNO'] = q  # 把用户请求的数据记录在session，以供换向使用
            request.session['direction'] = 0
            res = query.get_url(str(q), '0')  # 默认方向为0
            sn = query.get_sn(res)
            bus = query.get_bus(res)
            n_list = []  # 根据车站数，生成一个1,2,3......[车站数]的字符串数组
            for a in range(len(sn)):
                n_list.append(str(a))
            context = {
                'sn': sn,
                'bus': bus,
                'n_list': n_list,
            }
            return render(request, 'search_bus/index.html', context)
        else:
            return HttpResponse('ERROR')
    else:
        return HttpResponse('ERROR')


def welcome(request):
    return render(request, 'search_bus/index.html')


def reverse(request):
    q = request.session.get('BuoNO')
    direct = request.session.get('direction')
    if direct == 0:  # 换向
        direct = 1
    else:
        direct = 0
    request.session['direction'] = direct  # 修改当前方向
    res = query.get_url(str(q), str(direct))
    sn = query.get_sn(res)
    bus = query.get_bus(res)
    n_list = []
    for a in range(len(sn)):
        n_list.append(str(a))
    context = {
        'sn': sn,
        'bus': bus,
        'n_list': n_list,
    }
    return render(request, 'search_bus/index.html', context)
