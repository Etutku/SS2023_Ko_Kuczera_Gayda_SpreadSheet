# Acceptance Criteria [Updated]
--------------------------------------------------------------------------------------------------------------------------------------------------
1. **As a User** I want database that will automatically upload data to the face recognition system up-to-date so that I don't need to manually input them again.
      - **Priority** --> 1
      - [ ] User must have an account for Firebase website.
      - [ ] User must create a real-time database on the Firebase website.
      - [ ] User must download a private key file from the website and add it to the program directory.
      - [ ] User must add Admin SDK configuration provided by Firebase to the python file that is connected to the real-time database.
      - [ ] Implement a secure and scalable database system to store attendance data, with optimized data structures and indexes to ensure fast and efficient data retrieval.

--------------------------------------------------------------------------------------------------------------------------------------------------

2.  **As a User** I want to be able to add people's details and make modification to my database so that the database would include people and data necessary for my purpose of using this system. 
      - **Priority** --> 1
      - [ ] Personal data must be in JSON format where key is the ID number and value is another key-value pair where kes are the field names (ex) name, DOB, etc) and values are personal details of each person.
      - [ ] ID number is compulsory when adding a new person to the database.
      - [ ] User cannot have more than one person in the database with the same ID number.
      - [ ] If the User wants to change the ID number it cannot be the same as an ID number of any other person.
--------------------------------------------------------------------------------------------------------------------------------------------------

3.  **As a User** I want to be able to add pictures of people in my database so that they would be recognized by the software.
      - **Priority** --> 1
      - [x] All pictures must be 512px*512px.
      - [ ] Picture must be identical to the person.
      - [ ] User must add pictures into the separate directory in the program.
      - [ ] The name of the picture should be the same as person's ID number.
      - [ ] If the picture is in the wrong fomat then the program will show an error.
--------------------------------------------------------------------------------------------------------------------------------------------------
4.  **As a User** I want to be able to change pictures of people in my database so that it would be up-to-date in case of any changes in appearance.
      - **Priority** --> 2
      - [ ] The picture has to be the same size as the previous one (512px*512px).
      - [ ] The new picture should have the same name as the old one which is person's ID number.
      - [ ] If the picture is in the wrong fomat then the program will show an error.
--------------------------------------------------------------------------------------------------------------------------------------------------
5.  **As a User** I want to be able to remove a person from my database in case someone is not part of the organization, school, or etc any more so that the system wouldn't recognize them anymore.
      - **Priority** --> 2
      - [ ] All the information about the person must be removed from the database.
      - [ ] Picture must be removed from the directory as well.
      - [ ] The system shouldn't recognize removed person anymore.
--------------------------------------------------------------------------------------------------------------------------------------------------
6.  **As a User** I want to be able to use webcam real-time so that the system will compare images and people's face to verify the identity for attendance.
      -**Priority** --> 1
      - [ ] The real-time webcam will be shown on the left side of the system.
      - [ ] The system will compare people's face with pictures from database.
      - [ ] Pictures from database are linked with people's ID number.
      - [ ] The system will detect and recognize faces with varying facial expressions, such as glasses regarding the pictures from database.
--------------------------------------------------------------------------------------------------------------------------------------------------
7. **As a User** I want to be able to see personal details of on the screen when someone takes the attendance so that I get to know his/her details without checking their ID card.
      - **Priority** --> 3
      - [ ] ID, name, profile picture and total attendance should be displayed on the screen.
      - [ ] On the right side of the system, above details must be displayed once the system recognizes the face.
      - [ ] These details should only be displayed if the attendance is taken after the time limit set by the system.
--------------------------------------------------------------------------------------------------------------------------------------------------
8. **As a User** I want to be able to view total attendance of a person till the current time on the screen when someone takes the attendance so that I don't have to access my database to check everytime.
      - **Priority** --> 2
      - [ ] Personal details must have a variable that stores total attendance days.
      - [ ] The number of total attendance is updated each time there is a new attendance of that person.
      - [ ] The number includes the current attendance.
--------------------------------------------------------------------------------------------------------------------------------------------------
9. **As a User** I want to be able to set the time limit after which one person can be marked again so that it can fit my purpose for using this software.
      - **Priority** --> 2
      - [x] Personal details in python file must have a variable that stores last attendance time in a format of YYYY-MM-DD hh:mm:ss
      - [ ] Before the user changes the time limit it is set to one minute as a default.
      - [ ] The time limit can be changed by the user (from 5 seconds to infinity)
--------------------------------------------------------------------------------------------------------------------------------------------------
10. **As a User** I want the system to show attendance status of the person taking the attendance so that he/she knows whether the attendance has been taken or not.
      - **Priority** --> 2
      - [ ] There should be 4 modes: 'Active', 'Marked', displayed information about a person recently marked and 'Already marked'. 
      - [x] 'Active' mode should appear when there is no face detected in the camera.
      - [x] 'Marked' mode should appear when someone was detected and the attendance was added.
      - [ ]  Information about the person should appear after marked mode and be displayed for a few seconds.

--------------------------------------------------------------------------------------------------------------------------------------------------
11. **As a User** I want a notification to appear if someone has already took attendance within the time limit so that there is no duplicate attendance saved in the database.
      - **Priority** --> 3
      - [ ] System will check the current time and compare to the last attended time of the person when taking an attendance.
      - [ ] If the time from the last presence is less than the time limit the notification should appear.
      - [ ] The system should display "Already marked".
      - [ ] The system shouldn't count this as a new attendance.
-------------------------------------------------------------------------------------------------------------------------------------------------   
12. **As a User** I want to have the attendance system that automatically update my attendance database when someone checks the attendance so that I don't need to manually fill in attendance sheets which will save time and reduce the risk of errors. 
      - **Priority** --> 1
      - [ ]  The system updates the total number of attendance when the person is present.
      - [ ]  If the time from the last presence is less than the time limit the total attendance won't be changed.
--------------------------------------------------------------------------------------------------------------------------------------------------
13. **As a User** I want to be able to view data about specific person in my database so that I can find the information I'm currently looking for.
      - **Priority** --> 1
      - [ ] All of the information added previously by the user can be viewed on Firebase.
      - [ ] The information when was the last time someone was present can also be viewed.
--------------------------------------------------------------------------------------------------------------------------------------------------
14. **As a User** I want to be able to see when was the last time someone was present so that I don't have to check it manually.
      - **Priority** --> 2
      - [ ] The information is stored in a format "YYYY-MM-DD hh:mm:ss".
      - [ ] The date is updated each time a that person is present.
      - [ ] The information isn't updated if the time between the previous one and the current attendance is less than the time limit.
--------------------------------------------------------------------------------------------------------------------------------------------------
15. **As a User** I want to be able to see how many people are in my database so that I don't have to count them manually.
      - **Priority** --> 3
      - [ ] The number is updated each time a new person is added to the database.
      - [ ] The number is updated each time a person is removed from the database.
      - [ ] The count of people should be accurate and match the actual number of people in the database.
--------------------------------------------------------------------------------------------------------------------------------------------------
