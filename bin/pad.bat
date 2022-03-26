@ffmpeg -i "%~1" -vf "scale='min(%~2,iw)':min'(%~3,ih)':force_original_aspect_ratio=decrease,pad=%~2:%~3:(ow-iw)/2:(oh-ih)/2"  "%~n1_%~x1"
