---
tags:
  - drive-by
  - cross-origin
  - malicious-webpage
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Drive-by Compromise]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 96039dce-b8b8-421f-9719-638c9149aa5b
created_at: '2025-12-14T17:28:52.106Z'
updated_at: '2025-12-14T17:28:52.106Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Embed-Script-in-Malicious-Webpage

## Summary

This procedure creates and hosts a webpage that embeds the vulnerable JavaScript file from the target, leveraging cross-origin script loading to inject user-specific data into the victim's browser environment without triggering security restrictions.

## Description

For the Badoo issue, the malicious page uses a standard <script> tag to load the service worker JS, which runs in the context of the attacker's domain but pulls in the victim-dependent user_id. This bypasses SOP for script inclusion, as browsers allow cross-origin JS loading. The page can be disguised as legitimate content to lure logged-in Badoo users. Expected outcome: Silent execution of the script on victim visit, exposing data for extraction.

## Requirements

1. Web server to host the HTML page (e.g., Apache, Nginx)
2. Domain under attacker control
3. HTML editor for crafting the page

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP headers on third-party scripts
- Use SRI (Subresource Integrity) hashes for external scripts
- Educate users on phishing and monitor for anomalous script loads in analytics

## Objectives

1. Load the vulnerable script cross-origin
2. Ensure no blocking by browser policies
3. Set up for data extraction

## Instructions

### Step 1: Create the HTML Page

**Context**: Build the basic structure to include the target script.

Write an HTML file: `<!DOCTYPE html><html><head><title>Fake Page</title></head><body><script src="https://badoo.com/worker-scope/chrome-service-worker.js?ws=1"></script><script>/* extraction code here */</script></body></html>`.

> Save as index.html. Expected output: Valid HTML that references the external script.

### Step 2: Host and Test the Page

**Context**: Deploy and verify loading from a different origin.

Upload to your server and visit from a logged-in Badoo session. Inspect global scope in console for user_id.

> Console should show user_id variable without errors. Expected output: Script content loaded and variables accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[drive-by-compromise]]
- [[web-exploit]]
