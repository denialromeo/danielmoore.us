---
title: Random Classical Composition
layout: post
category: fun
permalink: random-classical-composition
author: Daniel Moore
box: random-classical-recording
---

<h3 id="song-title"></h3>

{% include yt.html width='80%' embed='
<iframe id="song" frameborder="0" allowfullscreen></iframe>
' %}

<p id="description">In 2007, Matthew Rye compiled <a href="https://www.amazon.com/1001-Classical-Recordings-Must-Before/dp/0785835822"><i>1001 Classical Recordings You Must Hear Before You Die</i></a>. This&nbsp;composition was randomly chosen from his book.</p>

<p id="next-song"></p>

<a href="javascript:;" id="dropdown" target="_self">Advanced Usage Instructions</a>
<div id="instructions" style="display:none;">
    <p>You can filter the composition selection! Examples &ndash;</p>
    <ul>
        <li>
            <a target="_self" href="?artist=mozart">Compositions by Mozart.</a>
        </li>
        <li>
            <a target="_self" href="?composition=swan+lake"><i>Swan Lake</i> by Tchaikovsky.</a>
        </li>
        <li>
            <a target="_self" href="?year=^1[1-6]..">Music from the 1600's and earlier.</a>
        </li>
    </ul>
   <p>Note that each artist's name is a link to their Wikipedia page. Where available, composition names also link to Wikipedia.</p>
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
    if ("composition" in params) {
        pool = pool.filter(s => new RegExp(params.composition, "i").exec(s.split("|")[1]) !== null)
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
    iframe.src = info[3].startsWith("PL") ? `https://youtube.com/embed/playlist?list=${info[3]}` : `https://youtube.com/embed/${info[3]}`
    const wikiLink = `<a style='text-decoration:none;border-bottom:none;' href=${wiki_link(info[4])}>${info[0]}</a>`
    const songLink = info[5] == '' ? `<span>${info[1]}</span>` : `<a style='text-decoration:none;border-bottom:none;' href=${wiki_link(info[5])}>${info[1]}</a>`
    title.innerHTML = `${wikiLink} - ${songLink} (${info[2]})`
    document.title  = `${info[0]} - ${info[1]} (${info[2]})`
</script>

<br>
<br>
<br>
