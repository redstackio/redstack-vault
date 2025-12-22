---
id: uuid-channel-create
tags:
  - xss
  - stored-xss
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:20.710Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Malicious-Channel-Name-for-Stored-XSS

## Summary

This procedure creates a Vimeo channel with a malicious name payload that exploits stored XSS in the mobile '+ Follow' button by injecting HTML attributes for JavaScript execution on interaction.

## Description

In Vimeo's desktop interface, channel names are not properly sanitized, allowing injection of payloads like '" ontouchstart="alert(document.domain)"' into the name field. This payload is stored and later rendered unescaped in the mobile web version's button attributes, enabling XSS when victims touch the button. The attack targets client-side execution for potential data theft, requiring a Vimeo account but no advanced privileges.

## Requirements

1. Valid Vimeo account with channel creation ability
2. Desktop web browser (e.g., Chrome) for setup
3. Access to https://vimeo.com

## Defense

Defensive measures and detection strategies:

- Implement output encoding for user-generated content in HTML attributes
- Use Content Security Policy (CSP) to restrict inline scripts and external sources
- Monitor for anomalous JavaScript alerts or network requests from mobile sessions

## Objectives

1. Store a touch-event payload in a channel name
2. Prepare for mobile exploitation without triggering desktop sanitization
3. Enable interaction-based XSS for victims

## Instructions

### Step 1: Navigate to Channel Creation

**Context**: Access the channel management page to initiate creation.

Log in to Vimeo on desktop and go to https://vimeo.com/[your_vimeo_url]/channels, then click '+ Create new channel'.

### Step 2: Inject Payload and Create Channel

**Context**: Enter the malicious payload as the channel name to store the XSS vector.

In the Channel Name field, input: `" ontouchstart="alert(document.domain)"`

Click 'Create This Channel' to save.

> This embeds the payload in the channel metadata, which will be reflected in mobile UI without escaping.

### Step 3: Save Channel URL

**Context**: Capture the URL for sharing with victims.

Copy the generated URL, e.g., https://vimeo.com/channels/963609.

**Expected Output**: Channel page loads with the tainted name visible.

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
- [[stored-xss]]
