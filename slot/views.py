from django.shortcuts import render
from .models import SlotInformation, SlotGameData
from datetime import datetime, date, timedelta
from dateutil.relativedelta import relativedelta

# Create your views here.

# トップページ　機種一覧
def index(request):
  # slot_lists = SlotInformation.objects.all()

  slot_list = [] 
  # for slot in slot_lists:
  #   slot_list.append(slot)

  params = {
    'slot_list' : slot_list,
  }
  print(params)
  return render(request, 'slot/index.html', params)

# 機種データ一覧
def show_data(request, slot_id):

  # 1ヶ月前の日付取得
  today = datetime.today()
  one_month_ago = datetime.strftime(today - relativedelta(months=1), '%Y-%m-%d')
  
  # 機種名取得
  slot_name = SlotInformation.objects.get(pk=slot_id).slot_name
  # slot_name = SlotInformation.objects.select_related('slot_name').get(pk=slot_id)

  # 機種に紐づく台番号一覧を取得
  number_list = SlotGameData.objects.filter(slot_id=slot_id,date_time__gte=one_month_ago).order_by('number').distinct().values_list('number', flat=True)

  #日付一覧を取得 
  dates = SlotGameData.objects.filter(slot_id=slot_id,date_time__gte=one_month_ago).order_by('-date_time').distinct().values_list('date_time', flat=True)
  # dates = SlotGameData.objects.select_related().filter(slot_id=slot_id,date_time__gte=one_month_ago).order_by('date_time').distinct().values_list('date_time', flat=True)
  date_list = []
  for date in dates:
    date_list.append(str(date))

  #機種データ取得
  slot_data_list = SlotGameData.objects.filter(slot_id=slot_id,date_time__gte=one_month_ago).order_by('date_time').values()

  params = {
    'slot_name':slot_name,
    'number_list':number_list,
    'date_list':date_list,
    'slot_data_list':slot_data_list,
  }
  return render(request, 'slot/data_show.html',params)

