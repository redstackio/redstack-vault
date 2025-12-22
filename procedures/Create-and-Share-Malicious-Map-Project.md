---
id: proc-uuid-4
tags:
  - project-creation
  - sharing
  - session-hijacking
  - cookie-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
updated_at: '2025-12-14T03:16:30.249Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[LLMNR-NBT-NS Poisoning and SMB Relay]]'
---
---

# Create-and-Share-Malicious-Map-Project

## Summary

This procedure creates a new Mapbox project using the malicious style, configures it, and generates a shareable URL that triggers XSS execution for session hijacking and data exfiltration.

## Description

On Mapbox.com, a project is built around the uploaded style, embedding the XSS in the attribution control. Sharing the URL lures victims to load the page, executing JS to steal cookies or manipulate the session. Targets Mapbox.com dashboard; outcomes include full browser control on victim side. Requires logged-in access to Mapbox.com.

## Requirements

1. Uploaded malicious style visible in Mapbox.com Styles
2. Victim targeting (e.g., via phishing)
3. Access to https://www.mapbox.com/

## Defense

Defensive measures and detection strategies:

- Sanitize attribution rendering in project views
- Warn users about untrusted shared projects
- Monitor for JS alerts or cookie access in browser dev tools

## Objectives

1. Integrate malicious style into a live project
2. Generate exploitable share URL
3. Achieve XSS execution on victim access

## Instructions

### Step 1: Log In and Select Style

**Context**: Access the web dashboard to use the uploaded style.

Visit https://www.mapbox.com/, log in, go to 'Styles', expand the malicious style, and click 'New project'.

> Expected output: Project editor opens with the style loaded; XSS may trigger here if preview renders attribution.

### Step 2: Configure and Save Project

**Context**: Finalize settings to make the project functional.

Set basic parameters like zoom levels or center coordinates, then save the project.

> Expected output: Project saved with a unique ID.

### Step 3: Share Project URL

**Context**: Distribute the URL to victims for exploitation.

Navigate to https://www.mapbox.com/projects/, find the project, and copy the share URL (e.g., https://api.tiles.mapbox.com/v4/[style-id]/page.html?access_token=[token]#3/0.00/0.00).

> Expected output: URL ready; test in incognito to verify alert(document.cookie) fires.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[LLMNR-NBT-NS Poisoning and SMB Relay]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[session-hijacking]]
- [[cookie-theft]]

