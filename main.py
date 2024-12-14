from PathViz.config import PathVizConfig
from PathViz.App.Model import AppModel
from PathViz.App.View import AppView


if __name__ == '__main__':
    config = PathVizConfig.load_config('config.json')

    app = AppModel(config.grid_size, config.fps)
    app_view = AppView(config.window_size, config.theme)
    app_view.view_model(app)

    app.run()
