---
id: proc-uuid-public-execution
tags:
  - xss
  - execution
  - public-access
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:47.246Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Access-Public-Permalink-to-Execute-Payload

## Summary

This procedure accesses the public permalink of the injected post to trigger XSS execution, confirming the vulnerability affects unauthenticated users.

## Description

After injection, the permalink renders the post_title in the public view without escaping, executing the JavaScript. This simulates a drive-by attack where visitors run arbitrary code, potentially leading to session theft. Tested on a host like alwaysdata.net, it results in an alert popup.

## Requirements

1. Generated permalink from injected post
2. Public access to the WordPress site (no auth needed)
3. Browser to observe execution

## Defense

Defensive measures and detection strategies:

- Escape all user inputs in public templates using esc_js() or equivalent
- Deploy XSS protection via browser extensions or WAF rules
- Log and monitor unusual JavaScript errors on public pages

## Objectives

1. Load permalink as unauthenticated user
2. Observe payload execution
3. Validate impact on client-side

## Instructions

### Step 1: Obtain Permalink

**Context**: Retrieve the URL post-publication.

From the post editor, copy the permalink, such as http://diaa.alwaysdata.net/wordpress/?tggr-tweets=alerta7a.

> Permalink includes the tainted title in parameters.

### Step 2: Visit and Execute

**Context**: Trigger the reflection.

Open the permalink in a new browser tab or incognito mode (to simulate public user). The page loads, and the script executes.

> Alert "a7a" pops up, confirming XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
