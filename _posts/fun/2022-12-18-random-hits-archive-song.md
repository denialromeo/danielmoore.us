---
title: Random Hits Archive Song
description: Listen to thousands of top hits!
layout: post
category: fun
permalink: random-hits-archive-song
author: Daniel Moore
box: random-hits-archive-song
---

<h3 id="song-title"></h3>

{% include yt.html width='80%' embed='
<iframe id="song" frameborder="0" allowfullscreen></iframe>
' %}

<p id="description">Since 2019, Bob Moke has maintained Hits Archive, a set of YouTube channels dedicated to major U.S. hits released between 1905 and 1975. This song was randomly chosen from his channels.</p>

<p id="next-song"></p>

<a href="javascript:;" id="dropdown" target="_self">Advanced Usage Instructions</a>
<div id="instructions" style="display:none;">
    <p>You can filter the song selection! Examples &ndash;</p>
    <ul>
        <li>
            <a target="_self" href="?year=19[2-3][0-9]">Songs released in the 1920's and 1930's.</a>
        </li>
        <li>
            <a target="_self" href="?artist=Glenn Miller">Songs by Glenn Miller.</a>
        </li>
    </ul>
</div>

<script src="/js/URI.js"></script>
<script src="/js/hits-archive.js"></script>
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
    var pool = songs
    var regex = ""
    try {
    if ("artist" in params) {
        pool = pool.filter(s => new RegExp(params.artist, "i").exec(s.split("|")[2]) !== null)
    }
    if ("song" in params) {
        pool = pool.filter(s => new RegExp(params.song, "i").exec(s.split("|")[2]) !== null)
    }
    if ("year" in params) {
        pool = pool.filter(s => new RegExp(params.year, "i").exec(s.split("|")[1]) !== null)
    }
    } catch (e) { }
    if (pool.length === 0) { pool = songs }
    if (pool.length !== songs.length) {
        pool.sort()
        console.log(pool.map(s => s.split("|").slice(0,3).concat(s.split("|").slice(6,7))))
    }
    const info = choice(pool).split("|")
    iframe.src = `https://youtube.com/embed/${info[0]}`
    title.innerHTML = `${info[2]} (${info[1]})`
    document.title  = `${info[2]} (${info[1]})`
</script>

<br>
<br>
<br>
