from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections
from datetime import datetime
from django.shortcuts import redirect

def show_history_temperature(request):
    sql = "SELECT * FROM myapp_temperature_db ORDER BY DATETIME DESC"
    cursor = connections['default'].cursor() #連接資料庫
    cursor.execute(sql,[]) #執行sql語法
    result = cursor.fetchall() #取得資料
    # print(result)

    #轉換格式
    field_name=cursor.description #取得資料表欄位名稱
    # print(field_name)

    resultList=[]
    for data in result:
        # print(data)
        i=0
        dict_data={}
        for d in data:
            # print(d)
            dict_data[field_name[i][0]]=d
            i=i+1
        resultList.append(dict_data)
    print(resultList)
    # return HttpResponse("test...")
    return render(request,"show_history_temperature.html",locals())

def add_temperature(request, mode=None):
    if mode == "edit":
        sensor_id = request.GET["sensor_id"]
        temperature = request.GET["temperature"]
        humidity = request.GET["humidity"]
        s_datetime = request.GET["datetime"]
        #可檢查版本
        sql = "INSERT INTO myapp_temperature_db (sensor_id,temperature,humidity,datetime)"
        sql += "VALUES('%s','%s','%s','%s')"
        sql %= (sensor_id,temperature,humidity,s_datetime)
        # print(sql)
        cursor = connections["default"].cursor()
        cursor.execute(sql,[])
        cursor.close()
        return redirect('/show_history_temperature')
        # return HttpResponse("test...2")
    elif mode == "load":
        # return HttpResponse("test...2")
        return render(request,"add_temperature.html",locals())


# 1. Import the csrf_exempt decorator
from django.views.decorators.csrf import csrf_exempt
# 2. Exempt the view from CSRF checks
@csrf_exempt
def api_add_temperature(request):
    try:
        if request.method == "GET":
            sensor_id = request.GET["sensor_id"]
            temperature = request.GET["temperature"]
            humidity = request.GET["humidity"]
        elif request.method == "POST":
            sensor_id = request.POST["sensor_id"]
            temperature = request.POST["temperature"]
            humidity = request.POST["humidity"]
    except:
        return HttpResponse("add error")
    try:
        s_datetime = datetime.now()
        s_datetime = s_datetime.strftime("%Y/%m/%d %H:%M:%S") #格式化
        print(s_datetime)
        #可檢查版本
        sql = "INSERT INTO myapp_temperature_db (sensor_id,temperature,humidity,datetime)"
        sql += "VALUES('%s','%s','%s','%s')"
        sql %= (sensor_id,temperature,humidity,s_datetime)
        # print(sql)
        cursor = connections["default"].cursor()
        cursor.execute(sql,[])
        cursor.close()
    except:
        return HttpResponse("sql execute error")
    return HttpResponse("added successfully!")

# 時想使某個視圖函數或視圖類不進行CSRF驗證
# https://www.cnblogs.com/meloncodezhang/p/11752602.html


import json
from django.http import JsonResponse
def api_show_temperature(request):
    sql = "SELECT * FROM myapp_temperature_db ORDER BY DATETIME DESC"
    cursor = connections['default'].cursor() #連接資料庫
    cursor.execute(sql,[]) #執行sql語法
    result = cursor.fetchall() #取得資料
    # print(result)

    #轉換格式
    field_name=cursor.description #取得資料表欄位名稱
    # print(field_name)

    resultList=[]
    for data in result:
        # print(data)
        i=0
        dict_data={}
        for d in data:
            # print(d)
            dict_data[field_name[i][0]]=d
            i=i+1
        resultList.append(dict_data)
    print(resultList)   
    return JsonResponse(resultList,  safe=False)



