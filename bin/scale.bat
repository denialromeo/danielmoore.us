@ffmpeg -i "%~1" -vf "scale=%~2:%~3:force_original_aspect_ratio=decrease,pad=%~2:%~3:(ow-iw)/2:(oh-ih)/2" "%~n1_%~x1"
