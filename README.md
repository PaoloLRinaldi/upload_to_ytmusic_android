# upload_to_ytmusic_android
Officially you can't upload the songs stored in your android smartphone directly on Youtube Music.
Now, with this simple script, you can.
No programming skills required.

Technically you could upload your songs by opening https://music.youtube.com/ from whichever browser on your phone and switching to Desktop mode.
However, once installed, this script makes this procedure 10x faster.

# Requirements
- Android
- No programming skills
- PC with Firefox, Chrome or Edge installed

# Installation guide for dummies
It may take up to 15 minutes but it's extremely simple.
Let's begin.

1. Install [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=it) on your Android device.
2. Open Termux. Since the built-in keyboards are very uncomfortable to use with Termux, it's strongly recommended to use [Hacker's Keyboard](https://play.google.com/store/apps/details?id=org.pocketworkstation.pckeyboard&hl=it).
3. Write the following line
```
termux-setup-storage
```
then press Enter and select "Allow".

4. Write the following lines of code and after each one of them press Enter. Alternatively you can copy them altogether and paste them on Termux (not recommended) and, when it arrives at the last command, just press Enter once.
```
apt update -y

pkg install python -y

pip install ytmusicapi

pkg up -y

apt update -y

pkg install git -y

git clone https://github.com/PaoloLRinaldi/upload_to_ytmusic_android.git

cp upload_to_ytmusic_andorid/UploadToYTMusic.py ./
```
5. Open Firefox/Chrome/Edge on your PC.
6. Go to https://music.youtube.com/.
7. If you are not logged in do it.
8. Press Ctrl + Shift + i.
9. A tab has opened (let's call it DevTab). Go on the section "Network" and on the search bar (named "Filter" or "Filter URLs") type "browse".
10. Now, on Youtube Music, click on "Library".
11. If Firefox:
    - On DevTab there should be several lines. On the left of these lines there are various "200" in green. Right click on any of these lines labeled with "POST", then go to "Copy" and finally "Copy request headers".

    If Chrome or Edge:
    - On DevTab there should be several lines (or requests). Choose a request and verify that it looks like this: **Status** 200, **Type** xhr, **Name** ``browse?...``
    - Click on the Name of any matching request. In the "Headers" tab, scroll to the section "Request headers" and copy everything starting from "accept: \*/\*" to the end of the section

12. Send the text that has been copied to your account (for example via WhatsApp web, Telegram, mail, etc.). Simply press Ctrl + V to paste the text.
13. Go back to your Android device.
14. Copy to clipboard the text you've sent to your account at point 12.
15. On Termux write
```
python
```
and press Enter.

16. Python has opened. Now write the following lines of code and after each one of them press Enter.
```python
from ytmusicapi import YTMusic

YTMusic.setup(filepath='headers_auth.json')
```
17. Now long press somewhere on the screen and select "Paste".
18. Press Enter.
19. Press Ctrl (right above the keyboard) and then "D".
20. Again, press Crtl and then "D".

# Usage for dummies
To launch the script open Termux and write
```
python UploadToYTMusic.py
```
and press Enter.

The list of all your songs will be shown in ascending time order (from the oldest to the newest).
They are numbered. Just write the list of the songs' numbers separated by Space and press Enter.

Done.


## First Time
The first time you launch it, it will ask you the directory where you store your music. It must be an absolute path.
For example if you store it in the Download directory the path will be:
```
/storage/emulated/0/Download/
```
If you put it in a folder named Music it will be
```
/storage/emulated/0/Music/
```
### Music in SD Card
Go on "Android Settings -> Apps -> Termux -> Permissions" and manually give the permissions for external storage.
If you store it in your SD card the path is simple. Open termux and write:
```
ls /storage | egrep "[A-Z0-9]{4}-[A-Z0-9]{4}"
```
and press Enter. The output should be of the form ????-???? where each "?" is a digit or a capital letter.
Now simply substitute "emulated/0" with your output (e.g. 0012-ABCD) in the path. So if you store your music
in a folder named Music, the path will be
```
/storage/0012-ABCD/Music/
```
Again, "0012-ABCD" is just an example. Remember to use the output of the line of code above.

# Authentication Expired
In case of authentication expired you have to regenerate the 'headers_auth.json' file.
Simply repeat steps 5 to 20 in "Installation guide for dummies".

# Credits
This code is based on [this repository](https://github.com/sigma67/ytmusicapi.git) by [sigma67](https://github.com/sigma67).
