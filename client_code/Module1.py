import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class Visitor(app_tables.visitors.Row, client_deletable=True):
    pass
