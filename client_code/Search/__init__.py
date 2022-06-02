from ._anvil_designer import SearchTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

cities = [
  (spec['name'], spec) for spec in app_tables.specialisation.search()
]

specialisations= [
  (spec['name'], spec) for spec in app_tables.specialisation.search()
]

rate =[
  (spec['name'], spec) for spec in app_tables.specialisation.search()
]



class Search(SearchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.specialisation_drop_down.items = specialisations
    



