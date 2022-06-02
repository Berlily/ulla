from ._anvil_designer import BaseTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Start import Start

class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.column_panel.add_component(Start())
  

    # Any code you write here will run when the form opens.
    
  def show_logout_button(self, **properties):
    if anvil.users.get_user(allow_remembered=True) is not None:
      logout_link = Link()
      self.navbar_links.add_component(logout_link)
      
      
    




 



