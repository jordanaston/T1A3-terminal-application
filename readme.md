# **PlantApp.**

## [GitHub Repo](https://github.com/jordanaston/T1A3-terminal-application)

## [Source Control](https://github.com/jordanaston/T1A3-terminal-application/commits/main)

## [Trello Board](https://trello.com/b/DqOqT1Yt/t1a3-terminal-application)

## [Presentation](youtube.com)

<br>

## **Application Purpose**
PlantApp is a terminal application built in Python. It's intent is to assist users with some basic care-taking of their indoor house-plants. At the time of creation, the app supports 15 varieties of popular indoor house-plants. During use of the app, the user will create a 'collection' of their own plants with the ability to add or remove them as the please. Stored inside the app is data related to each of the supported plants. The data includes how often you should water and re-pot each plant and the appropriate location the plant should be kept to ensure the right amount of sunlight. The app will ask the user when they last watered and re-pot each plant in their collection. It will also ask if each of their plants is kept near a window or not. Based on the information submitted by the user, the app will generate helpful recommendations by comparing the user data to the data stored by the app. 

The purpose of building this app is to demonstrate my ability to design, implement and test a terminal application in Python, and throughout the process, demonstrate that I am able to use a range of developer tools. The breif for this assignment is to accept user input in the form of a file or text input and produce printed output or interact with the file system. 

<br>

## **Features** 

### Feature 1
Feature one of the application shows the user a list of plants the app currently supports and then asks the user to add the first plant to their collection after pressing 'A'. During the process the app utilizes the Pretty Table module to display the users collection back to them in a nice table structure. It then asks the user to input details relating to each of their plants, it will first ask 'how many days since you last watered your plant?' for each plant in the collection. It then asks 'how many days since you last re-potted your plant?' for each plant in the collection. Finally it asks if each of those plants are kept in a location near a window or not near a window, and the user has to answer as 'Y' or 'N'. Throughout this feature, the user is met with a list of instructions. Enter 'A' to add a plant to the collection, Enter 'R' to remove a plant from the collection and Enter 'F' to finalize the plant collection. If the user enters 'A', they are met with the same list from before to chose from when adding a plant. If the user enters 'R' the user is met with more options: Select '0' to remove a plant from position one, Select '1' to remove a plant from position two, Select '2' to remove and plant from position '3' and so on.. Once the user is happy with their list, they can select 'F' to finalize their collection. The app shows them a finalized collection of their plants with Pretty Table and moves on to the next part of the app. 

### Feature 2
Feature two of the application starts by showing the user their current plant collection in Pretty Table. It then says 'Tell me a little bit more about plant 'X' (which will be the first plant in the users collection), and asks the question, 'How many days since you last WATERED plant 'X'?. The user hopefully enters an integer (but the program will catch the error with a try and except block 'Value Error' if not). If there are any more plants in the list, the app will ask the same question for the other plants and stores these values in a dictionary to use later. If there are 0 plants in the list (which can only happen if the user removes them all) the app will continue with a collection of 0. 

### Feature 3
Feature three of the application starts by showing the user their current plant collection in Pretty Table again. It then says 'Tell me a little bit more about plant 'X' (which will be the first plant in the users collection), and asks the question, 'How many days since you last RE-POTTED plant 'X'?. The user hopefully enters an integer (but the program will catch the error with a try and except block 'Value Error' if not). If there are any more plants in the list, the app will ask the same question for the other plants and appends these values to the appropriate KEY inside the dictionary to use later.  

### Feature 4
Feature four of the application starts by showing the user their current plant collection in Pretty Table once again. It then says 'Tell me a little bit more about plant 'X' (which will be the first plant in the users collection), and asks the question, ''Y' or 'N', do you keep plant 'X' near a window?. The user hopefully enters either 'Y' or 'N' (but the program will catch the error with an IF/ ELSE condition if not). If there are any more plants in the list, the app will ask the same question for the other plants and appends these values to the appropriate KEY inside the dictionary to use later. 

### Features 2, 3 and 4
Once the user has succesuflly added all the 'plant data' (watering, re-potting and location) for each plant in their collection, the app thanks the user for the data and requests the user press 'Enter' to move forward. Once the user selects 'Enter', Pretty Table shows the users collection one last time and throws a message to say 'Based on the details you have submitted, here is some handy information!'. Laid out neatly underneath a header that shows the name of each of the plants in the users collection, a recommendation is displayed for each of the questions the app initally asked. By comparing the user data for watering, re-potting and location from the dictionary to the Plant class, the app will suggest the following:

- If the number of days since the user last watered or re-pot plant 'X' is GREATER than the number of days you should wait to water or re-pot (according to the Plant class) then a message displays to say 'You're overdue on watering/ re-potting your plant by X days!'. 
- If the number of days since the user last watered or re-pot plant 'X' is LESS than the number of days you should wait to water or re-pot (according to the Plant class) then a message displays to say 'No need to stress!, you have X days to water / re-pot your plant!
- If the number of days since the user last watered or re-pot plant 'X' is EQUAL to the number of days you should wait to water or re-pot (according to the Plant class) then a message displays to say 'Today's the day to water / re-pot your plant!

The same concept is applied to the location of the plant (near window / not near window) but this time a boolen is stored in the dictionary. Whether or not the plant 'should' be kept near a window vs if it IS kept near a window, the appropriate message is displayed with a little message about the amount of sunlight each plant requires. 
<br>

## **Code Style-Guide and Styling Conventions**

<br>

## **Implementation Plan**

<br>

## **Algorithmic Thinking**

<br>

## **Help Documentation** 

### Instructions to assist with downloading and running PlantApp.

<br>

### **System Requirements:**

<br>

### **Option One:**


- Make sure you have Python 3 installed on your computer. You can check which version you have with the following command in your terminal.
```
python3 --version
```

- If you don't have Python 3 installed, you can get it from here: https://www.python.org/downloads/

- Once you are sure Python 3 is intalled, open the terminal and head to the desired location on your computer, make a directory and initilaze a repository in that directory with the following command.
```
git init
```

- From within your directory, use the following command to clone the THIS repository to your directory.
```
git clone https://github.com/jordanaston/T1A3-terminal-application.git
```

- Use cd to enter the directory titled T1A3-terminal-application.

- With the following command run the bash script in your terminal to initialise PlantApp.
```
bash run_app.sh
```

<br>

### **Option Two:**

- Make sure you have Python 3 installed on your computer. You can check which version you have with the following command in your terminal.
```
python3 --version
```

- If you don't have Python 3 installed, you can get it from here: https://www.python.org/downloads/

- Head to https://github.com/jordanaston/T1A3-terminal-application and press the green button that says <> Code, then press Download ZIP.

- Open the ZIP file and extract the directory.

- Open your terminal cd into this directory (titled T1A3-terminal-application).

- With the following command run the bash script in your terminal to initialise PlantApp.
```
bash run_app.sh
```

Running the executable will do a couple of things automatically.

1. Checks to make sure user has Python 3 installed, and if not, echo's a message to the user with instructions on how to install. 
2. Creates the virtual environment for the user.
3. Activates the virtual environment for the user.
4. Installs all required dependencies the user will need to run the app. This is done from the requirements.txt file.
5. Runs the application for the user.
6. Finally, deactivates the virtual environment.

## **References**