# If no commit message given, use date as commit message.
ifeq ($(m),)
m = $$(date)
endif

r remote g github: wincred
	jekyll build
	git add --all .
	git commit -m "$m"
	git push origin master --force 
	cd _site &&\
	git add --all . &&\
	git commit -m "$m" &&\
	git push origin master --force &&\
	del /s /q *~
	clear

wincred:
	git config --global credential.helper wincred
	git config --global user.name "Daniel Moore"
	git config --global user.email "hi@danielmoore.us"

l local:
	jekyll build
	jekyll serve --incremental --port 8000
	
i init:
	jekyll build
	cd _site &&\
	git init &&\
	git remote add origin https://github.com/denialromeo/denialromeo.github.io.git

gems:
	gem install jekyll jekyll-last-modified-at jekyll-seo-tag

e eject:
	powershell "(new-object -COM Shell.Application).NameSpace(17).ParseName('D:').InvokeVerb('Eject')"

b:
	cp ..\code\borders-quiz\dist\borders-quiz.js .\js

s:
	cp ..\code\random-acclaimed-song\songs.js .\js

chess:
	cp ..\code\4462-chess-problems\chess-puzzle-player\dist\chess-puzzle-player.js .\js
