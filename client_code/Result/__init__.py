from ._anvil_designer import ResultTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class Result(ResultTemplate):
  def __init__(self, selected_max_rate =0, selected_city:str =0, selected_specialisation:str =0, **properties ):
# You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)
    self.max_rate = selected_max_rate
    self.city = selected_city
    self.specialisation = selected_specialisation
    
    
      
    # Any code you write here will run when the form opens.
    self.refresh_therapists()
    
  def refresh_therapists(self):
    # Load existing therapists from the Data Table, and display them in the RepeatingPanel
    
    if self.city == 0:
      """we use this condition as a naive way to indicate that no values(i.e selected_max_rate, selected_city and selected_specialisation) were passed to __init__ method
         and thus the code right below is designed to work if the link 'Показать ВСЕХ специалистов' on page 'Search' was clicked"""
      self.repeating_panel.items =  anvil.server.call('get_therapists_all')
    else:
      """if instead filters were used """
      self.repeating_panel.items = anvil.server.call('get_therapists', self.max_rate, self.city, self.specialisation )
    
    
    