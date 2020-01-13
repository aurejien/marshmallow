from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)



        with self.canvas:
            Rectangle(pos=(300,300),size=(60,30))

class MyApp(App):
    def build(self):
        return game


if __name__ == "__main__":
    app = MyApp()
    app.run()
