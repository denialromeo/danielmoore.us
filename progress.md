---
layout: page
title: Progress
date: Nov 16 2016
photoswipe: true
permalink: progress
ps_dim: 500x500
modifiedMsg: false
---

<center><img src="https://www.fundraisingbrick.com/thermometer/thermgenerate.php?goal=1000000&current=587000&color=green&label=3" width="400" height="600"/></center>

<br>
<br>
{% include yt.html width='77%' embed='
<iframe width="560" height="315" src="https://www.youtube.com/embed/yURRmWtbTbo" frameborder="0" gesture="media" allow="encrypted-media" allowfullscreen></iframe>
' %}
<br>

```javascript
function yearsUntilDepletion(principal, returnRate, expenses) {
  returnRate /= 100;
  let years = 1;
  while (principal > 0) {
    principal += principal * returnRate - expenses;
    console.log(`${years}, ${principal}`);
    years++;
    if (years > 33) { break; }
  }
  return years;
}
// Sample use: yearsUntilDepletion(500000, 5, 30000);
// Remember, no point remaining in U.S. past age 60. Healthcare mafia.
```