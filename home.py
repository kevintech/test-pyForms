import pyforms
from pyforms.basewidget import BaseWidget
from pyforms.controls import ControlText
from pyforms.controls import ControlButton


class HomeExample(BaseWidget):

    def __init__(self):
        super(HomeExample, self).__init__("My Home Window")

        self._firstName = ControlText("First name", "Kevin")
        self._lastName = ControlText("Last name", "Herrarte")
        self._email = ControlText("E-mail", "mail@example.com")
        self._button = ControlButton("Ok!")

        self.formset = [{
            '1) Personal Information': ['_firstName', '||', '_lastName'],
            '2) Contacts': ['_email']
            },
            '=',
            (' ', '_button', ' ')]


if __name__ == "__main__": pyforms.start_app(HomeExample)
