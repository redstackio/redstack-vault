---
tags:
  - xss
  - session-hijacking
  - exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:53.379Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: cced62c4-3830-4391-b896-0d64411f91cf
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-for-Session-Hijacking

## Summary

This procedure triggers the stored XSS payload in the VK.com video selection feature by inducing victim interaction, executing JavaScript to steal session cookies and enable account takeover or data exfiltration.

## Description

Once the payload is stored via the injection procedure, it executes in the browser context of any authenticated user who views the affected video box. The JavaScript can access the DOM, steal cookies, and send them to an attacker-controlled endpoint. This leads to high-impact attacks like impersonating users to post content, access private data, or spread further malware. The attack relies on social engineering to get victims to interact with the video.

## Requirements

1. Successfully injected payload from prior procedure
2. Attacker server to receive exfiltrated data (e.g., simple HTTP listener)
3. Victim accounts on VK.com to target

## Defense

Defensive measures and detection strategies:

- Sanitize all stored outputs with context-aware encoding
- Implement user session validation and anomaly detection (e.g., unusual login locations)
- Log and alert on unexpected outbound requests from client-side scripts
- Educate users on phishing risks involving shared media

## Objectives

1. Execute the stored payload in victim browsers
2. Exfiltrate sensitive session data
3. Use stolen sessions for unauthorized actions

## Instructions

### Step 1: Share Manipulated Video

**Context**: Distribute the video containing the stored payload to potential victims.

Post the video to a group, send via messages, or make it publicly viewable to encourage interactions with the selection box.

### Step 2: Monitor for Trigger

**Context**: Wait for victims to view the video box, triggering payload execution.

Use browser dev tools on a test account to simulate: Load the video page and observe if the script executes (e.g., network request to attacker domain).

### Step 3: Receive and Validate Exfiltrated Data

**Context**: Capture incoming requests on the attacker server containing victim cookies.

Set up a listener (e.g., using netcat or a web server) on http://attacker.com/log. Upon trigger, expect GET requests with query params like ?cookie=session_token%3Dabc123.

**Expected Output**: Stolen cookies received, allowing replay in a browser.

### Step 4: Exploit Hijacked Session

**Context**: Use the stolen session to impersonate the victim.

Paste the cookie into a browser's dev tools (Application > Cookies) and refresh VK.com to gain access as the victim, performing actions like viewing private profiles.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss-trigger
- session-theft
- web-exploitation
