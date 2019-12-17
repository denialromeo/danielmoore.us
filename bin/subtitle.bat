@python -c "import sys;print(sys.argv[1][0:-4])" %1 > temp.txt
@python -c "import sys;print(sys.argv[1][0:-4])" %2 > temp1.txt
@set /p filename0=<temp.txt
@set /p filename1=<temp1.txt
@del temp.txt
@del temp1.txt
@ffmpeg -i %2 "%filename1%.ass"
@ffmpeg -i %1 -vf ass="%filename1%.ass" "%filename0%_.mp4"
@del "%filename1%.ass"
