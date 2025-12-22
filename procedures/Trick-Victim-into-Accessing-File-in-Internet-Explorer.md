---
id: proc-uuid-003
name: Trick-Victim-into-Accessing-File-in-Internet-Explorer
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:12.830Z'
tactics:
  - '[[Collection]]'
techniques:
  - '[[JavaScript]]'
tags:
  - social-engineering
  - xss-execution
  - internet-explorer
platforms:
  - Web
tools:
  - '[[tools/modern.ie]]'
commands: []
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Trick-Victim-into-Accessing-File-in-Internet-Explorer

## Summary

This procedure involves socially engineering a victim to open the uploaded malicious file URL in Internet Explorer, triggering content-type sniffing and execution of the embedded JavaScript for stored XSS.

## Description

Once uploaded, the file URL is shared via phishing or direct link. IE's legacy sniffing interprets the ZIP-prefixed HTML as executable script, running in the site's context for session hijacking or data theft. Test in isolated VMs to avoid real harm.

## Requirements

1. Uploaded file URL from previous step
2. Victim using vulnerable IE version (e.g., IE 11)
3. Social engineering vector (email, chat)

## Defense

Defensive measures and detection strategies:

- Educate users on phishing and unknown links
- Disable legacy browsers or enforce modern ones
- Implement CSP and monitor JS execution anomalies

## Objectives

1. Induce victim to load the URL in IE
2. Trigger sniffing and payload execution
3. Achieve data exfiltration or session theft

## Instructions

### Step 1: Share the URL

**Context**: Craft a convincing message to lure the victim, e.g., "Check this shared document: https://target.com/files/xss.zip".

No command; use email or messaging tools. Ensure the link is direct to the file.

> Expected: Victim clicks and opens in IE.

### Step 2: Verify Execution

**Context**: Use a test VM with [[tools/modern.ie]] to simulate victim access.

Open the URL in the IE VM and observe.

> Expected output: Alert box or network request from payload (e.g., to attacker server for cookie theft).

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/modern.ie]]

## Tags

- [[social-engineering]]
- [[xss-execution]]
