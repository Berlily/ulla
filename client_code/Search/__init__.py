from ._anvil_designer import SearchTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Result import Result

cities = [
  (city['name'], city) for city in app_tables.city.search()
]

specialisations = [
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
    
    # Create DropDowns
    self.specialisation_drop_down.items = specialisations + ["Затрудняюсь ответить"]
    self.city_drop_down.items = cities

  def city_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    if self.city_drop_down.selected_value == "Минск":
      /////
      

  def button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # go to Re
    self.column_panel.clear()
    self.column_panel.add_component(Result())

  
  




