@pushd .
@cd "C:\Users\hi\Desktop\code\export-saved-reddit"
dir
@python export_saved.py
@popd
@cd "C:\Users\hi\Desktop\code\export-saved-reddit"
@copy /y "C:\Users\hi\Desktop\code\export-saved-reddit\export-saved.html" "C:\Users\hi\Desktop\code\danielmoore.us"
@exit
