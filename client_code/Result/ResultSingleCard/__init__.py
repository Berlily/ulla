from ._anvil_designer import ResultSingleCardTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from .Profile import Profile

class ResultSingleCard(ResultSingleCardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    


  def profile_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.column_panel.clear()
    
    next_form = Profile()
    self.column_panel.add_component(next_form)





  