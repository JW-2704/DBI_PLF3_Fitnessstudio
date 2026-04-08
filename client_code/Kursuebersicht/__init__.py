from ._anvil_designer import KursuebersichtTemplate
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

class Kursuebersicht(KursuebersichtTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    kurs_daten = anvil.server.call('get_kurs_info')
    self.repeating_panel_1.items = kurs_daten
