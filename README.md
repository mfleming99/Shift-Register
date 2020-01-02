# Shift-Register
This script will automatically register you for shifts on WhenIWork.

To get this script to work with your accounts, you will have to change the login credentials in the scrip itself. In addition you can change the function `dayFree` to match your availabilities. It will parse the month and day of the shift our of the email, but you will have to change it matches your availabilities.

This script needs to be running 24/7 in order to work. I found that the easiest way to do this is to put it on a AWS server.

To begin automatically getting shifts call 

`python shiftGetter.py`.

Good luck getting more shifts!
