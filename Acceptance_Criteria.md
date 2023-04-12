# Acceptance Criteria 
1. **As a User** I want to be able to access to the *_real-time_* database that is linked with the face recognition attendance system so that I can see people in my database.
      - [ ] User must register to Firebase to create a real-time database.
      - [ ] User must generate a private key and Admin SDK configuration must be added to the python file that is connected to the database.

--------------------------------------------------------------------------------------------------------------------------------------------------

2.  **As a User** I want to be able to *_choose the camera_* which connects to the software so that I could use the preferable device. 
      - [ ] User cannot use a camera which has an issue while connecting with the system.
--------------------------------------------------------------------------------------------------------------------------------------------------

3.  **As a User** I want to be able to *_add data about people_* in my database so that the information about them would be stored in one place.
      - [ ] User cannot add data if he/she doesn't have an access to the data. 
      - [ ] User can decide on what kind of details will be stored but ID and name must be included to verify identity. 
      - [ ] Personal data must be in JSON format where key is the ID number and value is another key-value pair of people's details.
--------------------------------------------------------------------------------------------------------------------------------------------------
4.  **As a User** I want to be able to add new people to my database so that they would also be included.
      - [ ] To add a new person the User needs to provide ID number and the name.
      - [ ] User cannot have more than one person in the database with the same ID number.
--------------------------------------------------------------------------------------------------------------------------------------------------
5.  **As a User** I want to be able to add pictures of people in my database so that they would be recognized by the software.
      - [ ] All pictures must be of the same size.
      - [ ] Pictures must be identical to the person.
      - [ ] Picture can't be a random image. The system won't allow to add the picture of something other than human face.
--------------------------------------------------------------------------------------------------------------------------------------------------
6.  **As a User** I want to be able to change data about people in my database so that the information could be up-to-date in case of any changes.
      - [ ] If the User wants to change the ID number it cannot be the same as an ID number of any other person.
--------------------------------------------------------------------------------------------------------------------------------------------------
7.  **As a User** I want to be able to change pictures of people in my database so that it would be up-to-date in case of any changes in appearance.
      - [ ] The picture has to be the same size as the previous one.
      - [ ] The system won't allow to change the picture to a picture of something other than human face.
--------------------------------------------------------------------------------------------------------------------------------------------------
8.  **As a User** I want to be able to remove a person from my database in case someone is not part of the organization, school, or etc any more so that the system wouldn't recognize them anymore.
                  * All the information about the person including their picture and ID is removed as well.
                  * The system shouldn't recognize removed person.
--------------------------------------------------------------------------------------------------------------------------------------------------
9. **As a User** I want to be able to use a face recognition system to monitor entry from the place so that it can quickly and accurately record the attendance.
      - [ ] The face recognition system should be able to accurately identify each individual entering the place.
      - [ ] The system should be able to handle a high volume of entries without experiencing significant delays or errors.
      - [ ] The face recognition system should be able to accurately identify each individual entering the place.
--------------------------------------------------------------------------------------------------------------------------------------------------
10. **As a User** I want to have the attendance system that recognizes people's face saved in the database so that I don't have to check their face one by one and compare with ID or anything that can verify the identity.
      - [ ] The system will compare people's face with pictures from database.
      - [ ] Pictures from database are linked with people's ID number.
--------------------------------------------------------------------------------------------------------------------------------------------------
11. **As a User** I want to be able to see profile picture, name and ID of a person on the screen when someone takes the attendance so that I get know his/her details without checking their ID card.
      - [ ] The details about the person should only be displayed if the attendance is taken after more time than set time limit.
-------------------------------------------------------------------------------------------------------------------------------------------------   
12. **As a User** I want to be able to view total attendance of a person till the current time on the screen when someone takes the attendance for convenience so that I don't have to access my database to check everytime.
      - [ ]  Personal details must have a variable that stores total attendance days.
      - [ ] The number of total attendance is updated each time there is a new attendance of that person.
      - [ ] The number includes the current attendance.
--------------------------------------------------------------------------------------------------------------------------------------------------
13. **As a User** I want to be able to set the time limit after which one person can be marked again so that it can fit my purpose for using this software.
      - [ ] Personal details in python file must have a variable that stores last attendance time in a format of YYYY-MM-DD hh:mm:ss
      - [ ] Before the user changes the time limit it is set to one minute as a default.
      - [ ] The time limit can be changed by the user (from 5 seconds to infinity)
--------------------------------------------------------------------------------------------------------------------------------------------------
14. **As a User** I want a notification to appear if someone has already took attendance within the time limit so that there is no duplicate attendance saved in the database.
      - [ ] System will check the current time and compare to the last attended time of the person when taking an attendance.
      - [ ] If the time from the last presence is less than the time limit the notification should appear.
      - [ ] The system should display "Already marked".
      - [ ] The system shouldn't count this as a new attendance.
--------------------------------------------------------------------------------------------------------------------------------------------------
15. **As a User** I want to have the attendance system that automatically update my attendance database when someone checks the attendance so that I don't need to manually fill in attendance sheets which will save time and reduce the risk of errors. 
      - [ ] The system updates the total number of attendance when the person is present.
      - [ ] If the time from the last presence is less than the time limit the total attendance won't be changed.
--------------------------------------------------------------------------------------------------------------------------------------------------
16. **As a User** I want to be able to view data about specific person in my database so that I can find the information I'm currently looking for.
      - [ ]  All of the information added previously by the user can be viewed.
      - [ ] The information when was the last time someone was present can also be viewed.
--------------------------------------------------------------------------------------------------------------------------------------------------
17. **As a User** I want to be able to see when was the last time someone was present so that I don't have to check it manually.
       - [ ] The information is stored in a format "year-month-day hours:minutes:seconds".
       - [ ] The date is updated each time a that person is present.
       - [ ] The information isn't updated if the time between the previous one and the current attendance is less than the time limit.
--------------------------------------------------------------------------------------------------------------------------------------------------
18. **As a User** I want to be able to see how many people are in my database so that I don't have to count them manually.
      - [ ] The number is updated each time a new person is added to the database.
      - [ ] The number is updated each time a person is removed from the database.
      - [ ] The count of people should be accurate and match the actual number of people in the database.
      - [ ] The count of people should be accessible to all authorized users, and should be protected from unauthorized access.
