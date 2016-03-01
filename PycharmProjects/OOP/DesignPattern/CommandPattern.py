class Command(object):
    def execute(self):
        pass
    def undo(self):
        pass
# #=================Device Command====================#
# class LightOnCommand(Command):
#     def __init__(self, light):
#         self.light = light
#     def execute(self):
#         self.light.on()
#
# class GarageDoorOpenCommand(Command):
#     def __init__(self, door):
#         self.door = door
#     def execute(self):
#         self.door.up()
#
# #=====================Remote Controller===================#
# class RemoteControl(object):
#     def setCommand(self, command):
#         self.slot1 = command
#     def buttonWasPressed(self):
#         self.slot1.execute()
#
# #==============Devices============================#
# class Light(object):
#     def on(self):
#         print("light is on")
#     def off(self):
#         print("light is off")
#
# class GarageDoor(object):
#     def up(self):
#         print("the door up")
#     def down(self):
#         print("the door down")
#     def stop(self):
#         print("the door stop")
#     def lightOn(self):
#         print("the door light on")
#     def lightOff(self):
#         print("the door light off")
# #==============Devices============================#
#
#
#
# #=======================Client====================#
# def main():
#     remote = RemoteControl()
#     light = Light()
#     door = GarageDoor()
#     lightOn = LightOnCommand(light)
#     doorUp = GarageDoorOpenCommand(door)
#     remote.setCommand(lightOn)
#     remote.buttonWasPressed()
#     remote.setCommand(doorUp)
#     remote.buttonWasPressed()
# if __name__ == '__main__':
#     main()

#==============Devices============================#
# class Light(object):
#     def __init__(self, type):
#         self.light = type
#     def on(self):
#         print(str(self.light) + " light is opened")
#     def off(self):
#         print(str(self.light) + " light is closed")
# class CeilingFanHign(object):
#     def __init__(self, type):
#         self.ceilingfan = type
#     def on(self):
#         print(str(self.ceilingfan) + " ceiling fan is opened")
#     def off(self):
#         print(str(self.ceilingfan) + " ceiling fan is closed")
# class Stereo(object):
#     def __init__(self, type):
#         self.stereo = type
#     def on(self):
#         print(str(self.stereo) + " stereo is on")
#     def off(self):
#         print(str(self.stereo) + " stereo is off")
# #=================Device Command====================#
# class LightOnCommand(Command):
#     def __init__(self, light):
#         self.light = light
#     def execute(self):
#         self.light.on()
#     def undo(self):
#         self.light.off()
# class LightOffCommand(Command):
#     def __init__(self, light):
#         self.light = light
#     def execute(self):
#         self.light.off()
#     def undo(self):
#         self.light.on()
# # class CeilingFanOnCommand(Command):
# #     def __init__(self, ceiling):
# #         self.ceiling = ceiling
# #     def execute(self):
# #         self.ceiling.on()
# # class CeilingFanOffCommand(Command):
# #     def __init__(self, ceiling):
# #         self.ceiling= ceiling
# #     def execute(self):
# #         self.ceiling.off()
# #
# # class StereoOnCommand(Command):
# #     def __init__(self, room):
# #         self.room = room
# #     def execute(self):
# #         self.room.on()
# # class StereoOffCommand(Command):
# #     def __init__(self, room):
# #         self.room = room
# #     def execute(self):
# #         self.room.off()
# #=====================Remote Controller===================#
# class RemoteController(object):
#     def __init__(self):
#         self.onCommand = {}
#         self.offCommand = {}
#         self.undoCommand = None
#     def setCommand(self, slot, onCommand, offCommand):
#         self.onCommand.setdefault(slot, onCommand)
#         self.offCommand.setdefault(slot, offCommand)
#     def onButtonWasPress(self, slot):
#         self.onCommand[slot].execute()
#         self.undoCommand = self.onCommand[slot]
#     def offButtonWasPress(self, slot):
#         self.offCommand[slot].execute()
#         self.undoCommand = self.offCommand[slot]
#     def undoButtonWasPress(self):
#         self.undoCommand.undo()
# #=======================Client====================#
# def client():
#     controller = RemoteController()
#     livingRoomLight = Light("Living Room")
#     kitchenLight = Light("Kitchen")
#     ceilingFan = CeilingFanHign("Living Room")
#     stereo = Stereo("Living Room")
#
#     livingRoomLightOn = LightOnCommand(livingRoomLight)
#     livingRoomLightOff = LightOffCommand(livingRoomLight)
#     # kitchenLightOn = LightOnCommand(kitchenLight)
#     # kitchenLightOff = LightOffCommand(kitchenLight)
#     # ceilingFanOn = CeilingFanOnCommand(ceilingFan)
#     # ceilingFanOff = CeilingFanOffCommand(ceilingFan)
#     # stereoOn = StereoOnCommand(stereo)
#     # stereoOff = StereoOffCommand(stereo)
#
#     controller.setCommand(0, livingRoomLightOn, livingRoomLightOff)
#     # controller.setCommand(1, kitchenLightOn, kitchenLightOff)
#     # controller.setCommand(2, ceilingFanOn, ceilingFanOff)
#     # controller.setCommand(3, stereoOn, stereoOff)
#
#     controller.onButtonWasPress(0)
#     # controller.offButtonWasPress(0)
#     # controller.onButtonWasPress(1)
#     # controller.offButtonWasPress(1)
#     # controller.onButtonWasPress(2)
#     # controller.offButtonWasPress(2)
#     # controller.onButtonWasPress(3)
#     # controller.offButtonWasPress(3)
#     controller.undoButtonWasPress()
# if __name__ == '__main__':
#     client()

import sys
#===================================================================#
class Windou:
    def exit(self):
        sys.exit(0)

class Document:
    def __init__(self, filename):
        self.filename = filename
        self.contents = "This file cannot be modified"
    def save(self):
        with open(self.filename, 'w') as file:
            file.write(self.contents)
#===================================================================#
class ToolbarButton:
    def __init__(self, name, iconname):
        self.name = name
        self.iconname = iconname
    def click(self):
        self.command.execute()
class MenuItem:
    def __init__(self, menu_name, menuitem_name):
        self.menu = menu_name
        self.item = menuitem_name
    def click(self):
        self.command.execute()
class KeyboardShortcut:
    def __init__(self, key, modifire):
        self.key = key
        self.modifier = modifire
    def keyPress(self):
        self.command.execute()
#===================================================================#
class SaveCommand:
    def __init__(self, document):
        self.document = document
    def execute(self):
        self.document.save()

class ExitCommand:
    def __init__(self, window):
        self.window = window
    def execute(self):
        self.window.exit()
#===================================================================#


doc = Document("a_document.txt")
save = SaveCommand(doc)
save_button = ToolbarButton("save", 'save.png')
save_button.command = save
save_button.click()

window = Windou()
exit = ExitCommand(window)
exit_menu = MenuItem("File", "Exit")
exit_menu.command = exit
exit_menu.click()