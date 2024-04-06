from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
# from kivy.uix.floatlayout import FloatLayout


class NetworkMonitorGUI(App):

    def __init__(self):
        super(NetworkMonitorGUI, self).__init__()
        self.sidebar_hidden = False
        self.side_bar = None

    def build(self):
        main_layout = self.create_main_layout()
        return main_layout

    def create_main_layout(self):
        main_layout = BoxLayout(orientation='vertical')
        main_layout.add_widget(self.create_expand_button())
        main_layout.add_widget(self.create_content_layout())
        main_layout.add_widget(self.create_footer())
        return main_layout

    def create_expand_button(self):
        expand = Button(text='side')
        expand.size_hint_x = 0.2
        expand.size_hint_y = 0.2
        expand.pos_hint = {'x': 0.8, 'y': 0.8}
        expand.bind(on_press=lambda instance: self.expand_collapse(instance, self.side_bar))
        return expand

    def create_content_layout(self):
        content_layout = BoxLayout(orientation='horizontal')
        content_layout.add_widget(self.create_sidebar())
        content_layout.add_widget(self.create_graphs())
        content_layout.size_hint_y = 0.7
        return content_layout

    def create_sidebar(self):
        self.side_bar = BoxLayout(orientation='vertical')
        self.side_bar.add_widget(Button(text='Sites'))
        self.side_bar.add_widget(Button(text='Compare'))
        self.side_bar.add_widget(Button(text='Archive'))
        self.side_bar.size_hint_x = 0.3
        return self.side_bar

    @staticmethod
    def create_graphs():
        graphs = BoxLayout()
        graphs.add_widget(Label(text='Hello world'))
        graphs.size_hint_x = 0.7
        return graphs

    def create_footer(self):
        footer = BoxLayout(orientation='horizontal')
        footer.add_widget(self.create_button('Make Data using Ping', self.make_data))
        footer.add_widget(self.create_button('Convert to CSV File', self.format_data))
        footer.add_widget(self.create_button('Archive CSV Data', self.archive_data))
        footer.size_hint_y = 0.3
        return footer

    @staticmethod
    def create_button(text, callback):
        button = Button(text=text)
        button.bind(on_press=callback)
        return button

    def expand_collapse(self, instance, side_bar):
        if self.sidebar_hidden:
            self.sidebar_hidden = False
            side_bar.size_hint_x = 0
        else:
            self.sidebar_hidden = True
            side_bar.size_hint_x = 0.3

    @staticmethod
    def make_data(instance):
        print("Executing Your command ...")

    @staticmethod
    def format_data(instance):
        print("Makings CSV files.")

    @staticmethod
    def archive_data(instance):
        print("Archiving CSV data")

if __name__ == '__main__':
    NetworkMonitorGUI().run()
