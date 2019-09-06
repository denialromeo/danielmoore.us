@python -c "import sys;print(sys.argv[1][0:-4])" %1 > temp.txt
@set /p filename=<temp.txt
@del temp.txt
@ffmpeg -i %1 -strict -2 "%filename%.mp4"