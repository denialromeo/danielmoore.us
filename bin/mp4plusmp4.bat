@ffmpeg -i "%~1" -i "%~2" -filter_complex "[0:v] [0:a] [1:v] [1:a] concat=n=2:v=1:a=1 [v] [a]" -map "[v]" -map "[a]" "%~n1_.mp4"
