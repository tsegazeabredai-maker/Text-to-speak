from kivy.app import App
from kivy.uix.label import Label

class TextToSpeechApp(App):
    def build(self):
        return Label(text='Text to Speech App')

if __name__ == '__main__':
    TextToSpeechApp().run()
