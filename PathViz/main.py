from PathViz.Views import AppView
from PathViz.Models import AppModel

from globals import WIDTH, HEIGHT, WIN_WIDTH, WIN_HEIGHT


if __name__ == '__main__':
    model = AppModel((WIDTH, HEIGHT))
    app = AppView(model, (WIN_WIDTH, WIN_HEIGHT))
    model.run()
