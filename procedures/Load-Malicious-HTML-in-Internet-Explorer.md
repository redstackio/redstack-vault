---
id: proc-004
tags:
  - javascript-interception
  - ie-exploit
type: procedure
tools:
  - '[[tools/Internet-Explorer]]'
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Windows
  - Internet Explorer
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[DLL Search Order Hijacking]]'
updated_at: '2025-12-14T17:29:36.206Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[DLL Search Order Hijacking]]'
---
# Load Malicious HTML in Internet Explorer

## Summary

This procedure involves navigating to the malicious HTML page in Internet Explorer, where the JavaScript intercepts String.indexOf calls from Kaspersky's script to access and manipulate its internal namespace and commands.

## Description

The disable_features2.html file contains code that overrides String.prototype.indexOf, allowing it to monitor and hijack calls made by Kaspersky's injected script. This grants access to the AV's command interface, enabling feature disabling and potential RCE. The fake Google domain ensures script injection.

## Requirements

1. Internet Explorer with Kaspersky add-on installed
2. Local HTTPS server running on port 5000
3. Hosts file modified for domain redirect

## Defense

Defensive measures and detection strategies:

- Disable legacy browsers like IE or use Enhanced Protected Mode
- Monitor JS prototype modifications via browser dev tools or extensions
- Kaspersky updates to safeguard prototype methods

## Objectives

1. Deliver and execute intercepting JavaScript
2. Hijack Kaspersky's method calls for namespace access
3. Issue unauthorized commands like feature disable

## Instructions

### Step 1: Launch IE

**Context**: Start the vulnerable browser.

Open Internet Explorer, ensuring Kaspersky add-on is active (check extensions).

> Expected: IE launches; add-on icon visible.

### Step 2: Navigate and Override Cert

**Context**: Load the page and bypass security warning.

Enter URL https://www.google.example.com:5000/disable_features2.html and click through the invalid certificate warning.

> Expected: Page loads; JS executes silently, intercepting calls.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript
- [[DLL Search Order Hijacking]] Hijack Execution Flow: DLL Search Order Hijacking (JS prototype)

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Internet-Explorer]]

## Tags

- [[javascript-interception]]
- [[ie-exploit]]
