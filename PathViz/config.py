from pydantic import BaseModel
from PathViz.colors import ColorTheme
from PathViz.lib import JSONSerializableMixin
from PathViz.lib import SerializableVector2 as Vector2


class PathVizConfig(JSONSerializableMixin, BaseModel):
    window_size: Vector2
    grid_size: Vector2
    fps: int
    theme: ColorTheme()