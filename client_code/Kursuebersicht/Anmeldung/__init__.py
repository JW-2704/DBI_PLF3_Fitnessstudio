from ._anvil_designer import AnmeldungTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class Anmeldung(AnmeldungTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    mitglieder = anvil.server.call('mitglieder_anmelden')
    self.repeating_panel_1.items = mitglieder
