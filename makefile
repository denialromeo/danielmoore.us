SHELL=cmd

# If no commit message given, use date as commit message.
ifeq ($(m),)
m = $$(date)
endif

r remote g github: wincred
	git pull origin master
	jekyll build
	git add --all .
	git commit --allow-empty -m "Commit."
	git push origin master --force
	cd _site &&\
	git pull origin master &&\
	git add --all . &&\
	git commit --allow-empty -m "Commit." &&\
	git push origin master
	del /s /q *~
	clear

wincred:
	git config credential.helper wincred
	git config user.name "Daniel Moore"
	git config user.email "hi@danielmoore.us"

l local:
	jekyll build
	jekyll serve --incremental --port 8000
	
i init:
	mkdir _site &&\
	cd _site &&\
	git init &&\
	git remote add origin https://github.com/denialromeo/denialromeo.github.io.git &&\
	git pull origin master

gems:
	gem install jekyll jekyll-last-modified-at jekyll-seo-tag

e eject:
	powershell "(new-object -COM Shell.Application).NameSpace(17).ParseName('D:').InvokeVerb('Eject')"

b:
	cp ..\code\borders-quiz\dist\borders-quiz.js .\js

s:
	cp ..\code\random-acclaimed-song\songs.js .\js

chess:
	cp ..\4462-chess-problems\dist\chess-puzzle-player.js .\js

tv:
	dir /a-d /b a:\movies > tv.txt
	git diff
