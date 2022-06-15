import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.tables.query as q
from datetime import datetime

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.


@anvil.server.callable
def get_therapists( max_rate: int, city_var: str, spec: str ) :
  """the function is used when using filter search (i.e. essentially taking certain dropdown values)"""
  
  if max_rate == "не имеет значения" and spec!= "Затрудняюсь ответить" :
    result_view = app_tables.therapists.search(city= city_var, specialisation= [spec])
  elif max_rate != "не имеет значения" and spec == "Затрудняюсь ответить" :
    result_view = app_tables.therapists.search(rate_in_byn = q.less_than_or_equal_to(max_rate), city= city_var)
  
  elif max_rate == "не имеет значения" and spec == "Затрудняюсь ответить" :
    result_view = app_tables.therapists.search(city= city_var)
  else:
    result_view = app_tables.therapists.search(rate_in_byn = q.less_than_or_equal_to(max_rate), city= city_var, specialisation = [spec])
  
  return result_view


@anvil.server.callable
def get_therapists_all( ) :
  result_view = app_tables.therapists.search()
  return result_view

@anvil.server.callable
def add_feedback(feedback):
  app_tables.feedback.add_row(
    content=feedback, 
    date_added=datetime.now()
  )
 
