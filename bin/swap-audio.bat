@ffmpeg -i "%~1" -strict -2 -map 0:v:0 -map 0:a:1 "%~n1_.mp4"
