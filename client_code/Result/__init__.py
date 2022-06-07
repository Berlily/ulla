from ._anvil_designer import ResultTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables




class Result(ResultTemplate):
  def __init__(self, selected_max_rate, selected_city:str, selected_specialisation:str, **properties ):
# You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)
    self.max_rate = selected_max_rate
    self.city = selected_city
    self.specialisation = selected_specialisation
    
  

    # Any code you write here will run when the form opens.
    self.refresh_therapists()
    
  def refresh_therapists(self):
    # Load existing therapists from the Data Table, and display them in the RepeatingPanel
    print(self.repeating_panel.items)
    print (type(self.repeating_panel.items))
    self.repeating_panel.items = anvil.server.call('get_therapists', self.max_rate, self.city, self.specialisation )
    print(self.repeating_panel.items)
    print (type(self.repeating_panel.items))
#     if self.repeating_panel.items == None:
#       return anvil.alert('По вашему запросу ничего не найдено:(')
#     else:
#       return self.repeating_panel.items

    if self.repeating_panel.items == []:
      return anvil.alert('По вашему запросу ничего не найдено:(')
    else:
      return self.repeating_panel.items
    