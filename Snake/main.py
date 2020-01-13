from kivy.app import App
from kivy.uix.widget import Widget
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.clock import Clock

class GameWidget(Widget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._on_keyboard_closed,self)
        self._keyboard.bind(on_key_down=self._on_key_down)
        #self._keyboard.bind(on_key_up=self._on_key_up)

        with self.canvas:
            self.player = Rectangle(pos=(300,300),size=(30,30))
        
        Clock.schedule.interval(self,0)

    def _on_keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_key_down)
        #self._keyboard.unbind(on_key_up=self._on_key_up)
        self._keyboard = None

    def _on_key_down(self,keyboard,keycode,text,modifiers):
        currentx = self.player.pos[0]
        currenty = self.player.pos[1]

        if text == "w":
            currenty += 1
        if text == "s":
            currenty -=1
        if text == "a":
            currentx -=1
        if text == "d":
            currentx += 1
        
        self.player.pos = (currentx,currenty)


class MyApp(App):
    def build(self):
        return GameWidget()


if __name__ == "__main__":
    app = MyApp()
    app.run()
