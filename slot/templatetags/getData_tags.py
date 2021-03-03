from django import template

register = template.Library() # Djangoのテンプレートタグライブラリ

# カスタムタグとして登録する
@register.simple_tag
def getData(column_name, date, number, slot_data_list):
  '''
  arg1:取得するカラム名
  arg2:日付
  arg3:台番号
  return：日付・台番号に一致するデータの指定したカラム名のデータを返す
  '''
  return_value = ""
  for slot_data in slot_data_list:
    if slot_data.get('number') == number and str(slot_data.get('date_time')) == date:
      return_value = slot_data.get(column_name)

  return return_value




