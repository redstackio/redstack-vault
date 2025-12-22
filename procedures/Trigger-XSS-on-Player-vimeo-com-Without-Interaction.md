---
id: proc-trigger-player-xss-001
tags:
  - xss
  - no-interaction
  - iframe
  - vimeo
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:14.340Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-on-Player-vimeo-com-Without-Interaction

## Summary

This procedure demonstrates executing the XSS payload on Vimeo's embedded player (player.vimeo.com) without any user interaction beyond loading the page, by waiting for the short video to end and the thumbnail to render the malicious username.

## Description

When the HTML file loads the iframe with the attacker's video, the player starts automatically or on load. After ~10 seconds, the video ends, showing the 'More from [user]' thumbnail. The unescaped username injects the SVG, which onloads eval(window.name), running the payload to steal cookies via prompt. This affects embedded contexts like third-party sites using Vimeo iframes.

## Requirements

1. Prepared 'name_xss_iframe.html' file.
2. Short uploaded video on attacker's account.
3. Browser allowing popups for prompt testing.

## Defense

Defensive measures and detection strategies:

- Auto-escape user data in all dynamic UI components.
- Delay or prevent thumbnail rendering in iframes.
- Monitor for eval() calls or unexpected prompts in player contexts.
- Use sandbox attributes on iframes to restrict script execution.

## Objectives

1. Simulate victim embed load.
2. Achieve no-interaction JS execution.
3. Exfiltrate session data silently.

## Instructions

### Step 1: Open HTML File

**Context**: Load the page to set payload and start iframe.

Double-click 'name_xss_iframe.html' or open in browser.

### Step 2: Wait for Video End

**Context**: Allow the embedded video to play and end automatically.

Observe the iframe; wait 10 seconds for thumbnail to appear.

### Step 3: Observe Execution

**Context**: Confirm payload runs via alert.

A prompt should appear showing domain and cookies.

**Expected Output**: Alert with 'vimeo.com' and cookie data.

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
- [[no-interaction]]
