---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: Inject-Malicious-Payload-into-Flickr-Group-Name
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-13T23:52:49.364Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - stored-xss
  - payload-injection
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Inject-Malicious-Payload-into-Flickr-Group-Name

## Summary

This procedure involves creating a Flickr group with a name that includes a malicious JavaScript payload, exploiting the lack of escaping in the photos_user_map.gne endpoint to store the payload for later execution.

## Description

In the context of Flickr's web application, group names are stored and displayed on the photo map page without proper HTML/JS escaping. An attacker with a standard user account can create a group, inject a payload like `<script>alert(document.cookie);</script>` into the name, and store it. When the group gains photos and the map is viewed, the payload executes in the viewer's browser, potentially stealing cookies or performing other actions. This was reported in HackerOne report #1534636 with high severity (8.2) and a $3,263 bounty.

## Requirements

1. Valid Flickr account with group creation permissions
2. Web browser for manual interaction
3. Basic knowledge of JavaScript payloads for XSS

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output escaping for all user-controlled data, especially group metadata
- Use Content Security Policy (CSP) to restrict script execution on map pages
- Monitor for anomalous group names containing script tags via automated scans

## Objectives

1. Store malicious JavaScript in Flickr group metadata
2. Prepare for reflection on the photo map page
3. Enable remote execution against viewers

## Instructions

### Step 1: Log In and Navigate to Group Creation

**Context**: Authenticate and access the group creation interface to input the payload.

Log in to Flickr at https://www.flickr.com and click on "Create" > "Group".

### Step 2: Enter Malicious Group Name

**Context**: Inject the XSS payload directly into the group name field, which is stored without escaping.

In the group name field, enter: `<script>alert('XSS via Flickr Group');</script>`. Provide a description and privacy settings as needed, then submit to create the group.

> This stores the payload server-side. No immediate execution occurs, confirming the stored nature of the vulnerability.

### Step 3: Verify Storage

**Context**: Confirm the payload is retained in the group details.

After creation, view the group settings page. The name should display the raw HTML, indicating inadequate escaping (though it may render partially here).

**Expected Output**: Group created with the injected name visible in dashboard.

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
- [[stored-xss]]
- [[flickr]]
