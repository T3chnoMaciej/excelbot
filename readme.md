# EXCEL BOT
## Struggling with boring excel job that you have? No more worries! I might have a solution for you!
This little program makes your life just a bit better, when you have to be seen on excel/google calc and the pricks don't want to pay you.
## Usage:
### The program has two modes:
* 1 - dot - inserting a dot into a random cell in excell, without deleting it's original content, then waiting from 12 to 180 secodns to move to the next one. 
* 2 - message - I get it, they screwed you over big time. Now you can replace random excell cells with your message of choice! (ex. pay me now dickheads)
## Disclaimer
I am not responsible for any consequences that using this software may bring upon you. Have fun! ;)
### To get it working:
tutorial:


https://user-images.githubusercontent.com/20857124/159496004-1f3106ea-bee5-42bd-91ff-d4ac867ccab9.mp4


* install python3 and requirements. 
* run a terminal instance, then type import pyautogui . Position your mouse where the row you're "editing" is. Type in terminal pyuatogui.position(). Press enter.
* put result values into conf.json in  cell: [x, y]. 
* Do the same with name (name of the row/column you're editing, the program can email you that) and field (the very end of excel input field)
* into conf.json insert "command" - if you have macos or "control" - if you run linux or windows(you normie)
* run the program and enjoy your life! fuck corpo.
### All conf.json parameters
* "cell" - [x, y] - where's the cell you're supposed to be editing.
* "name" - [x, y] - where's name of that cell.
* "field" - [x, y] - where's input field on you calc software.
* "button" - control/command - depending on os
* "email" - 1/0 - do you want to receive email with list of edited cells when the program is done?
* em_host - ex. "smtp.host.com"
* em_user = name@host.com
* em_password = i don't have to explain that one, do i?
* em_recepient = same, rec_name@host.ocm
You can leave the em_* values blank if you don't want the emails. The program does it's own logging to a file.

## logging isn't yet implemented in second mode (message)
