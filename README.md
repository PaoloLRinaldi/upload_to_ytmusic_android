# upload_to_ytmusic_android
Officially you can't upload the songs stored in your android smartphone directly on Youtube Music.
Now, with this simple script, you can.
No programming skills required.

# Requirements
- Android
- No programming skills
- PC with Firefox installed

# Installation guide for dummies
It may take up to 15 minutes but it's extremely simple.
Let's begin.

1. Install [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=it) on your Android device.
2. Open Termux.
3. Write the following lines of code and after each one of them press Enter. Whenever it asks your permission to proceed just press "y" and then Enter.
```
apt update

apt install python-pip

pip install ytmusicapi

pkg up

pkg install git

git clone https://github.com/PaoloLRinaldi/upload_to_ytmusic_android.git

cp upload_to_ytmusic_andorid/UploadToYTMusic.py ./
```
4. Open Firefox on your PC.
5. Go to https://music.youtube.com/.
6. If you are not logged in do it.
7. Press Ctrl + Shift + i.
8. A tab has opened (let's call it DevTab). Go on the section "Network".
9. Now, on Youtube Music, click on "Library".
10. On DevTab there should be several lines. On the left of this lines there are various "200" in green. Right click on one of these lines, then go to "Copy" and finally "Copy request headers".
11. Send yourself the text that has been copied (for example via WhatsApp web, Telegram, mail, etc.). Simply press Ctrl + V to paste the text.
12. Go back to your Android device.
13. Copy the text you've sent yourself at point 10.
14. On Termux write
```
python
```
and press Enter.

15. Python has opened. Now write the following lines of code and after each one of them press Enter.
```python
from ytmusicapi import YTMusic

YTMusic.setup(filepath='headers_auth.json')
```
16. Now long press somewhere on the screen and select "Paste".
17. Press Enter.
18. Press Ctrl (right above the keyboard) and then "D".
19. Again, press Crtl and then "D".

# Usage for dummies
To launch the script open Termux and write
```
python UploadToYTMusic.py
```
and press Enter.

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

## Everytime usage
The list of all your songs will be shown in ascending time order (from the oldest to the newest).
They are numbered. Just write the list of the songs' numbers separated by Space and press Enter.

Done.

# Credits
This code is based on [this repository](https://github.com/sigma67/ytmusicapi.git) by [sigma67](https://github.com/sigma67).
