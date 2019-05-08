#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Project   : Elevator Dispatch
#
# @Purpose   : Assignment of Operaint System
#
# @Time      : 05/08/2019
#
# @Author    : Feifan Wang
#
# @Student ID: 1751694
#
# @Filename  : Controller.py

import sys
import time
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer, QThread, pyqtSignal
from elevatorInterface import Ui_MainWindow


class Elevator:
    ''' define Elevator '''

    def __init__(self, parent=None):
        super(Elevator, self).__init__()
        self.statusFree = True
        self.statusUp = False
        self.statusDown = False
        self.stay = False
        self.currentFloor = 1
        self.goList = []

    def move(self):
        # change status of Elevator
        if len(self.goList):
            self.statusFree = False
            if min(self.goList) > self.currentFloor:
                self.statusFree = False
                self.statusUp = True
                self.statusDown = False
            elif max(self.goList) < self.currentFloor:
                self.statusFree = False
                self.statusUp = False
                self.statusDown = True
        else:
            self.statusFree = True
            self.statusUp = False
            self.statusDown = False

    def updateFloor(self):
        if self.ifArrive():
            self.goList.remove(self.currentFloor)
            return

        if len(self.goList):
            if self.statusUp:
                self.currentFloor += 1
            else:
                self.currentFloor -= 1

    def ifArrive(self):
        return self.currentFloor in self.goList


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    ''' interactions on interface '''

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_1u.clicked.connect(lambda: up(1))
        self.ui.pushButton_2u.clicked.connect(lambda: up(2))
        self.ui.pushButton_3u.clicked.connect(lambda: up(3))
        self.ui.pushButton_4u.clicked.connect(lambda: up(4))
        self.ui.pushButton_5u.clicked.connect(lambda: up(5))
        self.ui.pushButton_6u.clicked.connect(lambda: up(6))
        self.ui.pushButton_7u.clicked.connect(lambda: up(7))
        self.ui.pushButton_8u.clicked.connect(lambda: up(8))
        self.ui.pushButton_9u.clicked.connect(lambda: up(9))
        self.ui.pushButton_10u.clicked.connect(lambda: up(10))
        self.ui.pushButton_11u.clicked.connect(lambda: up(11))
        self.ui.pushButton_12u.clicked.connect(lambda: up(12))
        self.ui.pushButton_13u.clicked.connect(lambda: up(13))
        self.ui.pushButton_14u.clicked.connect(lambda: up(14))
        self.ui.pushButton_15u.clicked.connect(lambda: up(15))
        self.ui.pushButton_16u.clicked.connect(lambda: up(16))
        self.ui.pushButton_17u.clicked.connect(lambda: up(17))
        self.ui.pushButton_18u.clicked.connect(lambda: up(18))
        self.ui.pushButton_19u.clicked.connect(lambda: up(19))
        self.ui.pushButton_2d.clicked.connect(lambda: down(2))
        self.ui.pushButton_3d.clicked.connect(lambda: down(3))
        self.ui.pushButton_4d.clicked.connect(lambda: down(4))
        self.ui.pushButton_5d.clicked.connect(lambda: down(5))
        self.ui.pushButton_6d.clicked.connect(lambda: down(6))
        self.ui.pushButton_7d.clicked.connect(lambda: down(7))
        self.ui.pushButton_8d.clicked.connect(lambda: down(8))
        self.ui.pushButton_9d.clicked.connect(lambda: down(9))
        self.ui.pushButton_10d.clicked.connect(lambda: down(10))
        self.ui.pushButton_11d.clicked.connect(lambda: down(11))
        self.ui.pushButton_12d.clicked.connect(lambda: down(12))
        self.ui.pushButton_13d.clicked.connect(lambda: down(13))
        self.ui.pushButton_14d.clicked.connect(lambda: down(14))
        self.ui.pushButton_15d.clicked.connect(lambda: down(15))
        self.ui.pushButton_16d.clicked.connect(lambda: down(16))
        self.ui.pushButton_17d.clicked.connect(lambda: down(17))
        self.ui.pushButton_18d.clicked.connect(lambda: down(18))
        self.ui.pushButton_19d.clicked.connect(lambda: down(19))
        self.ui.pushButton_20d.clicked.connect(lambda: down(20))
        self.ui.elevator1_1.clicked.connect(lambda: insidePush(1, 1))
        self.ui.elevator1_2.clicked.connect(lambda: insidePush(1, 2))
        self.ui.elevator1_3.clicked.connect(lambda: insidePush(1, 3))
        self.ui.elevator1_4.clicked.connect(lambda: insidePush(1, 4))
        self.ui.elevator1_5.clicked.connect(lambda: insidePush(1, 5))
        self.ui.elevator1_6.clicked.connect(lambda: insidePush(1, 6))
        self.ui.elevator1_7.clicked.connect(lambda: insidePush(1, 7))
        self.ui.elevator1_8.clicked.connect(lambda: insidePush(1, 8))
        self.ui.elevator1_9.clicked.connect(lambda: insidePush(1, 9))
        self.ui.elevator1_10.clicked.connect(lambda: insidePush(1, 10))
        self.ui.elevator1_11.clicked.connect(lambda: insidePush(1, 11))
        self.ui.elevator1_12.clicked.connect(lambda: insidePush(1, 12))
        self.ui.elevator1_13.clicked.connect(lambda: insidePush(1, 13))
        self.ui.elevator1_14.clicked.connect(lambda: insidePush(1, 14))
        self.ui.elevator1_15.clicked.connect(lambda: insidePush(1, 15))
        self.ui.elevator1_16.clicked.connect(lambda: insidePush(1, 16))
        self.ui.elevator1_17.clicked.connect(lambda: insidePush(1, 17))
        self.ui.elevator1_18.clicked.connect(lambda: insidePush(1, 18))
        self.ui.elevator1_19.clicked.connect(lambda: insidePush(1, 19))
        self.ui.elevator1_20.clicked.connect(lambda: insidePush(1, 20))
        self.ui.elevator2_1.clicked.connect(lambda: insidePush(2, 1))
        self.ui.elevator2_2.clicked.connect(lambda: insidePush(2, 2))
        self.ui.elevator2_3.clicked.connect(lambda: insidePush(2, 3))
        self.ui.elevator2_4.clicked.connect(lambda: insidePush(2, 4))
        self.ui.elevator2_5.clicked.connect(lambda: insidePush(2, 5))
        self.ui.elevator2_6.clicked.connect(lambda: insidePush(2, 6))
        self.ui.elevator2_7.clicked.connect(lambda: insidePush(2, 7))
        self.ui.elevator2_8.clicked.connect(lambda: insidePush(2, 8))
        self.ui.elevator2_9.clicked.connect(lambda: insidePush(2, 9))
        self.ui.elevator2_10.clicked.connect(lambda: insidePush(2, 10))
        self.ui.elevator2_11.clicked.connect(lambda: insidePush(2, 11))
        self.ui.elevator2_12.clicked.connect(lambda: insidePush(2, 12))
        self.ui.elevator2_13.clicked.connect(lambda: insidePush(2, 13))
        self.ui.elevator2_14.clicked.connect(lambda: insidePush(2, 14))
        self.ui.elevator2_15.clicked.connect(lambda: insidePush(2, 15))
        self.ui.elevator2_16.clicked.connect(lambda: insidePush(2, 16))
        self.ui.elevator2_17.clicked.connect(lambda: insidePush(2, 17))
        self.ui.elevator2_18.clicked.connect(lambda: insidePush(2, 18))
        self.ui.elevator2_19.clicked.connect(lambda: insidePush(2, 19))
        self.ui.elevator2_20.clicked.connect(lambda: insidePush(2, 20))
        self.ui.elevator3_1.clicked.connect(lambda: insidePush(3, 1))
        self.ui.elevator3_2.clicked.connect(lambda: insidePush(3, 2))
        self.ui.elevator3_3.clicked.connect(lambda: insidePush(3, 3))
        self.ui.elevator3_4.clicked.connect(lambda: insidePush(3, 4))
        self.ui.elevator3_5.clicked.connect(lambda: insidePush(3, 5))
        self.ui.elevator3_6.clicked.connect(lambda: insidePush(3, 6))
        self.ui.elevator3_7.clicked.connect(lambda: insidePush(3, 7))
        self.ui.elevator3_8.clicked.connect(lambda: insidePush(3, 8))
        self.ui.elevator3_9.clicked.connect(lambda: insidePush(3, 9))
        self.ui.elevator3_10.clicked.connect(lambda: insidePush(3, 10))
        self.ui.elevator3_11.clicked.connect(lambda: insidePush(3, 11))
        self.ui.elevator3_12.clicked.connect(lambda: insidePush(3, 12))
        self.ui.elevator3_13.clicked.connect(lambda: insidePush(3, 13))
        self.ui.elevator3_14.clicked.connect(lambda: insidePush(3, 14))
        self.ui.elevator3_15.clicked.connect(lambda: insidePush(3, 15))
        self.ui.elevator3_16.clicked.connect(lambda: insidePush(3, 16))
        self.ui.elevator3_17.clicked.connect(lambda: insidePush(3, 17))
        self.ui.elevator3_18.clicked.connect(lambda: insidePush(3, 18))
        self.ui.elevator3_19.clicked.connect(lambda: insidePush(3, 19))
        self.ui.elevator3_20.clicked.connect(lambda: insidePush(3, 20))
        self.ui.elevator4_1.clicked.connect(lambda: insidePush(4, 1))
        self.ui.elevator4_2.clicked.connect(lambda: insidePush(4, 2))
        self.ui.elevator4_3.clicked.connect(lambda: insidePush(4, 3))
        self.ui.elevator4_4.clicked.connect(lambda: insidePush(4, 4))
        self.ui.elevator4_5.clicked.connect(lambda: insidePush(4, 5))
        self.ui.elevator4_6.clicked.connect(lambda: insidePush(4, 6))
        self.ui.elevator4_7.clicked.connect(lambda: insidePush(4, 7))
        self.ui.elevator4_8.clicked.connect(lambda: insidePush(4, 8))
        self.ui.elevator4_9.clicked.connect(lambda: insidePush(4, 9))
        self.ui.elevator4_10.clicked.connect(lambda: insidePush(4, 10))
        self.ui.elevator4_11.clicked.connect(lambda: insidePush(4, 11))
        self.ui.elevator4_12.clicked.connect(lambda: insidePush(4, 12))
        self.ui.elevator4_13.clicked.connect(lambda: insidePush(4, 13))
        self.ui.elevator4_14.clicked.connect(lambda: insidePush(4, 14))
        self.ui.elevator4_15.clicked.connect(lambda: insidePush(4, 15))
        self.ui.elevator4_16.clicked.connect(lambda: insidePush(4, 16))
        self.ui.elevator4_17.clicked.connect(lambda: insidePush(4, 17))
        self.ui.elevator4_18.clicked.connect(lambda: insidePush(4, 18))
        self.ui.elevator4_19.clicked.connect(lambda: insidePush(4, 19))
        self.ui.elevator4_20.clicked.connect(lambda: insidePush(4, 20))
        self.ui.elevator5_1.clicked.connect(lambda: insidePush(5, 1))
        self.ui.elevator5_2.clicked.connect(lambda: insidePush(5, 2))
        self.ui.elevator5_3.clicked.connect(lambda: insidePush(5, 3))
        self.ui.elevator5_4.clicked.connect(lambda: insidePush(5, 4))
        self.ui.elevator5_5.clicked.connect(lambda: insidePush(5, 5))
        self.ui.elevator5_6.clicked.connect(lambda: insidePush(5, 6))
        self.ui.elevator5_7.clicked.connect(lambda: insidePush(5, 7))
        self.ui.elevator5_8.clicked.connect(lambda: insidePush(5, 8))
        self.ui.elevator5_9.clicked.connect(lambda: insidePush(5, 9))
        self.ui.elevator5_10.clicked.connect(lambda: insidePush(5, 10))
        self.ui.elevator5_11.clicked.connect(lambda: insidePush(5, 11))
        self.ui.elevator5_12.clicked.connect(lambda: insidePush(5, 12))
        self.ui.elevator5_13.clicked.connect(lambda: insidePush(5, 13))
        self.ui.elevator5_14.clicked.connect(lambda: insidePush(5, 14))
        self.ui.elevator5_15.clicked.connect(lambda: insidePush(5, 15))
        self.ui.elevator5_16.clicked.connect(lambda: insidePush(5, 16))
        self.ui.elevator5_17.clicked.connect(lambda: insidePush(5, 17))
        self.ui.elevator5_18.clicked.connect(lambda: insidePush(5, 18))
        self.ui.elevator5_19.clicked.connect(lambda: insidePush(5, 19))
        self.ui.elevator5_20.clicked.connect(lambda: insidePush(5, 20))

        self.moveElevator1 = MoveThread1()
        self.moveElevator2 = MoveThread2()
        self.moveElevator3 = MoveThread3()
        self.moveElevator4 = MoveThread4()
        self.moveElevator5 = MoveThread5()
        self.work = WorkThread()
        self.change = ChangeThread()
        self.downWaitList = DownWaitListThread()
        self.upWaitList = UpWaitListThread()
        self.work.start()
        if Elevator_1.stay == False:
            self.work.trigger.connect(lambda: self.moveElevator1.start())
        if Elevator_2.stay == False:
            self.work.trigger.connect(lambda: self.moveElevator2.start())
        if Elevator_3.stay == False:
            self.work.trigger.connect(lambda: self.moveElevator3.start())
        if Elevator_4.stay == False:
            self.work.trigger.connect(lambda: self.moveElevator4.start())
        if Elevator_5.stay == False:
            self.work.trigger.connect(lambda: self.moveElevator5.start())
        if (Elevator_1.statusUp == False or Elevator_2.statusUp == False or Elevator_3.statusUp == False
                or Elevator_4.statusUp == False or Elevator_5.statusUp == False):
            self.work.trigger.connect(lambda: self.downWaitList.start())
        if (Elevator_1.statusDown == False or Elevator_2.statusDown == False or Elevator_3.statusDown == False
                or Elevator_4.statusDown == False or Elevator_5.statusDown == False):
            self.work.trigger.connect(lambda: self.upWaitList.start())
        self.timer = QTimer()
        self.timer.timeout.connect(lambda: self.work.start())
        self.timer.start(0.01)
        self.timer_2 = QTimer()
        self.timer_2.timeout.connect(lambda: self.change.start())
        self.timer_2.start(0.01)

    def changeFloor(self):
        self.ui.floor_e1.setText(str(Elevator_1.currentFloor))
        self.ui.floor_e2.setText(str(Elevator_2.currentFloor))
        self.ui.floor_e3.setText(str(Elevator_3.currentFloor))
        self.ui.floor_e4.setText(str(Elevator_4.currentFloor))
        self.ui.floor_e5.setText(str(Elevator_5.currentFloor))

    def move1(self):
        # 1. Move elevators
        # 2. Change status of elevators
        if Elevator_1.stay == False:
            Elevator_1.stay = True
            if Elevator_1.ifArrive():
                self.ui.status_e1.setStyleSheet("color: rgb(99,192,135);")
                self.ui.status_e1.setText("open")
                #Elevator_1.goList.remove(Elevator_1.currentFloor)
                time.sleep(1)
                update1()
            elif Elevator_1.statusFree:
                self.ui.status_e1.setStyleSheet("color: rgb(223,129,113);")
                self.ui.status_e1.setText("closed")
                update1()
            elif Elevator_1.statusUp:
                self.ui.status_e1.setStyleSheet("color: rgb(106,189,144);")
                self.ui.status_e1.setText("running")
                for i in range(10):
                    time.sleep(0.05)
                    self.ui.elevator1Slider.setValue(
                        self.ui.elevator1Slider.value()+1)
                update1()
            elif Elevator_1.statusDown:
                self.ui.status_e1.setStyleSheet("color: rgb(106,189,144);")
                self.ui.status_e1.setText("running")
                for i in range(10):
                    time.sleep(0.05)
                    self.ui.elevator1Slider.setValue(
                        self.ui.elevator1Slider.value()-1)
                update1()

    def move2(self):
        if Elevator_2.stay == False:
            Elevator_2.stay = True
            if Elevator_2.ifArrive():
                self.ui.status_e2.setStyleSheet("color: rgb(99,192,135);")
                self.ui.status_e2.setText("open")
                #Elevator_2.goList.remove(Elevator_2.currentFloor)
                time.sleep(1)
                update2()
            elif Elevator_2.statusFree:
                self.ui.status_e2.setStyleSheet("color: rgb(223,129,113);")
                self.ui.status_e2.setText("closed")
                update2()
            elif Elevator_2.statusUp:
                self.ui.status_e2.setStyleSheet("color: rgb(106,189,144);")
                self.ui.status_e2.setText("running")
                for i in range(10):
                    time.sleep(0.05)
                    self.ui.elevator2Slider.setValue(
                        self.ui.elevator2Slider.value()+1)
                update2()
            elif Elevator_2.statusDown:
                self.ui.status_e2.setStyleSheet("color: rgb(106,189,144);")
                self.ui.status_e2.setText("running")
                for i in range(10):
                    time.sleep(0.05)
                    self.ui.elevator2Slider.setValue(
                        self.ui.elevator2Slider.value()-1)
                update2()

    def move3(self):
        if Elevator_3.stay == False:
            Elevator_3.stay = True
            if Elevator_3.ifArrive():
                self.ui.status_e3.setStyleSheet("color: rgb(99,192,135);")
                self.ui.status_e3.setText("open")
                #Elevator_3.goList.remove(Elevator_3.currentFloor)
                time.sleep(1)
                update3()
            elif Elevator_3.statusFree:
                self.ui.status_e3.setStyleSheet("color: rgb(223,129,113);")
                self.ui.status_e3.setText("closed")
                update3()
            elif Elevator_3.statusUp:
                self.ui.status_e3.setStyleSheet("color: rgb(106,189,144);")
                self.ui.status_e3.setText("running")
                for i in range(10):
                    time.sleep(0.05)
                    self.ui.elevator3Slider.setValue(
                        self.ui.elevator3Slider.value()+1)
                update3()
            elif Elevator_3.statusDown:
                self.ui.status_e3.setStyleSheet("color: rgb(106,189,144);")
                self.ui.status_e3.setText("running")
                for i in range(10):
                    time.sleep(0.05)
                    self.ui.elevator3Slider.setValue(
                        self.ui.elevator3Slider.value()-1)
                update3()

    def move4(self):
        if Elevator_4.stay == False:
            Elevator_4.stay = True
            if Elevator_4.ifArrive():
                self.ui.status_e4.setStyleSheet("color: rgb(99,192,135);")
                self.ui.status_e4.setText("open")
                #Elevator_4.goList.remove(Elevator_4.currentFloor)
                time.sleep(1)
                update4()
            elif Elevator_4.statusFree:
                self.ui.status_e4.setStyleSheet("color: rgb(223,129,113);")
                self.ui.status_e4.setText("closed")
                update4()
            elif Elevator_4.statusUp:
                self.ui.status_e4.setStyleSheet("color: rgb(106,189,144);")
                self.ui.status_e4.setText("running")
                for i in range(10):
                    time.sleep(0.05)
                    self.ui.elevator4Slider.setValue(
                        self.ui.elevator4Slider.value()+1)
                update4()
            elif Elevator_4.statusDown:
                self.ui.status_e4.setStyleSheet("color: rgb(106,189,144);")
                self.ui.status_e4.setText("running")
                for i in range(10):
                    time.sleep(0.05)
                    self.ui.elevator4Slider.setValue(
                        self.ui.elevator4Slider.value()-1)
                update4()

    def move5(self):
        if Elevator_5.stay == False:
            Elevator_5.stay = True
            if Elevator_5.ifArrive():
                self.ui.status_e5.setStyleSheet("color: rgb(99,192,135);")
                self.ui.status_e5.setText("open")
                #Elevator_5.goList.remove(Elevator_5.currentFloor)
                time.sleep(1)
                update5()
            elif Elevator_5.statusFree:
                self.ui.status_e5.setStyleSheet("color: rgb(223,129,113);")
                self.ui.status_e5.setText("closed")
                update5()
            elif Elevator_5.statusUp:
                self.ui.status_e5.setStyleSheet("color: rgb(106,189,144);")
                self.ui.status_e5.setText("running")
                for i in range(10):
                    time.sleep(0.05)
                    self.ui.elevator5Slider.setValue(
                        self.ui.elevator5Slider.value()+1)
                update5()
            elif Elevator_5.statusDown:
                self.ui.status_e5.setStyleSheet("color: rgb(106,189,144);")
                self.ui.status_e5.setText("running")
                for i in range(10):
                    time.sleep(0.05)
                    self.ui.elevator5Slider.setValue(
                        self.ui.elevator5Slider.value()-1)
                update5()


class MoveThread1(QThread):

    def __int__(self):
        super(MoveThread1, self).__init__()

    def run(self):
        Elevator_1.move()
        MainWindow.move1(w)


class MoveThread2(QThread):

    def __int__(self):
        super(MoveThread2, self).__init__()

    def run(self):
        Elevator_2.move()
        MainWindow.move2(w)


class MoveThread3(QThread):

    def __int__(self):
        super(MoveThread3, self).__init__()

    def run(self):
        Elevator_3.move()
        MainWindow.move3(w)


class MoveThread4(QThread):

    def __int__(self):
        super(MoveThread4, self).__init__()

    def run(self):
        Elevator_4.move()
        MainWindow.move4(w)


class MoveThread5(QThread):

    def __int__(self):
        super(MoveThread5, self).__init__()

    def run(self):
        Elevator_5.move()
        MainWindow.move5(w)


class WorkThread(QThread):
    ''' Dispatch elevators every 0.001s '''
    trigger = pyqtSignal()

    def __int__(self):
        super(WorkThread, self).__init__()

    def run(self):
        self.trigger.emit()


class DownWaitListThread(QThread):
    def __int__(self):
        super(DownWaitListThread, self).__init__()

    def run(self):
        if len(downWaiting):
            down(downWaiting.pop(0))


class UpWaitListThread(QThread):
    def __int__(self):
        super(UpWaitListThread, self).__init__()

    def run(self):
        if len(upWaiting):
            up(upWaiting.pop(0))


class ChangeThread(QThread):
    ''' Dispatch elevators every 0.001s '''\


    def __int__(self):
        super(ChangeThread, self).__init__()

    def run(self):
        MainWindow.changeFloor(w)


def update1():
    Elevator_1.stay = False
    Elevator_1.updateFloor()


def update2():
    Elevator_2.stay = False
    Elevator_2.updateFloor()
    #Elevator_2.move()


def update3():
    Elevator_3.stay = False
    Elevator_3.updateFloor()
    #Elevator_3.move()


def update4():
    Elevator_4.stay = False
    Elevator_4.updateFloor()
    # Elevator_4.move()


def update5():
    Elevator_5.stay = False
    Elevator_5.updateFloor()
    # Elevator_5.move()


def up(num):
    # When the up buttons outside the elevators are pushed
    # Choose proper elevator to response
    # Priority : 1. closest
    #            2. going down
    #            3. free
    # If there are no elevators available currently,
    # append the request into upWaiting list
    elevatorDValue = []
    if Elevator_1.statusDown == False and Elevator_1.currentFloor <= num:
        if Elevator_1.statusUp == False:
            elevatorDValue.append(abs(Elevator_1.currentFloor-num)+1)
        else:
            elevatorDValue.append(abs(Elevator_1.currentFloor-num))
    else:
        elevatorDValue.append(20)
    if Elevator_2.statusDown == False and Elevator_2.currentFloor <= num:
        if Elevator_2.statusUp == False:
            elevatorDValue.append(abs(Elevator_2.currentFloor-num)+1)
        else:
            elevatorDValue.append(abs(Elevator_2.currentFloor-num))
    else:
        elevatorDValue.append(20)
    if Elevator_3.statusDown == False and Elevator_3.currentFloor <= num:
        if Elevator_3.statusUp == False:
            elevatorDValue.append(abs(Elevator_3.currentFloor-num)+1)
        else:
            elevatorDValue.append(abs(Elevator_3.currentFloor-num))
    else:
        elevatorDValue.append(20)
    if Elevator_4.statusDown == False and Elevator_4.currentFloor <= num:
        if Elevator_4.statusUp == False:
            elevatorDValue.append(abs(Elevator_4.currentFloor-num)+1)
        else:
            elevatorDValue.append(abs(Elevator_4.currentFloor-num))
    else:
        elevatorDValue.append(20)
    if Elevator_5.statusDown == False and Elevator_5.currentFloor <= num:
        if Elevator_5.statusUp == False:
            elevatorDValue.append(abs(Elevator_5.currentFloor-num)+1)
        else:
            elevatorDValue.append(abs(Elevator_5.currentFloor-num))
    else:
        elevatorDValue.append(20)

    if min(elevatorDValue) > 20:
        upWaiting.append(num)
    else:
        if elevatorDValue.index(min(elevatorDValue)) == 0:
            if num not in Elevator_1.goList:
                Elevator_1.goList.append(num)
        elif elevatorDValue.index(min(elevatorDValue)) == 1:
            if num not in Elevator_2.goList:
                Elevator_2.goList.append(num)
        elif elevatorDValue.index(min(elevatorDValue)) == 2:
            if num not in Elevator_3.goList:
                Elevator_3.goList.append(num)
        elif elevatorDValue.index(min(elevatorDValue)) == 3:
            if num not in Elevator_4.goList:
                Elevator_4.goList.append(num)
        elif elevatorDValue.index(min(elevatorDValue)) == 4:
            if num not in Elevator_5.goList:
                Elevator_5.goList.append(num)


def down(num):
    # When the down buttons outside the elevators are pushed
    # Choose proper elevator to response
    # Priority : 1. closest
    #            2. going down
    #            3. free
    # If there are no elevators available currently,
    # append the request into downWaiting list
    elevatorDValue = []
    if Elevator_1.statusUp == False and Elevator_1.currentFloor >= num:
        if Elevator_1.statusDown == False:
            elevatorDValue.append(
                abs(Elevator_1.currentFloor-num)+1)  # set priority
        else:
            elevatorDValue.append(abs(Elevator_1.currentFloor-num))
    else:
        elevatorDValue.append(20)
    if Elevator_2.statusUp == False and Elevator_2.currentFloor >= num:
        if Elevator_2.statusDown == False:
            elevatorDValue.append(abs(Elevator_2.currentFloor-num)+1)
        else:
            elevatorDValue.append(abs(Elevator_2.currentFloor-num))
    else:
        elevatorDValue.append(20)
    if Elevator_3.statusUp == False and Elevator_3.currentFloor >= num:
        if Elevator_3.statusDown == False:
            elevatorDValue.append(abs(Elevator_3.currentFloor-num)+1)
        else:
            elevatorDValue.append(abs(Elevator_3.currentFloor-num))
    else:
        elevatorDValue.append(20)
    if Elevator_4.statusUp == False and Elevator_4.currentFloor >= num:
        if Elevator_4.statusDown == False:
            elevatorDValue.append(abs(Elevator_4.currentFloor-num)+1)
        else:
            elevatorDValue.append(abs(Elevator_4.currentFloor-num))
    else:
        elevatorDValue.append(20)
    if Elevator_5.statusUp == False and Elevator_5.currentFloor >= num:
        if Elevator_5.statusDown == False:
            elevatorDValue.append(abs(Elevator_5.currentFloor-num)+1)
        else:
            elevatorDValue.append(abs(Elevator_5.currentFloor-num))
    else:
        elevatorDValue.append(20)

    if min(elevatorDValue) >= 20:
        downWaiting.append(num)
    else:
        if elevatorDValue.index(min(elevatorDValue)) == 0:
            if num not in Elevator_1.goList:
                Elevator_1.goList.append(num)
        elif elevatorDValue.index(min(elevatorDValue)) == 1:
            if num not in Elevator_2.goList:
                Elevator_2.goList.append(num)
        elif elevatorDValue.index(min(elevatorDValue)) == 2:
            if num not in Elevator_3.goList:
                Elevator_3.goList.append(num)
        elif elevatorDValue.index(min(elevatorDValue)) == 3:
            if num not in Elevator_4.goList:
                Elevator_4.goList.append(num)
        elif elevatorDValue.index(min(elevatorDValue)) == 4:
            if num not in Elevator_5.goList:
                Elevator_5.goList.append(num)


def insidePush(index, num):
    # When the buttons inside the elevators are pushed
    # append the request into Elevator_index.goList
    if index == 1 and num not in Elevator_1.goList:
        Elevator_1.goList.append(num)
    elif index == 2 and num not in Elevator_2.goList:
        Elevator_2.goList.append(num)
    elif index == 3 and num not in Elevator_3.goList:
        Elevator_3.goList.append(num)
    elif index == 4 and num not in Elevator_4.goList:
        Elevator_4.goList.append(num)
    elif index == 5 and num not in Elevator_5.goList:
        Elevator_5.goList.append(num)


if __name__ == "__main__":
    Elevator_1 = Elevator()
    Elevator_2 = Elevator()
    Elevator_3 = Elevator()
    Elevator_4 = Elevator()
    Elevator_5 = Elevator()
    upWaiting = []
    downWaiting = []

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())