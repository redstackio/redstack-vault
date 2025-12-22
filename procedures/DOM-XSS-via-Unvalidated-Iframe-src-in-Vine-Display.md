---
tags:
  - dom-xss
  - iframe
  - vine-display
type: procedure
tools:
  - '[[tools/Internet-Explorer]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.281Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: bd40b9bd-0241-4c32-97b0-3b499f4f4b63
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# DOM-XSS-via-Unvalidated-Iframe-src-in-Vine-Display

## Summary

This procedure exploits DOM-based XSS in the ui/playback/vine_display module by setting the iframe src to a user-supplied javascript: URL via the player_url parameter when source_type=vine.

## Description

The vine_display module directly assigns the playerUrl parameter to the iframe's src attribute without protocol validation, allowing javascript:alert(1) to execute code upon iframe load. This occurs in the Amplify Web Player at https://amp.twimg.com/amplify-web-player/prod/source.html, enabling attacks on Vine embeds in Twitter.

## Requirements

1. Internet Explorer for PoC testing
2. No additional hosting needed for basic alert payload
3. Access to the player URL

## Defense

Defensive measures and detection strategies:

- Validate URLs to enforce http/https protocols only
- Use URL sanitization libraries to strip javascript: schemes
- Monitor for anomalous iframe src attributes in client-side logs

## Objectives

1. Execute JavaScript directly in an iframe context
2. Enable clickjacking on embedded Vine players
3. Expose risks in video playback modules

## Instructions

### Step 1: Craft PoC URL

**Context**: Embed the javascript: payload in player_url with source_type=vine.

Construct the URL:

```url
https://amp.twimg.com/amplify-web-player/prod/source.html?player_url=javascript:alert(1)&source_type=vine
```

### Step 2: Load and Trigger

**Context**: Access the URL and interact to load the iframe.

Open in Internet Explorer and click the play button.

> The iframe src executes the javascript: URL, triggering the alert.

### Step 3: Confirm Impact

**Context**: Verify no blocking and potential for escalation.

**Expected Output**: Alert pops on play click.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Internet-Explorer]]

## Tags

- [[dom-xss]]
- [[twitter]]
- [[vine]]
