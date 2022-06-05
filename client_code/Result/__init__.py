from ._anvil_designer import ResultTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class Result(ResultTemplate):
  def __init__(self, selected_city, selected_specialisation, selected_max_rate, **properties ):
# You must call self.init_components() before doing anything else in this function
    self.init_components(**properties)    
    self.city = selected_city
    self.specialisation = selected_specialisation
    self.max_rate = selected_max_rate
    


    # Any code you write here will run when the form opens.
    self.refresh_therapists()
    
  def refresh_therapists(self):
    # Load existing therapists from the Data Table, and display them in the RepeatingPanel
    self.repeating_panel.items = anvil.server.call('get_therapists', self.city, self.specialisation, self.max_rate)
    