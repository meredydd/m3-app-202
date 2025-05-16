from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
from m3 import components
from anvil.js import window

class Form1(Form1Template):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        if confirm('Extra button?'):
            btn = components.Button(text="Hello there")
            self.add_component(btn)
            btn.add_event_handler('click', lambda **e: print("foo"))

    def button_1_click(self, **event_args):
        """This method is called when the component is clicked."""
        self.message_txt.text = f"Hello, {self.name_box.text}!"
        #anvil.server.call('say_hello', self.name_box.text)
        window.alert("Hello, " + self.name_box.text)