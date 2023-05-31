---
title: Random Classical Recording
description: Listen to 10,272 top-rated songs!
layout: post
category: fun
permalink: random-classical-recording
author: Daniel Moore
box: random-acclaimed-song
---

<h3 id="song-title"></h3>

{% include yt.html width='80%' embed='
<iframe id="song" frameborder="0" allowfullscreen></iframe>
' %}

<p id="description">In 2007, music critic Matthew Rye and cellist Steven Isserlis published <a href="https://www.amazon.com/1001-Classical-Recordings-Must-Before/dp/0785835822"><i>1001 Classical Recordings You Must Hear Before You Die</i></a>. This recording was randomly chosen from their book.</p>

<p id="next-song"></p>

<a href="javascript:;" id="dropdown" target="_self">Advanced Usage Instructions</a>
<div id="instructions" style="display:none;">
    <p>You can filter the recording selection! Examples &ndash;</p>
    <ul>
        <li>
            <a target="_self" href="?song=requiem&artist=mozart"><i>Requiem</i> by Mozart.</a>
        </li>
        <li>
            <a target="_self" href="?year=17..">Recordings from the 1700's.</a>
        </li>
    </ul>
   <p>Also note that each artist's name is a link to their Wikipedia page.</p>
</div>

<script src="/js/URI.js"></script>
<script src="/js/classical.js"></script>
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
    var pool = classical
    var regex = ""
    try {
    if ("artist" in params) {
        pool = pool.filter(s => new RegExp(params.artist, "i").exec(s.split("|")[0]) !== null)
    }
    if ("song" in params) {
        pool = pool.filter(s => new RegExp(params.song, "i").exec(s.split("|")[1]) !== null)
    }
    if ("year" in params) {
        pool = pool.filter(s => new RegExp(params.year, "i").exec(s.split("|")[2]) !== null)
    }
    if ("genre" in params) {
        pool = pool.filter(s => new RegExp(params.genre, "i").exec(s.split("|")[6]) !== null)
    }
    } catch (e) { }
    if (pool.length === 0) { pool = classical }
    if (pool.length !== classical.length) {
        pool.sort()
        console.log(pool.map(s => s.split("|").slice(0,3).concat(s.split("|").slice(6,7))))
    }
    const info = choice(pool).split("|")
    const infoLog = info.slice(0,3).concat(info.slice(6,7))
    for (let i = 0; i < infoLog.length; i++) { console.log(infoLog[i]) }
    iframe.src = info[3].startsWith("http") ? info[3] : `https://youtube.com/embed/${info[3]}`
    const wikiLink = `<a style='text-decoration:none;border-bottom:none;' href=${wiki_link(info[4])}>${info[0]}</a>`
    // const songLink = `${info[1]}<a style='text-decoration:none;border-bottom:none;' href='http://acclaimedmusic.net/song/${info[5]}.htm'></a>`
    const songLink = info[1]
    title.innerHTML = `${wikiLink} - ${songLink} (${info[2]})`
    document.title  = `${info[0]} - ${info[1]} (${info[2]})`
</script>

<br>
<br>
<br>
