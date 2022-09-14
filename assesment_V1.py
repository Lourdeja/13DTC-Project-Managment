##Questions
#Q1 What is Inheritance
    #A1 classes inheriting from other classes (true)
    #A2 dna you inherit from parents
    #A3 money you inherit from dead grandparents
    #A4 the inherit will to outcast the vast universe

#Q2 What is a base class?  
    #an object-oriented programming language, from which other classes are derived (true)
    #a mere peasant to society
    # An object-oriented programming language, that stores objects
    #the base fundemtentals of object oriented

#Q3 What is a super class
    #the class from which many subclasses can be created (true)
    #the controlling class of the objects
    #the ultimate lifeform
    #supernated class object code

#Q4 What is the main benefit of OOP?
    #Makes it much easier to create 3D objects, such as cubes, spheres for visual design 
    #Modularity: Encapsulation enables objects to be self-contained, making troubleshooting and collaborative development easier. (true)
    #Ooopsie doopsie
    #to concur code is validated and evaluated for object oriented playgrounds.

#Q5 Which of these is not related to OOP?
    #class
    #object
    #method
    #mugiwara (true)

#Q6 An __ is an instance of class
    #object (true)
    #inheritance
    #variable
    #cheese

#Q7 A __ is a template or blueprint from which objects can be instantiated from.
    #class (true)
    #integer
    #turnip
    #diaphram

#Q8 OOP stands for Object ______ Programming?
    #oriented (true)
    #originated
    #opium
    #odiss

#Q9 When sub class declares a method that has the same type of arguments as a method declared by 
#one of its superclasses, it is termed as?
    #Method overriding (true)
    #Microwave transaction
    #Operator overloading
    #Method overloading

#Q10 Can objects of abstract classes be instantiated?
    #No (true)
    #Yes
    #depends on circumstance
    #idk

#For me second stage i will begin production of code
#I am starting of with the bare necessaties

from dataclasses import dataclass
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap

app = QApplication()
main_window = QMainWindow()
main_window.setWindowTitle("Title Goes Here")
main_window.resize(1280, 720)

# Set up main window's widget
main_widget = QWidget()
main_vbox = QHBoxLayout()
main_widget.setLayout(main_vbox)

# Set up widgets
label = QLabel("Label text")
text_field = QLineEdit("Default text")
button = QPushButton("Button Text")

# Add widgets to main layout
main_vbox.addWidget(label)
main_vbox.addWidget(text_field)
main_vbox.addWidget(button)

# Run the program
main_window.show()
# main_window.showFullScreen()

# Main layout — left to right
outer_hbox = QHBoxLayout()

# Left side
left_widget = QWidget()
left_vbox = QVBoxLayout()

# Left widgets
left_label_01 = QLabel("01")
left_label_02 = QLabel("02")
left_label_03 = QLabel("03")

# Left layout
left_vbox.addWidget(left_label_01)
left_vbox.addWidget(left_label_02)
left_vbox.addWidget(left_label_03)

# Centre
centre_widget = QWidget()
centre_vbox = QVBoxLayout()

# Centre widgets
centre_label_01 = QLabel("01")
centre_label_02 = QLabel("02")
centre_label_03 = QLabel("03")

# Centre layout
centre_vbox.addWidget(centre_label_01)
centre_vbox.addWidget(centre_label_02)
centre_vbox.addWidget(centre_label_03)

# Right side
right_widget = QWidget()
right_vbox = QVBoxLayout()

# Right widgets
right_label_01 = QLabel("01")
right_label_02 = QLabel("02")
right_label_03 = QLabel("03")

# Right layout
right_vbox.addWidget(right_label_01)
right_vbox.addWidget(right_label_02)
right_vbox.addWidget(right_label_03)

# Add the three columns to the main layout
outer_hbox.addWidget(left_widget)
outer_hbox.addWidget(centre_widget)
outer_hbox.addWidget(right_widget)

app.exec()