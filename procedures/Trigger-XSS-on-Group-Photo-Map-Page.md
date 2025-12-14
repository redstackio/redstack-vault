---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Trigger-XSS-on-Group-Photo-Map-Page
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-13T23:52:49.359Z'
tactics:
  - '[[Execution]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - execution-trigger
  - web
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

# Trigger-XSS-on-Group-Photo-Map-Page

## Summary

This procedure triggers the stored XSS payload by directing a user to load the Flickr group photo map page, where the unescaped group name causes JavaScript execution in the viewer's browser.

## Description

Once the payload is stored in the group name via the photos_user_map.gne endpoint, adding photos to the group enables the map view. Loading this page reflects the group name without escaping, executing the script. This affects any authenticated or public viewer, leading to potential impacts like session theft. Discovered by keer0k and reported on April 8, 2022.

## Requirements

1. Flickr group with stored XSS payload and at least one photo
2. Victim access to the group map URL
3. Browser on victim side to render the page

## Defense

Defensive measures and detection strategies:

- Escape all outputs on dynamic pages like maps using HTML entity encoding
- Implement JS sandboxing or strict CSP headers
- Log and alert on map page loads for groups with suspicious names

## Objectives

1. Cause reflection of the stored payload on the map page
2. Execute JavaScript in the victim's context
3. Demonstrate impact such as cookie access or phishing

## Instructions

### Step 1: Add Photo to Enable Map

**Context**: The map feature requires group photos; add one to activate the endpoint.

Log in as the group owner, upload a photo to the group via the web interface.

### Step 2: Generate and Share Map URL

**Context**: Obtain the URL that triggers the vulnerable endpoint.

Navigate to the group's photos page and access the map view, or construct the URL: https://www.flickr.com/groups/[group-id]/map. Share this link with the victim (e.g., via email or social engineering).

### Step 3: Observe Execution

**Context**: Victim loads the page, triggering the payload.

When the victim visits the URL, the group name renders on the map, executing the script (e.g., alert box appears).

> Monitor browser dev tools on victim side for console output confirming execution, such as logged document.cookie.

**Expected Output**: Malicious script runs, e.g., alert dialog or network requests from payload.

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
- [[trigger]]
- [[flickr-map]]
