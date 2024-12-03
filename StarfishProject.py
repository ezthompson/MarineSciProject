from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from PySide6.QtMultimedia import *
import sys
import os

envpath = r'C:\ProgramData\Anaconda3\envs\CV36\Lib\site-packages\PySide6\plugins\platforms'
os.environ["QT_QPA_PLATFORM_PLUGIN_PATH"] = envpath

buttonSound = QSoundEffect()
buttonSound.setSource(QUrl.fromLocalFile("sound/button press.wav"))
buttonSound.setVolume(0.25)

moveSound = QSoundEffect()
moveSound.setSource(QUrl.fromLocalFile("sound/paper_out.wav"))
moveSound.setVolume(0.25)


class StarfishProject(QStackedWidget):
    def __init__(self):
        # Initializing all the inherited properties of QStackedWidget
        super().__init__()
        self.CreateWindow()

    def CreateWindow(self):
        self.setGeometry(100, 100, 800, 600)
        self.setFixedSize(QSize(800, 600))
        self.setWindowTitle("Starfish Project")

        # Creating the 'pages' for the user to tab through
        self.MainWindow = QWidget()
        self.GenInfoWindow = QWidget()
        self.BodyFunctionsWindow = QWidget()
        self.FeedingHabitsWindow = QWidget()
        self.MovementWindow = QWidget()
        self.ReproductionWindow = QWidget()

        self.setStyleSheet("""
        QLabel#titleLabel {font-family: Verdana; font-size: 32px;}
        QLabel#infoLabel {text-align: left; font-size: 21px;}
        QLabel#image {border: 7px solid tan; border-radius: 10px;}
        QPushButton {font-size: 25px; border: 2px solid black; border-radius: 5px; height: 30px; width: 15px;}
        QPushButton:hover {background-color: #FFFFFF; border: 3px solid black; border-radius: 7px;}
        QPushButton#leftButton, QPushButton#rightButton {height: 30px; width: 30px;}
        """)

        # Running each function as to create each screen
        self.CreateMainWindow()
        self.CreateGenInfoWindow()
        self.CreateBodyWindow()
        self.CreateFeedingWindow()
        self.CreateMovementWindow()
        self.CreateReproductionWindow()

        self.show()

    # Creating the widgets and layout for the home screen
    def CreateMainWindow(self):
        self.mainGrid = QGridLayout()

        self.titleLabel = QLabel("Starfish Project", objectName="titleLabel")

        # Creating a QPixmap object with the star_mainScreen image and then putting it in a label as to display on the screen
        self.starImage = QPixmap("images/main/star_mainScreen.jpg")
        self.starImageLabel = QLabel(objectName="image")
        self.starImageLabel.setPixmap(
            self.starImage.scaled(400, 400, Qt.KeepAspectRatio))

        self.buttonBox = QVBoxLayout()

        # Creating the buttons needed to go to each screen along with setting the function to be called when clicked
        self.genInfoButton = QPushButton("General Info", clicked=lambda:
                                         self.ChangeScreen(self.genInfoButton.text()))

        self.bodyButton = QPushButton("Body Functions", clicked=lambda:
                                      self.ChangeScreen(self.bodyButton.text()))

        self.feedingButton = QPushButton("Feeding Habits", clicked=lambda:
                                         self.ChangeScreen(self.feedingButton.text()))

        self.movementButton = QPushButton("Movement", clicked=lambda:
                                          self.ChangeScreen(self.movementButton.text()))

        self.reproductionButton = QPushButton("Reproduction", clicked=lambda:
                                              self.ChangeScreen(self.reproductionButton.text()))

        self.buttonList = [self.genInfoButton,
                           self.bodyButton, self.feedingButton, self.movementButton, self.reproductionButton]
        for button in self.buttonList:
            self.buttonBox.addWidget(button)

        self.mainGrid.addWidget(self.titleLabel, 0, 0, 1, 2, Qt.AlignCenter)
        self.mainGrid.addWidget(self.starImageLabel, 1,
                                0, 1, 1, Qt.AlignCenter)
        self.mainGrid.addLayout(self.buttonBox, 1, 1, 1, 1)
        self.mainGrid.setVerticalSpacing(0)

        self.MainWindow.setLayout(self.mainGrid)

        # Adding the window to the list of widgets to index through
        self.addWidget(self.MainWindow)

    # Getting the button's text and then going to the proper screen
    def ChangeScreen(self, buttonPressed):
        buttonSound.play()
        if buttonPressed == "Home":
            self.setCurrentIndex(0)
        elif buttonPressed == "General Info":
            self.setCurrentIndex(1)
        elif buttonPressed == "Body Functions":
            self.setCurrentIndex(2)
        elif buttonPressed == "Feeding Habits":
            self.setCurrentIndex(3)
        elif buttonPressed == "Movement":
            self.setCurrentIndex(4)
        elif buttonPressed == "Reproduction":
            self.setCurrentIndex(5)

    # When the buttons to go left or right are pressed, set the StackedWidget's index to the proper screen
    def MoveScreen(self, direction):
        moveSound.play()
        currentIndex = self.currentIndex()
        if direction == "left":
            self.setCurrentIndex(currentIndex - 1)
        else:
            self.setCurrentIndex(currentIndex + 1)

    def CreateGenInfoWindow(self):
        self.infoGrid = QGridLayout()

        self.moveBox = QHBoxLayout()

        # Creating a blank QLabel so that the moveBox's appearance remains consistent across screens
        self.blankLabel = QLabel()

        self.genInfoTitle = QLabel("General Info", objectName="titleLabel")

        self.rightButton = QPushButton(
            "->", objectName="rightButton", clicked=lambda: self.MoveScreen("right"))

        self.moveBox.addWidget(self.blankLabel)
        self.moveBox.addWidget(self.genInfoTitle)
        self.moveBox.addWidget(self.rightButton)

        self.infoLabel = QLabel("""
        \u2022Also known as sea stars, starfish are invertebrates that belong to the class Asteroidea, the same class as sea urchins and sand dollars.
        \u2022Length can range from 4.7 to 9.4 inches.
        \u2022Typically only have 5 limbs but species with up to 40 limbs have been known to exist.
        \u2022Live mostly in saltwater with a select few living in brackish water, not confined to one type of environment and can be found all over the world.
        """, objectName="infoLabel")
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setStyleSheet("QLabel {font-size: 24px;}")

        self.imageBox = QVBoxLayout()

        self.genInfoImage = QPixmap("images/genInfo/star_genInfoScreen1.jpg")
        self.genImageLabel = QLabel(objectName="image")
        self.genImageLabel.setPixmap(
            self.genInfoImage.scaled(400, 400, Qt.KeepAspectRatio))

        self.genInfoImage2 = QPixmap("images/genInfo/star_genInfoScreen2.jpg")
        self.genImageLabel2 = QLabel(objectName="image")
        self.genImageLabel2.setPixmap(
            self.genInfoImage2.scaled(400, 400, Qt.KeepAspectRatio))

        self.genInfoImage2Caption = QLabel(
            "An example of a starfish with 19 limbs", objectName="imageCaption")

        self.imageBox.addWidget(self.genImageLabel)
        self.imageBox.addWidget(self.genImageLabel2)
        self.imageBox.addWidget(self.genInfoImage2Caption, 0, Qt.AlignCenter)

        self.imageBox.insertStretch(-1, 1)

        self.homeButton = QPushButton(
            "Home", clicked=lambda: self.ChangeScreen("Home"))

        self.infoGrid.addLayout(self.moveBox, 0, 0, 1, 3)
        self.infoGrid.addWidget(self.infoLabel, 1, 0, 1, 1)
        self.infoGrid.addLayout(self.imageBox, 1, 1, 1, 1)
        self.infoGrid.addWidget(
            self.homeButton, self.infoGrid.rowCount() + 1, 0, 1, 3)
        self.GenInfoWindow.setLayout(self.infoGrid)

        self.addWidget(self.GenInfoWindow)

    def CreateBodyWindow(self):
        self.bodyGrid = QGridLayout()

        self.moveBox = QHBoxLayout()

        self.leftButton = QPushButton(
            "<-", objectName="leftButton", clicked=lambda: self.MoveScreen("left"))

        self.bodyFuncTitle = QLabel(
            "Body Functions", objectName="titleLabel")

        self.rightButton = QPushButton(
            "->", objectName="rightButton", clicked=lambda: self.MoveScreen("right"))

        self.moveBox.addWidget(self.leftButton)
        self.moveBox.addWidget(self.bodyFuncTitle, 0, Qt.AlignCenter)
        self.moveBox.addWidget(self.rightButton)

        self.infoLabel = QLabel("""
        \u2022Have bony, calcified skin that protects them from predators and can scare off others through its bright colors.
        \u2022Can regenerate limbs or an entire body as their vital organs are kept in their arms which can be used to get away from predators.
        \u2022Do not have a typical circulatory system with blood, instead using a water vascular system to take in water to pump nutrients through the body.
        \u2022Do not have a central brain, instead relying on nerves in the arms along with light and chemical sensors to interpret their environment.
        """, objectName="infoLabel")
        self.infoLabel.setStyleSheet("QLabel {font-size: 20px;}")
        self.infoLabel.setWordWrap(True)

        self.imageBox = QVBoxLayout()

        self.bodyFuncImage = QPixmap("images/bodyFunctions/star_bodyFunc1.jpg")
        self.bodyImageLabel = QLabel(objectName="image")
        self.bodyImageLabel.setPixmap(
            self.bodyFuncImage.scaled(400, 400, Qt.KeepAspectRatio))

        self.bodyInfoImageCaption = QLabel(
            "Note the hard, calcified skin", objectName="imageCaption")

        self.bodyFuncImage2 = QPixmap(
            "images/bodyFunctions/star_bodyFunc2.jpg")
        self.bodyImageLabel2 = QLabel(objectName="image")
        self.bodyImageLabel2.setPixmap(
            self.bodyFuncImage2.scaled(300, 300, Qt.KeepAspectRatio))

        self.bodyInfoImage2Caption = QLabel(
            "A diagram of a starfish's water vascular system", objectName="imageCaption")

        self.imageBox.addWidget(self.bodyImageLabel, 0, Qt.AlignCenter)
        self.imageBox.addWidget(self.bodyInfoImageCaption, 0, Qt.AlignCenter)
        self.imageBox.addWidget(self.bodyImageLabel2, 0, Qt.AlignCenter)
        self.imageBox.addWidget(self.bodyInfoImage2Caption, 0, Qt.AlignCenter)

        self.imageBox.insertStretch(-1, 1)

        self.homeButton = QPushButton(
            "Home", clicked=lambda: self.ChangeScreen("Home"))

        self.bodyGrid.addLayout(self.moveBox, 0, 0, 1, 3)
        self.bodyGrid.addWidget(self.infoLabel, 1, 0, 1, 1)
        self.bodyGrid.addLayout(self.imageBox, 1, 1, 1, 1)
        self.bodyGrid.addWidget(
            self.homeButton, self.bodyGrid.rowCount() + 1, 0, 1, 3)
        self.BodyFunctionsWindow.setLayout(self.bodyGrid)

        self.addWidget(self.BodyFunctionsWindow)

    def CreateFeedingWindow(self):
        self.feedingGrid = QGridLayout()

        self.moveBox = QHBoxLayout()

        self.leftButton = QPushButton(
            "<-", objectName="leftButton", clicked=lambda: self.MoveScreen("left"))

        self.feedingTitle = QLabel("Feeding Habits", objectName="titleLabel")

        self.rightButton = QPushButton(
            "->", objectName="rightButton", clicked=lambda: self.MoveScreen("right"))

        self.moveBox.addWidget(self.leftButton)
        self.moveBox.addWidget(self.feedingTitle, 0, Qt.AlignCenter)
        self.moveBox.addWidget(self.rightButton)

        self.infoLabel = QLabel("""
        \u2022Main prey are other invertebrates such as mussels and clams who live on the sea floor.
        \u2022Some species are able to bring out their stomachs from their mouth through eversion, allowing them to partially dissolve prey and suck up the rest of the nutrients later. 
        \u2022Predators of starfish include sea turtles, crabs, and sea otters who can either eat the starfish whole or flip it over to eat the softer underside.
        """, objectName="infoLabel")
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setStyleSheet("QLabel {font-size: 24px;}")

        self.imageBox = QVBoxLayout()

        self.feedingImage = QPixmap(
            "images/feedingHabits/star_feedingHabits.jpg")
        self.feedingImageLabel = QLabel(objectName="image")
        self.feedingImageLabel.setPixmap(
            self.feedingImage.scaled(300, 300, Qt.IgnoreAspectRatio))

        self.feedingImageCaption = QLabel(
            "An example of a starfish performing eversion on its stomach", objectName="imageCaption")

        self.imageBox.addStretch()
        self.imageBox.addWidget(self.feedingImageLabel, 0, Qt.AlignCenter)
        self.imageBox.addWidget(self.feedingImageCaption, 0, Qt.AlignCenter)
        self.imageBox.addStretch()

        self.imageBox.setAlignment(Qt.AlignCenter)
        self.imageBox.insertStretch(-1, 0.1)

        self.homeButton = QPushButton(
            "Home", clicked=lambda: self.ChangeScreen("Home"))

        self.feedingGrid.addLayout(self.moveBox, 0, 0, 1, 3)
        self.feedingGrid.addWidget(self.infoLabel, 1, 0, 1, 1)
        self.feedingGrid.addLayout(self.imageBox, 1, 1, 1, 1)
        self.feedingGrid.addWidget(
            self.homeButton, self.feedingGrid.rowCount() + 1, 0, 1, 3)
        self.FeedingHabitsWindow.setLayout(self.feedingGrid)

        self.addWidget(self.FeedingHabitsWindow)

    def CreateMovementWindow(self):
        self.movementGrid = QGridLayout()

        self.moveBox = QHBoxLayout()

        self.leftButton = QPushButton(
            "<-", objectName="leftButton", clicked=lambda: self.MoveScreen("left"))

        self.movementTitle = QLabel("Movement", objectName="titleLabel")

        self.rightButton = QPushButton(
            "->", objectName="rightButton", clicked=lambda: self.MoveScreen("right"))

        self.moveBox.addWidget(self.leftButton)
        self.moveBox.addWidget(self.movementTitle, 0, Qt.AlignCenter)
        self.moveBox.addWidget(self.rightButton)

        self.infoLabel = QLabel("""
        \u2022On the inner side of the starfish are thousands of tiny tube-like feet that allow for the starfish to rapidly stick and unstick to a surface.
            \u25aaEach foot has two parts: an ampulla, a water-filled sac, and a podium, a flat tip of muscle that acts as a sucker.
            \u25aaWater enters through the starfish's madreporite, a small plate on the outer side of the starfish that allows water to enter in its water vascular system, filling all the canals of the starfish including the ones attached to the feet.
            \u25aaAfter the water enters in the feet canals, pressure builds up which causes the ampulla to press down on the podium, making the starfish 'stick'. Once the water pressure is decreased, the ampulla relaxes, 'unsticking' the podium.
        """, objectName="infoLabel")
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setStyleSheet("QLabel {font-size: 18px;}")

        self.imageBox = QVBoxLayout()

        self.movementImage = QPixmap(
            "images/movement/star_movement.jpg")
        self.movementImageLabel = QLabel(objectName="image")
        self.movementImageLabel.setPixmap(
            self.movementImage.scaled(400, 400, Qt.KeepAspectRatio))
        self.movementImageLabel.setScaledContents(True)

        self.imageBox.addWidget(self.movementImageLabel, 0, Qt.AlignCenter)

        self.homeButton = QPushButton(
            "Home", clicked=lambda: self.ChangeScreen("Home"))

        self.movementGrid.addLayout(self.moveBox, 0, 0, 1, 3)
        self.movementGrid.addWidget(self.infoLabel, 1, 0, 1, 1)
        self.movementGrid.addLayout(self.imageBox, 1, 1, 1, 1)
        self.movementGrid.addWidget(
            self.homeButton, self.movementGrid.rowCount() + 1, 0, 1, 3)
        self.MovementWindow.setLayout(self.movementGrid)

        self.addWidget(self.MovementWindow)

    def CreateReproductionWindow(self):
        self.reproGrid = QGridLayout()

        self.moveBox = QHBoxLayout()

        self.leftButton = QPushButton(
            "<-", objectName="leftButton", clicked=lambda: self.MoveScreen("left"))

        self.reproTitle = QLabel("Reproduction", objectName="titleLabel")

        self.blankLabel = QLabel()

        self.moveBox.addWidget(self.leftButton)
        self.moveBox.addWidget(self.reproTitle, 0, Qt.AlignCenter)
        self.moveBox.addWidget(self.blankLabel)

        self.infoLabel = QLabel("""
        \u2022Starfish can reproduce both sexually and asexually:
            \u25aaAsexual reproduction can be performed by allowing a limb to detach from the body, allowing the body to regenerate slowly over time.
            \u25aaSexual reproduction is performed through broadcasting sperm throughout the water in hopes of finding a female's eggs to attach to. Once found, the eggs fertilize and starfish are born in a larvae-like plankton form, growing to its adult form usually in a few months.
        """, objectName="infoLabel")
        self.infoLabel.setWordWrap(True)
        self.infoLabel.setStyleSheet("QLabel {font-size: 22px;}")

        self.imageBox = QVBoxLayout()

        self.reproductionImage = QPixmap(
            "images/reproduction/star_reproduction.jpg")
        self.reproductionImageLabel = QLabel(objectName="image")
        self.reproductionImageLabel.setPixmap(
            self.reproductionImage.scaled(400, 400, Qt.KeepAspectRatio))

        self.reproductionCaption = QLabel(
            "A starfish splitting itself apart to form a new starfish", objectName="imageCaption")

        self.reproductionImage2 = QPixmap(
            "images/reproduction/star_reproduction2.jpg")
        self.reproductionImageLabel2 = QLabel(objectName="image")
        self.reproductionImageLabel2.setPixmap(
            self.reproductionImage2.scaled(300, 300, Qt.IgnoreAspectRatio))

        self.reproductionCaption2 = QLabel(
            "Two starfish performing sexual reproduction", objectName="imageCaption")

        self.imageBox.addWidget(self.reproductionImageLabel)
        self.imageBox.addWidget(self.reproductionCaption, 0, Qt.AlignCenter)
        self.imageBox.addWidget(
            self.reproductionImageLabel2, 0, Qt.AlignCenter)
        self.imageBox.addWidget(self.reproductionCaption2, 0, Qt.AlignCenter)

        self.imageBox.insertStretch(-1, 1)

        self.homeButton = QPushButton(
            "Home", clicked=lambda: self.ChangeScreen("Home"))

        self.reproGrid.addLayout(self.moveBox, 0, 0, 1, 3)
        self.reproGrid.addWidget(self.infoLabel, 1, 0, 1, 1)
        self.reproGrid.addLayout(self.imageBox, 1, 1, 1, 1)
        self.reproGrid.addWidget(
            self.homeButton, self.reproGrid.rowCount() + 1, 0, 1, 3)
        self.ReproductionWindow.setLayout(self.reproGrid)

        self.addWidget(self.ReproductionWindow)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = StarfishProject()

    p = QPalette()
    gradient = QLinearGradient(0, 0, 0, 400)
    gradient.setColorAt(0.5, QColor(240, 240, 240))
    gradient.setColorAt(0.8, QColor(222, 243, 246))
    p.setBrush(QPalette.Window, QBrush(gradient))
    window.setPalette(p)

    sys.exit(app.exec_())
