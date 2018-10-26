import Model
import GUI
import RepeatableTimer
import profile

if __name__ == "__main__":
    print("------------------GUI:-------------------")
    gui=GUI.GUI()
    #profile.run(gui.__init__())
    print("------------------Model:-------------------")
    model = Model.Model()
    profile.run("model.__init__()")
    profile.run("model.updateMap()")
    print("------------------RepeatableTimer:-------------------")
    time=RepeatableTimer.RepeatableTimer(0,gui.job)
    profile.run("time.__init__(0,gui.job)")
    profile.run("time.start()")