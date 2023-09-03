from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import time

#Builder.load_file('testcamera.kv')


class CameraClick(BoxLayout):
    def capture(self):
        camera = self.ids['camera']
        time_str = time.strftime("%Y%m%d_%H%M%S")
        camera.export_to_png(f'IMG_{time_str}.png')
        print("Captured")


class TestCamera(App):
    def build(self):
        return CameraClick()


TestCamera().run()
