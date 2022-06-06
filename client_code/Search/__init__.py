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
    # numbers are strings here, because in anvil " dropdown 'items' must be a list of strings or tuples"
    self.max_rate_dropdown.items = ['40', '60', '80', '100', 'не имеет значения']
    
    #save tha state of variable when a dropdown item is selected
    self.selected_city = self.city_drop_down_change()
    self.selected_specialisation = self.specialisation_drop_down_change()
    self.selected_max_rate = self.max_rate_dropdown_change()
    
    #dropdown functions   
  def city_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    self.selected_city = self.city_drop_down.selected_value
    print (self.selected_city)
    print (type(self.selected_city))
    return self.selected_city

  def specialisation_drop_down_change(self, **event_args):
    """This method is called when an item is selected"""
    self.selected_specialisation = self.specialisation_drop_down.selected_value
    return self.selected_specialisation
    

  def max_rate_dropdown_change(self, **event_args):
    """This method is called when an item is selected"""
    # converting string to int
    if self.max_rate_dropdown.selected_value != 'не имеет значения':
      self.selected_max_rate = int (self.max_rate_dropdown.selected_value)
      print (self.selected_max_rate)
      print (type(self.selected_max_rate))
    else:
      self.selected_max_rate = self.max_rate_dropdown.selected_value
      print (self.selected_max_rate)
      print (type(self.selected_max_rate))
    
    return self.selected_max_rate

   #go to 'Result' page
  def button_click(self, **event_args):
    """This method is called when the button is clicked"""
    # go to 'Result' page
    self.column_panel.clear()
    
    next_form = Result(self.selected_max_rate, self.selected_city,  self.selected_specialisation)
    self.column_panel.add_component(next_form)  
    





  
  




