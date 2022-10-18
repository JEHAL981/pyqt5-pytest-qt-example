import time

import pytest

from PyQt5 import QtCore

import desk_app


@pytest.fixture
def app(qtbot):
    app = desk_app.MyApp()
    qtbot.addWidget(app)
    app.show()
    qtbot.waitForWindowShown(app)
    time.sleep(5)
    return app


def test_should_see_hello_world_displayed(app):
    assert app.text_label.text() == "Hello World!"


def test_should_see_goodbye_world_displayed(app, qtbot):
    qtbot.mouseClick(app.button, QtCore.Qt.LeftButton)
    assert app.text_label.text() == "Goodbye World!"
