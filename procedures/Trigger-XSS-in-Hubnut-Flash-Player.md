---
tags:
  - xss
  - flash
  - player
  - trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: f2500abe-ed33-4127-98a2-087461e85cbf
created_at: '2025-12-14T03:16:30.637Z'
updated_at: '2025-12-14T03:16:30.637Z'
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Hubnut-Flash-Player

## Summary

This procedure simulates victim interaction by accessing the video via the Hubnut widget to force Flash player usage, playing the video, and enabling captions to execute the injected JavaScript payload.

## Description

The Hubnut player URL bypasses modern HTML5 defaults, rendering captions in Flash without escaping. From a separate account, embed and interact with the video to trigger XSS. This requires user action (enabling CC) and targets browsers supporting Flash. Outcome is arbitrary JavaScript execution in the victim's context, such as domain alerts.

## Requirements

1. Separate Vimeo account or incognito browser for victim simulation
2. Configured video with malicious captions from prior procedure
3. Browser with Flash support enabled (legacy requirement)
4. Access to Hubnut player URL format

## Defense

Defensive measures and detection strategies:

- Migrate fully to HTML5 players that sanitize .vtt content
- Disable or detect Flash usage in embeds
- Log and alert on caption enables in embedded players
- Educate users on risks of enabling captions from untrusted sources

## Objectives

1. Force rendering in vulnerable Flash player
2. Require and simulate user interaction to enable captions
3. Achieve JavaScript execution confirming XSS

## Instructions

### Step 1: Access Hubnut Player

**Context**: Use the special URL to invoke Flash player.

From another account, navigate to https://player.vimeo.com/hubnut/user/[user_url], replacing [user_url] with the target (e.g., user36690798).

**Expected Output**: Hubnut player loads the video in Flash mode.

### Step 2: Play Video and Enable Captions

**Context**: Trigger payload rendering.

Click 'Play' to start the video, then click the 'CC' button at the bottom right and select 'English' to activate captions.

**Expected Output**: Captions display, executing the script (e.g., alert pops up with document.domain).

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
- [[flash]]
- [[vimeo]]
- [[player]]
