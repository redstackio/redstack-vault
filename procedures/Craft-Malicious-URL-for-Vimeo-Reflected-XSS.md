---
tags:
  - xss
  - url-crafting
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 77c76ca7-8700-4d74-b5b3-b1218b87498c
created_at: '2025-12-14T03:15:35.678Z'
updated_at: '2025-12-14T03:15:35.678Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-URL-for-Vimeo-Reflected-XSS

## Summary

This procedure crafts a malicious URL exploiting the reflected XSS in player.vimeo.com's 'user' parameter, injecting a JavaScript event handler for later execution.

## Description

The Vimeo player reflects the 'user' GET parameter directly into HTML attributes without encoding, allowing attribute-based XSS. The payload breaks out of the attribute using quotes and injects an event handler like onmousemove. This step prepares the URL for delivery to victims, such as via email or social engineering. Prerequisites include basic URL encoding knowledge; no tools beyond a text editor or browser dev tools are needed. Expected outcome: A functional URL that embeds the payload in the page.

## Requirements

1. Access to a web browser for encoding and testing
2. Knowledge of the target endpoint (player.vimeo.com/hubnut/channel/830190)
3. URL encoding capability (manual or via browser)

## Defense

Defensive measures and detection strategies:

- Implement output encoding for user inputs in HTML attributes (e.g., use htmlspecialchars in PHP)
- Deploy Content Security Policy (CSP) to block inline scripts and event handlers
- Monitor for anomalous URLs in access logs containing script tags or event attributes

## Objectives

1. Inject JavaScript payload into reflected parameter
2. Ensure payload survives URL transmission
3. Prepare for victim interaction to trigger execution

## Instructions

### Step 1: Design the Payload

**Context**: Create a breakout payload that closes the HTML attribute and injects an event handler.

Raw payload: `user="onmousemove="alert(1)"`

URL-encode special characters: `%22` for quotes, resulting in `user=%22onmousemove=%22alert(1)%22`.

### Step 2: Construct the Full URL

**Context**: Append the encoded payload to the vulnerable endpoint.

Base URL: `http://player.vimeo.com/hubnut/channel/830190`

Full URL:

```plaintext
http://player.vimeo.com/hubnut/channel/830190?user=%22onmousemove=%22alert(1)%22
```

> This URL, when visited, reflects the payload into the page, setting up the event handler.

### Step 3: Verify Reflection

**Context**: Test the URL to confirm reflection without triggering.

Load the URL in a browser and inspect the HTML source (right-click > View Page Source). Search for the 'user' value to ensure it's inserted unencoded.

**Expected Output**: Payload visible in source, e.g., `<some-attr="user" onmousemove="alert(1)">`.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
