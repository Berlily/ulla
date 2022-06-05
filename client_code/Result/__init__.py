from ._anvil_designer import ResultTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables



class Result(ResultTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    self.refresh_therapists()
    
  def refresh_therapists(self):
    # Load existing therapists from the Data Table, and display them in the RepeatingPanel
    self.repeating_panel.items = anvil.server.call('get_therapists', self.city, self.specialisation, self.max_rate)
    