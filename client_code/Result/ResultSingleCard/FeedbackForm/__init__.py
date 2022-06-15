from ._anvil_designer import FeedbackFormTemplate
from anvil import *
import anvil.server
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class FeedbackForm(FeedbackFormTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
    

  def submit_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    #name = self.name_box.text
    feedback = self.feedback_box.text
    anvil.server.call('add_feedback', feedback)
    Notification("Отзав отправлен! Спасибо!").show()
    self.clear_inputs()

       
  def clear_inputs(self):
    #self.name_box.text = ""
    self.feedback_box.text = ""
