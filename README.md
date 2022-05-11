# CC Video Instructions
### Known Bugs/Issues
* You cannot generate your own `.pkl` file
* Excel files have a chance to become corrupted! Save and make copies at regular intervals during QC
* The attached excel file *cannot* be open at the same time while QC is being done.

### Changelog v1.0:
* Mid-slice button works! Just click on the up and down arrows next to “set mid-slice” to look through the mid-slice of the image. The default mid-slice is set to 89.
* Added two new rotate buttons! Click them to rotate any images clockwise or counterclockwise. The program remembers this new orientation for future images, if you ever need to QC a dataset with images rotated a certain way. 
* The blank “ghost” button bug no longer appears when customizing the program
* Under the “file path will appear here,” you can now highlight the path with your cursor if you ever need to copy/paste that path directly to your clipboard.
### Changelog v1.1:
* Scrolling through the midslices with “set midslice” is now instantaneous. There is zero lag once the initial image has been loaded.
Added a hotkey! Press the spacebar to pause the program if you are looping through the images in a slideshow, instead of having to click that pesky little “pause” button. I will probably add more hotkeys in the future. Let me know which hotkeys would be the most useful for you. 
Changelog v1.2:
* NOTE: WORK IN PROGRESS: The program now tells you if the image is currently being loaded or not. When the image is loaded correctly, there will be green text saying “Image Loaded!”. If the program is currently in the process of showing a new image, there will be a red text saying “Image Loading…”
Added two columns for “motion error” and “notes” that adds this data in separate columns to the attached excel sheet. 


### Folder Contents
The script that will be used to run the program contains: 
* the executable file `cc_final`
* A user-defined excel sheet
* A “pickle” file that is contains the paths to the images
    * Note: Message Kevin Low (kevinlow@usc.edu) with help to generate this file, if it is not yet present


### Starting the Program:
#### Mac Instructions
1. Open terminal (on Mac, go to the top right of your screen and click on the magnifying glass, then type in “terminal” to run it). 
2. Change directories to the location of where you copied the CCVIS folder
(`cd /Users/kevinlow/Documents/CCVis`)
3. Run the program by typing `./cc_final_mac`
#### Windows Instructions
1. Use your file explorer and go to the folder containing the `cc_final_win` program
2. Double click the `cc_final_win` file to run it. 
 
### The Program:
Note: Depending on your computer, you may need to put the application into fullscreen mode to see all the features
* "Current image" shows the image # that is being displayed from the list
* "Running Status" shows if the program is currently moving through a slideshow of the images, or is paused
* Press "Quit" to quit the program
* Before quitting, note the “Current Image” number so that you can later pick up where you last left off.

### Customizing the Application 
* Before you can begin your analysis, first click on the Customize button on the left side of the screen. Here is where you will customize the program.
* To set which excel file you want to have the abnormality data output to, type in the file name (including the .xlsx extension) in the “Excel Sheet Path” text box. Note: the excel sheet must be in the CCVis folder. 
    * For example, type in “CC_Abnormalities_List.xlsx” into the text box (without quotes)
* To set any custom abnormality buttons, type in the text box “Custom Abnormality Buttons”. To add multiple buttons, separate each entry with a semicolon. 
    * For example, “Button here;Button there; Button everywhere!” typed into the text box (without the quotation marks) will add the buttons “Button here”, “Button there” and “Button everywhere!” on the right side of the main screen.
* If you have a pickle file, simply type that into the text box “Pickle File Path”. For example, “cc_files.pkl” into the text box.
This pickle file contains all the paths for the images you will do QC on. The program reads each path and outputs the image for you to QC.
Once you are ready, click on “Apply Changes” at the bottom. You are now ready to begin the program!
* If you are unsure if the customization worked correctly, open up the terminal. You should see some text pop up describing any errors that might have occured.

### Running the application from the start:
* To start viewing images in a video format (one image shown about every 5 seconds), click on the "Loop Images" button.
 
### Pause and Play:
* To pause your slideshow, click the "Pause" button. Note: you will need to click the "Pause" button in the moment between the images switching, when your cursor stops showing the rainbow loading icon and has its regular cursor. You should now see the "Running Status" at the left change from "True" or "Running" to "Paused"
* To see which number image you are currently on, see the “Current image” on the left side of the screen.
* To play the slideshow, press the "Play" button, THEN click the "loop images" button. The program should start running again where you left off. 
 
### Running the application from a certain image number:
* If you open the application and want to start at a certain image, type in the number in the text box on the right of the “Go To Image” button. You can confirm that it is showing the correct image # by looking at the "Current Image" at the left. 

### Changing the View
* Mid-slice: If the program is showing somewhat off of the mid-slice, you can change the mid-slice coordinates with the “Set Mid-slice” scrollbar. Simply click the up or down arrows next to the “89” mid-slice number, and it will automatically change the mid-slice of the current image. Remember, the program remembers this new mid-slice for new images, so make sure to change the mid-slice back to 89 before QCing further images!
* Rotation: If the image is rotated at an odd angle, you can click one of the rotate buttons to rotate the image! As with the mid-slice function, the program will remember this new rotation as you continue to QC further images.

### Adding Abnormalities to Excel Sheet
* First, make sure that you do NOT have the excel sheet open while adding data.
* If you see an abnormality in the cc, press the Pause button. 
* After identifying the kind of abnormality, type in the abnormality in the “Describe the Abnormality Here:” text box. 
    * Note: To save time, you can also  press one of the “add abnormality” buttons to add a specific, preset abnormality that was customized before.
* Once you are done, press “Add Data to Spreadsheet”. After you press this button, the text you entered in step 3 will display in the “Abnormality will appear here” zone, which confirms that the data was added to the excel sheet successfully. 
* Once your text appears in the “Abnormality will appear here”, you are free to delete any text in the “Describe the Abnormality Here” text box and continue with your analyses. See “Pause and Play” to continue using the program. 
* If you want to review the excel sheet, open your excel document in the CCVis folder. The first column, “Image Number” shows the number of the image if you ever want to go back and review that image using this program. “Abnormality” is the abnormality text you inputted previously, and the “Path to Image” shows the image’s path on the grid.

## Questions, contact Kevin Low (kevinlow@usc.edu)
