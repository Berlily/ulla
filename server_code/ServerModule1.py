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
def get_therapists( city="", spec="", max_rate=0 ):
  # Get a list of therapists from the Data Table
  city_col = city
  specialisation_col = spec
  max_rate_col = max_rate
  items = app_tables.therapists.search(rate_in_byn = q.less_than_or_equal_to(max_rate_col), city= city_col, specialisation= specialisation_col)
  return items


