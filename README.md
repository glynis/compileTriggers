compileTriggers
===============

(This readme is still being updated, please excuse the brevity...)

Ask for subject number range from the user, ranging from 1-24.

The first for loop separates the ecode column out of the eventlist file.  It goes line by line through this file and if the line does not start with # (denoting the header of the file), the ecode column's value is put into a new list in a new .txt file.

The second for loop combines the ecode column and the triggers list.  

Lastly there is a checking function.
