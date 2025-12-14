---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - csrf
  - html
  - deeplink
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:27:57.404Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Create-HTML-Page-with-Periscope-Deeplink-for-CSRF

## Summary

This procedure creates an HTML page embedding a deeplink to exploit CSRF in the Periscope iOS app's follow action, allowing attackers to force follows via clickable links.

## Description

By embedding the deeplink `pscp://user/<user-id>/follow` in an HTML anchor tag, the page can be served to victims. When clicked on an iOS device with the Periscope app installed and logged in, it triggers the app to perform the follow without confirmation. This leverages the app's lack of CSRF protection for URI schemes, enabling unauthorized actions through social engineering.

## Requirements

1. Text editor to create HTML file
2. Target user ID for the deeplink
3. iOS device for testing the link

## Defense

Defensive measures and detection strategies:

- Add confirmation prompts for deeplink actions in the app
- Use CSRF tokens or state checks in URI handling
- Browser policies to warn on custom URI schemes
- Log and alert on anomalous app launches from links

## Objectives

1. Build an HTML payload with clickable deeplink for CSRF
2. Trigger unauthorized follow via browser interaction
3. Enable web-based delivery of the exploit

## Instructions

### Step 1: Construct the HTML Content

**Context**: Write the basic HTML structure with the malicious link.

Create a file named `csrf-demo.html` containing:

```html
<html><body><a href="pscp://user/periscopeco/follow">CSRF DEMO</a></body></html>
```

Replace `periscopeco` with any target user ID.

**Expected Output**: Valid HTML file with the anchor tag.

### Step 2: Test the Link Locally

**Context**: Open the HTML in a browser on the target iOS device to verify.

Open the file in Safari or another browser. Click the link; it should attempt to open the Periscope app and execute the follow.

**Expected Output**: App opens and follows the user silently.

### Step 3: Customize for Delivery

**Context**: Enhance the page to disguise the link if needed.

Add styling or text to make it look legitimate, e.g., "Click to follow cool profile!".

**Expected Output**: Disguised HTML ready for hosting.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[html]]
- [[deeplink]]
