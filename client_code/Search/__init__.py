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





class Search(SearchTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # attributes that will result in differrent versions of 'Result' page
    self.selected_city = ""
    self.selected_specialisation = ""
    self.selected_max_rate = 0
    
    # Any code you write here will run when the form opens.
    
    # Create DropDowns
    self.specialisation_drop_down.items = specialisations + ["Затрудняюсь ответить"]
    self.city_drop_down.items = cities
    self.max_rate_dropdown.items = [40, 60, 80, 100, 'не имеет значения']
    
    #manage dropdowns    
  def city_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    self.selected_city = self.city_drop_down.selected_value    

  def specialisation_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    self.selected_specialisation = self.specialisation_drop_down.selected_value

  def drop_down_3_change(self, **event_args):
    """This method is called when an item is selected"""
    self.selected_max_rate = self.max_rate_dropdown.selected_value

   #go to 'Result' page
  def button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # go to 'Result' page
    self.column_panel.clear()
    next_form = Result(self.selected_city,  self.selected_specialisation, self.selected_max_rate)
    self.column_panel.add_component(next_form)  
    




  
  




