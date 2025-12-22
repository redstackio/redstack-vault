---
type: code
language: HTML
verified: true
tags:
  - csrf
  - payload
  - html
platforms:
  - Web
validated: true
---

# HTML-IMG-CSRF-Payload-for-Username-Change

## Code

```html
<img src="http://www.example.com/api/setusername?username=CSRFd">
```

## Description

This HTML code snippet uses an image tag to perform a CSRF attack by automatically sending a GET request to a vulnerable endpoint when loaded in the victim's browser. It disguises the malicious action as a harmless image fetch, exploiting the browser's inclusion of session cookies for the target domain. The payload targets username modification but can be adapted for other state-changing GET requests.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Target URL (in src) | The vulnerable endpoint URL on the target site | `http://www.example.com/api/setusername` |
| username parameter | The value to set for the username (or other action parameter) | `CSRFd` |

## Usage

Embed this snippet in an attacker-controlled HTML page, email, or resource that the victim visits while authenticated to the target site. For example, host it as part of a phishing page: wrap it in a full <html> document and link to it. The request fires immediately upon page load, requiring no victim interaction.

## Detection

- Web application logs showing state changes from unexpected referers or user agents.
- Browser developer tools revealing suspicious img src requests to internal APIs.
- Absence of CSRF tokens in request headers; implement Content-Security-Policy to block inline scripts or suspicious loads.
- Network monitoring for cross-origin requests lacking proper validation.

## Related

- [[procedures/CSRF-Attack-via-HTML-GET-Payload]]
