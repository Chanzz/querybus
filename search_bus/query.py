import requests
import json


def get_url(busno, direction):  # 利用接口获取数据，并初步清洗数据
    headers = {
        'charset': 'utf-8',
        'Accept-Encoding': 'gzip',
        'referer': 'https://servicewechat.com/wx71d589ea01ce3321/148/page-frame.html',
        'content-type': 'text',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; M5s Build/MRA58K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.147 Mobile Safari/537.36 MicroMessenger/6.7.3.1360(0x2607033D) NetType/WIFI Language/zh_CN Process/appbrand2',
        'Host': 'web.chelaile.net.cn',
    }
    url = 'https://web.chelaile.net.cn/api/bus/line!lineDetail.action?s=h5&wxs=wx_app&src=weixinapp_cx&sign=1&v=3.7.57&from=NO_FROM&cityId=040&geo_lat=23.045717&lat=23.045717&geo_lng=113.382364&lng=113.382364&gpstype=wgs&userId=okBHq0FO9z87DpBXE05Vy9ux8g-g&h5Id=okBHq0FO9z87DpBXE05Vy9ux8g-g&targetOrder=14&lineId=020-0' + busno + '0-' + direction + '&lineName=' + busno + "'"
    r = requests.get(url, headers=headers)
    html = r.text
    jsondata = html[15:]
    jsondata1 = jsondata[:-7]
    test = json.loads(jsondata1)
    return test


def get_sn(r):  # 接收get_url()返回的数据，并返回车站列表
    station_list = []
    sno = r["data"]["line"]["stationsNum"]
    for a in range(sno):
        station_list.append(r["data"]["stations"][a]["sn"])
    return station_list


'''首先获取每个车辆的位置，并用后一个位置减去前一个位置，方便回调后渲染模板'''


def get_bus(r):  # 接收get_url()返回的数据，并返回公交车的位置
    bus_list = [0]
    s_list = []
    for a in range(10):
        try:
            bus_list.append(int(r["data"]["buses"][a]["order"]))
        except:
            pass
    for s in range(len(bus_list) - 1):
        if bus_list[s + 1] != bus_list[s]:  # 如果两辆车的位置相同，只留一个位置
            s_list.append(str(bus_list[s + 1] - bus_list[s] - 1))
    return s_list
