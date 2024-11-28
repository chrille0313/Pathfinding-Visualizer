from PathViz.App.Model import AppModel
from PathViz.App.View import AppView

from globals import GRID_SIZE, WIN_SIZE


if __name__ == '__main__':
    app = AppModel(GRID_SIZE)
    app_view = AppView(WIN_SIZE)
    app_view.view_model(app)

    app.run()
