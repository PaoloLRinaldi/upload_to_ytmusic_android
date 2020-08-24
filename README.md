# upload_to_ytmusic_android
Officially you can't upload the songs stored in your android smartphone directly on Youtube Music.
With this simple script you now can.

# Requirements
- Android
- No programming skills
- PC with Firefox installed

# Installation guide
It may take up to 20 minutes.

1. Install [Termux](https://play.google.com/store/apps/details?id=com.termux&hl=it) on your Android device.
2. Open Termux.
3. Write the following lines of code and after each one of them press Enter.
```
apt update
```
```
apt install python-pip
```
```
pip install ytmusicapi
```
4. Open Firefox on your PC.
5. Go to https://music.youtube.com/.
6. Press Ctrl + Shift + i.
7. A tab has opened (let's call it DevTab). Go on the section "Network".
8. Now, on Youtube Music, click on "Library".
9. On DevTab there should be several lines. On the left of this lineas there are various "200" in green. Right click on one of these lines, then go to "Copy" and finally "Copy request headers".
10. Send yourself the text that has been copied (for example via WhatsApp web, Telegram, mail, etc.). Simply press Ctrl + V to paste the text.
11. Go back to your Android device.
12. Copy the text you've sent yourself at point 10.
13. On Termux write
```
python
```
and press Enter.

12. Python has opened. Now write the following lines of code and after each one of them press Enter.
```python
from ytmusicapi import YTMusic
```
```python
YTMusic.setup(filepath='headers_auth.json')
```
13. Now long press somewhere on the screen and select "Paste".
14. Press Enter.
15. Press Ctrl (right above the keyboard) and then "D".
16. Repeat point 15 once again.
