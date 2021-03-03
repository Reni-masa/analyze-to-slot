from django.db import models

class SlotGameData(models.Model):
  number = models.IntegerField(blank=True, null=True)
  bb = models.IntegerField(db_column='BB', blank=True, null=True)  # Field name made lowercase.
  rb = models.IntegerField(db_column='RB', blank=True, null=True)  # Field name made lowercase.
  bb_average = models.CharField(db_column='BB_average', max_length=10, blank=True, null=True)  # Field name made lowercase.
  rb_average = models.CharField(db_column='RB_average', max_length=10, blank=True, null=True)  # Field name made lowercase.
  total_game = models.IntegerField(blank=True, null=True)
  bonus_average = models.CharField(max_length=10, blank=True, null=True)
  class_field = models.IntegerField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
  date_time = models.DateField(blank=True, null=True)
  user_id = models.IntegerField(blank=True, null=True)
  store_id = models.IntegerField()
  slot_id = models.IntegerField()

  class Meta:
    managed = False
    db_table = 'slot_game_data'


class SlotInformation(models.Model):
  slot_name = models.CharField(max_length=30, blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'slot_information'


class StoreInformation(models.Model):
  store_name = models.CharField(max_length=30, blank=True, null=True)
  event_day = models.CharField(max_length=15, blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'store_information'


class StoreSlot(models.Model):
  store_id = models.IntegerField(blank=True, null=True)
  slot_id = models.IntegerField(blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'store_slot'


class User(models.Model):
  user_name = models.CharField(max_length=10, blank=True, null=True)
  password = models.CharField(max_length=30, blank=True, null=True)
  valid_flag = models.IntegerField(blank=True, null=True)
  email = models.CharField(max_length=30, blank=True, null=True)

  class Meta:
    managed = False
    db_table = 'user'
