---
tags:
  - xss
  - evernote
  - redirect
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: c0978716-3cb0-4691-964a-58f899c18760
created_at: '2025-12-14T03:47:23.557Z'
updated_at: '2025-12-14T03:47:23.557Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access Evernote Shared Note and Observe Redirect

## Summary

This procedure involves accessing a publicly shared Evernote note to observe the internal redirect to the vulnerable client/snv endpoint, setting the stage for further analysis and exploitation.

## Description

Evernote shared notes are accessible without authentication via unique URLs. Accessing one triggers a redirect to the /client/snv endpoint, which renders the note using client-side JavaScript. This step confirms the endpoint structure and prepares for JavaScript inspection. The target environment is the Evernote web app, requiring only a browser and a valid shared note URL.

## Requirements

1. Web browser with developer tools enabled
2. Valid shared note URL (e.g., from https://www.evernote.com/shard/s[SHARD_NUMBER]/sh/[NOTE_GUID]/[NOTE_KEY])
3. Internet access to Evernote domain

## Defense

Defensive measures and detection strategies:

- Monitor for unusual redirects in web application logs
- Implement Content Security Policy (CSP) to restrict script execution
- Rate-limit access to shared note endpoints

## Objectives

1. Confirm access to shared note viewer
2. Identify the /client/snv redirect endpoint
3. Gather parameters like noteGuid and noteKey for payload crafting

## Instructions

### Step 1: Navigate to Shared Note

**Context**: Load the shared note to trigger the viewer and redirect.

Open your browser and visit a shared note URL, such as `https://www.evernote.com/shard/s1/sh/[NOTE_GUID]/[NOTE_KEY]`. Enable developer tools (F12) and switch to the Network tab to capture requests.

> The page should display the note content, and a GET request to /client/snv will appear in the logs with parameters like noteGuid, noteKey, sn, and title.

### Step 2: Verify Redirect

**Context**: Confirm the endpoint and parameters for subsequent steps.

Inspect the redirected request in the Network tab. Note the full URL: `https://www.evernote.com/shard/s1/client/snv?noteGuid=[NOTE_GUID]&noteKey=[NOTE_KEY]&sn=[PREVIOUS_LINK]&title=[NOTE_TITLE]`.

> Successful verification shows the snv endpoint handling the rendering.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[evernote]]
- [[redirect]]
