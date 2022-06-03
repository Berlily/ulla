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
    
    # Any code you write here will run when the form opens.
    
    # First off, the login form pops up
    # clean the previous sesssion's user
    self.current_user = anvil.users.get_user(allow_remembered=False)
    if self.current_user is not None:
      anvil.users.logout()
    # pop the login/sign_up form  
    anvil.users.login_with_form(remember_by_default=False, allow_remembered=False)
      
    # Second, the Start page loads
    self.column_panel.add_component(Start())
    
    
  def show_logout_button(self, **properties):
    if anvil.users.get_user(allow_remembered=True) is not None:
      logout_link = Link()
      self.navbar_links.add_component(logout_link)
      
      
    

  def logout_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    anvil.users.logout()
    # pop the login/sign_up form  
    anvil.users.login_with_form(remember_by_default=False, allow_remembered=False)

  def start_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.column_panel.clear()
    self.column_panel.add_component(Start())
    






 



