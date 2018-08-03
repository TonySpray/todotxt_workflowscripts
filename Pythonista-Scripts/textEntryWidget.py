#! /usr/bin/env python


import ui
import time, datetime


def timeStamp():
    return datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')


def clearTodoField(sender):
    '@type sender: ui.Button'
    todoEntry.text = ""


def sendTodoField(sender):
    '@type sender: ui.Button'
    todo_text = todoEntry.text
    todo_payload = "({0}) {1}".format(todo_text[:1], todo_text[1:]).replace(' ', '%20')
    import webbrowser
    webbrowser.open("swiftodo://x-callback-url/add?x-source=Pythonista&x-success=x-pythonista://&tasks={0}".format(todo_payload))


def sendToDevonThink(sender):
    '@type sender: ui.Button'
    todo_text = todoEntry.text .replace(' ', '%20')
    title = 'Note: {0}'.format(timeStamp()).replace(' ', '%20')
    import webbrowser
    webbrowser.open('x-devonthink://clip?title={0}&text={1}'.format(title, todo_text))
    

def sendToLyricPool(sender):
    '@type sender: ui.Button'
    todo_text = todoEntry.text.replace(' ', '%20')
    title = 'UUID-of-note-to-append-to'
    import webbrowser
    webbrowser.open('x-devonthink://append?uuid={0}&text={1}'.format(title, todo_text))


def openSimpleNote(sender):
    '@type sender: ui.Button'
    import webbrowser
    webbrowser.open('simplenote://')


v = ui.load_view()
todoEntry = v['todoEntry']

def run():
    v.present('sheet')


