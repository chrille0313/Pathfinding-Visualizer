from PathViz.App.Model import AppModel
from PathViz.App.View import AppView

from globals import WIDTH, HEIGHT, WIN_WIDTH, WIN_HEIGHT


if __name__ == '__main__':
    model = AppModel((WIDTH, HEIGHT))
    app = AppView(model, (WIN_WIDTH, WIN_HEIGHT))
    model.run()
