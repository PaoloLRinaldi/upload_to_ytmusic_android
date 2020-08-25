import os
import subprocess
from time import gmtime, asctime
import sys
from ytmusicapi import YTMusic


def first_time_file(filename, message):
	'''
	Retrieve infos from a file. If the file
	doesn't exist it asks the user for this
	infos and store them in the file.
	'''
	try:
		f = open(filename, 'r')
	except:
		ret = input(message)
		f = open(filename, 'w')
		f.write(ret)
	else:
		ret = f.read()
	finally:
		f.close()
	return ret

# The path where this script is located
static_path = os.path.dirname(os.path.abspath(__file__)) + '/'

# Authentication
try:
	ytmusic = YTMusic(static_path + 'headers_auth.json')

except:
	rmfile = input('Authentication failed. Maybe two years have passed and you should generate \"headers_auth.json\" again.\nRemove \"headers_auth.json\"? [y/n]: ')
	if rmfile == 'y':
		os.remove(static_path + 'headers_auth.json')
	sys.exit('Aborting. Check your internet connection or try to regenerate the \"headers_auth.json\" file.')


# Get music path
good_music_path = False
while(not good_music_path):
	# Retrieve path
	music_dir = first_time_file(static_path + 'music_dir.txt', 'Insert the folder where you store your music: ')

	# Check if the path is valid
	try:
		os.chdir(music_dir)
	except:
		good_music_path = False
		os.remove(static_path + 'music_dir.txt')
		sys.stderr.write('Path does not exist, insert again.\n')
	else:
		good_music_path = True


# Arguments (2 options):
# UploadToYTMusic.py 'the divisor' [list of numbers of the songs to choose (separated by space). 0 is the newest]
# or
# UploadToYTMusic.py

# If arguments are passed the script will behave as a no-input program
quiet = len(sys.argv) > 1
if quiet:  # not quiet = normal program
	divisor = sys.argv[1]  # The string used to separate the output infos of the scirpt

# Store songs names
files = filter(os.path.isfile, os.listdir(music_dir))  # get file list
files = [os.path.join(music_dir, f) for f in files]  # add path to each file
accepted_formats = ['mp3', 'm4a', 'wma']
files = list(filter(lambda x: any([x.endswith('.' + frmt) for frmt in accepted_formats]), files))  # get music only
files.sort(key=lambda x: os.path.getmtime(x), reverse=True)  # sort by time
barefiles = [x.split("/")[-1] for x in files]  # files without path

if not quiet:
	for i in range(len(files) - 1, -1, -1):
		print("{0}\t{1}\n{2}\n".format(i, asctime(gmtime(os.path.getmtime(files[i]))), barefiles[i]))

	inp = str(input("Choose songs numbers (separeted by Space):\n"))
	inp = inp.split(" ")
else:
	inp = sys.argv[2:]

# Interpret the input list of numbers as list of integers
inp = [int(x) for x in inp if not (x == "")]

if not quiet:
	print("Upload started...\n")

success_count = 0  # Number of successfully uploaded songs
success = []  # List of successfully uploaded songs
already = []  # List of songs already uploaded
failed = []  # List of songs which failed to be uploaded

# The part of the code where the songs are uploaded
for i in range(len(inp)):
	if not quiet:
		print("Uploading {}".format(barefiles[inp[i]]))
	try:
		res = ytmusic.upload_song(files[inp[i]])  # Upload the current song
	except Exception as e:
		res = str(e)

	if res != "STATUS_SUCCEEDED":  # If failed
		if '<Response [409]>' == str(res):
			if not quiet:
				print("You have already uploaded this song")
			success_count += 1
			already.append(files[inp[i]])
		else:
			failed.append(files[inp[i]])
			if not quiet:
				print("Failed to upload the song. Reason: {}".format(res))
	elif res == 'STATUS_SUCCEEDED':  # If succeeded
		success_count += 1
		success.append(files[inp[i]])
		if not quiet:
			print("Song successfully uploaded!")
	elif not quiet:  # Useless condition. It should never happen
		print("Something went wrong. Printing output:")
		print(out2)
		print("End of output")

        # Print progress
	if not quiet:
		print("{0}/{1} songs uploaded until now. Total = {2}\n".format(success_count, i + 1, len(inp)))

if not quiet:
	print("*************** DONE ****************")
	if len(failed) != 0:
		print("Couldn't upload following songs:")
		for i in range(len(failed)):
			print(failed[i])
	print("\n\n")
	print("Press Enter to exit")
	input()
else:
	print('Successfully uploaded songs', end='')
	for a in success:
		print(f'{divisor}{a}', end='')

	print(f'{divisor}{divisor}', end='')

	print('Already uploaded songs', end='')
	for a in already:
		print(f'{divisor}{a}', end='')

	print(f'{divisor}{divisor}', end='')

	print('Unsuccessfully uploaded songs', end='')
	for a in failed:
		print(f'{divisor}{a}', end='')
