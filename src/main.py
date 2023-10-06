from kivy.app import App
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty

from . import service


class MainApp(App):
    pass


class CustomBoxLayout(BoxLayout):
    username = ObjectProperty(None)
    password = ObjectProperty(None)
    token = ObjectProperty(None)

    def on_submit(self):
        uname = self.username.text
        pwd = self.password.text
        # Call our external api to authenticate the uer.
        res: dict = service.login_user(uname, pwd)

        if res["message"] == "success":
            # do something to show a successful request
            self.token.text = res["token"]
        else:
            # do something to show a failed request
            self.token.text = res["error"]


if __name__ == "__main__":
    Window.size = (300, 500)
    MainApp().run()
