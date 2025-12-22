---
id: proc-001
tags:
  - kaspersky
  - setup
type: procedure
tools:
  - '[[tools/Internet-Explorer]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:29:36.237Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Enable Kaspersky Anti-Banner and Private Browsing

## Summary

This procedure activates the Anti-Banner and Private Browsing features in Kaspersky Internet Security to ensure the Web protection script is loaded and vulnerable to JavaScript interception in Internet Explorer.

## Description

Kaspersky's Web protection injects scripts into browser pages for domains matching certain patterns, such as Google sites. Enabling these features primes the environment for the exploit by ensuring the script runs in the browser context, where String.prototype.indexOf calls can be intercepted. This step is a prerequisite for triggering the vulnerability without altering core AV settings prematurely.

## Requirements

1. Kaspersky Internet Security installed and licensed on Windows
2. Administrative access to Kaspersky settings
3. Internet Explorer as the target browser

## Defense

Defensive measures and detection strategies:

- Regularly audit Kaspersky settings for unexpected changes
- Use browser extensions or policies to restrict add-on script execution
- Monitor for unauthorized feature toggles in AV logs

## Objectives

1. Activate Web protection features to load injectable scripts
2. Verify script presence in browser context
3. Prepare for domain-specific injection on Google-like hostnames

## Instructions

### Step 1: Access Kaspersky Settings

**Context**: Open the Kaspersky configuration to navigate to Web protections.

No command required; use the system tray icon or Start menu to launch Kaspersky settings. Go to "Protection" > "Web Anti-Virus" or similar section.

> Expected: Settings interface loads without errors.

### Step 2: Enable Features

**Context**: Toggle the specific features to enable script injection.

Navigate to Anti-Banner and Private Browsing options. Check the boxes to enable them, then apply and save changes.

> Expected: Status updates to "Enabled"; restart browser if prompted.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Internet-Explorer]]

## Tags

- [[kaspersky]]
- [[setup]]
