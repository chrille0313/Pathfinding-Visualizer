from pydantic import BaseModel
from PathViz.lib.json_serializeable_mixin import JSONSerializableMixin


class CellColorTheme(BaseModel, JSONSerializableMixin):
    default: str = "#323232"
    wall: str = "#000000"
    visited: str = "#c20f00"
    searching: str = "#69c100"
    path: str = "#258bae"
    start: str = "#258bae"
    end: str = "#258bae"

class ColorTheme(BaseModel, JSONSerializableMixin):
    cells: CellColorTheme = CellColorTheme()
