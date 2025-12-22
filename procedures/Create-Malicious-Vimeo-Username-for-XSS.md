---
id: proc-vimeo-username-xss-001
tags:
  - xss
  - username-injection
  - vimeo
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.344Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Vimeo-Username-for-XSS

## Summary

This procedure involves registering a Vimeo account with a username containing malicious HTML/SVG code to exploit unescaped output in video thumbnails, enabling XSS injection for arbitrary JavaScript execution on viewers.

## Description

The vulnerability stems from Vimeo's failure to escape user names when rendering the 'More from [user]' text in video end thumbnails. By setting the username to '<svg onload=eval(name)></svg>', attackers can inject an SVG element that executes JavaScript from the window.name property when the thumbnail loads. This is particularly effective for short videos that end quickly, displaying the thumbnail without much delay. The attack targets both embedded players (player.vimeo.com) and the main site (vimeo.com), with varying interaction levels.

## Requirements

1. Access to a web browser and internet connection.
2. Ability to create a free Vimeo account.
3. A short video file (under 10 seconds) to upload for quick thumbnail trigger.

## Defense

Defensive measures and detection strategies:

- Implement proper HTML escaping for all user-controlled inputs in UI elements.
- Sanitize usernames during account creation to block HTML/JS tags.
- Monitor for anomalous account creations with suspicious strings like '<svg'.
- Use Content Security Policy (CSP) to restrict inline script execution.

## Objectives

1. Establish a persistent injection point via username.
2. Prepare for payload delivery through video views.
3. Enable JS execution on victim browsers viewing attacker's content.

## Instructions

### Step 1: Register Vimeo Account

**Context**: Create a new account to set the malicious username.

Navigate to vimeo.com/signup and complete registration, ensuring the username field accepts the payload.

### Step 2: Set Malicious Username

**Context**: Input the injectable SVG tag as the display name.

During profile setup, set the name to: `<svg onload=eval(name)></svg>`. Save changes.

### Step 3: Upload Short Video

**Context**: Upload a video to test thumbnail display.

Go to upload section, select a short video (<10s), and publish it publicly.

**Expected Output**: Video live; profile shows malicious name.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[vimeo]]
