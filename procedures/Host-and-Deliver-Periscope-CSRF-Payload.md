---
id: d4e5f6g7-h8i9-0123-defg-456789012345
tags:
  - csrf
  - hosting
  - payload-delivery
type: procedure
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:27:57.399Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Host-and-Deliver-Periscope-CSRF-Payload

## Summary

This procedure hosts the HTML POC or uses data URIs to deliver the Periscope CSRF payload, tricking victims into clicking and triggering the unauthorized follow action.

## Description

Hosting the HTML page locally or using data URIs allows delivery of the deeplink payload. Victims are social-engineered into clicking while the Periscope app is installed and logged in on iOS. Direct data URIs may fail in Safari, so hosting is preferred. This completes the CSRF chain by executing the exploit without user awareness.

## Requirements

1. Local server capability (e.g., Python or Node.js)
2. Delivery channel (email, messaging, website)
3. Victim with Periscope app open and logged in

## Defense

Defensive measures and detection strategies:

- App updates to include deeplink validation and confirmations
- User training on suspicious links and QR scans
- Network monitoring for unusual app URI invocations
- Browser extensions to block custom schemes

## Objectives

1. Make the payload accessible for victim interaction
2. Execute the CSRF follow via delivery
3. Achieve unwanted subscription without consent

## Instructions

### Step 1: Prepare Hosting Option

**Context**: Choose between data URI or local server for delivery.

For data URI: `data:text/html,<html><a href="pscp://user/periscopeco/follow">CSRF DEMO</a></html>`.

For hosting: Save HTML as `index.html`.

**Expected Output**: Payload in deliverable format.

### Step 2: Start Local Server

**Context**: Host the HTML if data URI is unreliable.

Use Python: Navigate to the directory and run:

```bash
python -m http.server 8000
```

Access via `http://localhost:8000` or IP for remote.

> This starts a simple HTTP server. Note: Data URIs often fail in Safari for custom schemes; use hosted version.

**Expected Output**: Server running, page accessible at the URL.

### Step 3: Deliver to Victim

**Context**: Send the link or QR to the target via social engineering.

Share the hosted URL or data URI in an email/message, e.g., "Check this cool Periscope demo!" Ensure victim clicks while app is logged in.

**Expected Output**: Victim interacts, app follows the profile.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[hosting]]
- [[payload-delivery]]
