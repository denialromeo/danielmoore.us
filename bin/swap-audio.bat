@ffmpeg -i "%~1" -map 0:v:0 -map 0:a:1 -c copy "%~n1_%~x1"
