@ffmpeg -i "%~2" "%~n2.ass"
@ffmpeg -i "%~1" -vf ass="%~n2.ass" "%~n1_.mp4"
@del "%~n2.ass"
