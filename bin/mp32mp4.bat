rem @python -c "import sys;print(sys.argv[1][0:-4])" %1 > temp.txt
rem @set /p filename=<temp.txt
rem @del temp.txt
@ffmpeg -loop 1 -i "%~2" -i "%~1" -c:a copy -c:v libx264 -shortest "%~n1.mp4"
