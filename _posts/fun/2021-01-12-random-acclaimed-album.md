---
title: Random Acclaimed Album
description: Listen to 3,000 top-rated albums!
layout: post
category: fun
permalink: random-acclaimed-album
author: Daniel Moore
box: random-acclaimed-song
---

<h3 id="song-title"></h3>

{% include yt.html width='80%' embed='
<iframe id="song" frameborder="0" allowfullscreen></iframe>
' %}

<p id="description">Since 2001, statistician Henrik Franzon has maintained <a href="http://acclaimedmusic.net">acclaimedmusic.net</a>, his ranking of the top&#8209;rated albums of all time. This album was randomly chosen from his <a href="http://www.acclaimedmusic.net/year/alltime_albums.htm">list</a> of 3,000 albums.</p>

<p id="next-song"></p>

<a href="javascript:;" id="dropdown" target="_self">Advanced Usage Instructions</a>
<div id="instructions" style="display:none;">
    <p>You can filter the album selection! Examples &ndash;</p>
    <ul>
        <li>
            <a target="_self" href="?year=19[6-7][0-9]">Albums released in the 1960's and 1970's.</a>
        </li>
        <li>
            <a target="_self" href="?artist=Bob+Marley|The.Wailers">Albums by Bob Marley.</a>
        </li>
        <li>
            <a target="_self" href="?album=love">Albums whose titles contain the word "love".</a>
        </li>
        <li>
            <a target="_self" href="?genre=disco&year=197.">Disco albums from the 1970's.</a>
        </li>
    </ul>
   <p>Also note that each album's name is a link to its Wikipedia page. To see an album's genres, hit <code class="language-plaintext highlighter-rouge">Ctrl + Shift + J</code> to open the browser console.</p>
</div>

<script src="/js/URI.js"></script>
<script src="/js/albums.js"></script>
<script>
    const is_firefox = typeof(InstallTrigger) !== "undefined"
    const next_song = document.querySelector("#next-song")
    next_song.innerHTML = is_firefox ? `Click <a href='${window.location.href}' target='_self'>here</a> for another!` : "Refresh the page for another!"

    function random(x) { return Math.floor(x * Math.random()) }
    function choice(a) { return a[random(a.length)] }
    function wiki_link(title) {
        if (title.startsWith("http")) {
            return title
        }
        const escaped = title.replace(/ /g, "_").replace(/'/g, "&#39;")
        return `https://en.wikipedia.org/wiki/${escaped}`
    }
    const iframe = document.querySelector("#song");
    const title = document.querySelector("#song-title");
    const params = new URI(window.location.href).search(true)
    var pool = albums
    var regex = ""
    try {
    if ("artist" in params) {
        pool = pool.filter(s => new RegExp(params.artist, "i").exec(s.split("|")[0]) !== null)
    }
    if ("album" in params) {
        pool = pool.filter(s => new RegExp(params.album, "i").exec(s.split("|")[1]) !== null)
    }
    if ("year" in params) {
        pool = pool.filter(s => new RegExp(params.year, "i").exec(s.split("|")[2]) !== null)
    }
    if ("genre" in params) {
        pool = pool.filter(s => new RegExp(params.genre, "i").exec(s.split("|")[7]) !== null)
    }
    } catch (e) { }
    if (pool.length === 0) { pool = albums }
    if (pool.length !== albums.length) {
        pool.sort()
        console.log(pool.map(s => s.split("|").slice(0,3).concat(s.split("|").slice(7,8))))
    }
    const info = choice(pool).split("|")
    const infoLog = info.slice(0,3).concat(info.slice(7,8))
    for (let i = 0; i < infoLog.length; i++) { console.log(infoLog[i]) }
    iframe.src = info[3].startsWith("http") ? info[3] : `https://youtube.com/embed/playlist?list=${info[3]}`
    const wikiLink = `<a style='text-decoration:none;border-bottom:none;' href=${wiki_link(info[0])}>${info[0]}</a>`
    const songLink = `<a style='text-decoration:none;border-bottom:none;' href=${wiki_link(info[5])}>${info[1]}</a>`
    const artistLink = `<a style='text-decoration:none;border-bottom:none;' href=${wiki_link(info[6])}>${info[0]}</a>`
    // const songLink = `<a style='text-decoration:none;border-bottom:none;' href='http://acclaimedmusic.net/album/${info[4]}.htm'>${info[1]}</a>`
    title.innerHTML = `${artistLink} - ${songLink} (${info[2]})`
    document.title  = `${info[0]} - ${info[1]} (${info[2]})`
</script>

<br>
<br>
<br>
