import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import anvil.tables.query as q

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.


@anvil.server.callable
def get_therapists( max_rate: int, city_var: str ) :
  # max_rate: int, city_var: str, spec_var: str
  # Get a list of therapists from the Data Table

  
#   kwargs = {'rate_in_byn': max_rate, 'city': city, 'specialisation': spec}
#   items = app_tables.therapists.search(q.all_of(**kwargs))


  #city
  matching_city = str(app_tables.city.get(name = city_var))
  
  city_view = app_tables.therapists.search(city=matching_city)
  
  #max rate
  
  result_view = app_tables.therapists.search(rate_in_byn = q.less_than_or_equal_to(max_rate), city= city_var)

  return items


