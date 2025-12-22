---
tags:
  - ssrf
  - payload-injection
  - url-forgery
type: procedure
tools:
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:09.263Z'
sub_techniques: []
id: 315eec17-f783-4e35-8ac8-ee7060f851c5
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-Burp-Collaborator-URL-via-Chat

## Summary

This procedure details the injection of a Burp Collaborator URL into the chat box to trigger server-side requests, exploiting the Blind SSRF vulnerability without direct feedback on the client side.

## Description

The MTN Group website's chat feature processes user inputs by making HTTP requests to provided URLs, lacking validation for external domains. By sending a unique Collaborator URL, the attacker induces the server to perform DNS resolutions and HTTP fetches, confirming the SSRF. This can lead to broader impacts like internal network scanning or malicious payload delivery. Prerequisites include an active Burp Suite instance with Collaborator configured.

## Requirements

1. Burp Suite Professional with Collaborator enabled
2. Access to the chat interface from the previous procedure
3. Unique Collaborator domain generated

## Defense

Defensive measures and detection strategies:

- Validate and whitelist allowed domains in chat processing logic
- Sanitize inputs to block URL schemes or external hosts
- Monitor server logs for unexpected outbound connections from chat services

## Objectives

1. Deliver the SSRF payload via chat input
2. Trigger unauthorized server requests
3. Set up for out-of-band observation

## Instructions

### Step 1: Generate Collaborator URL

**Context**: Create a traceable URL for monitoring interactions.

Use Burp Suite interface (no CLI command):

```bash
# In Burp: Copy a payload like https://abc123.oastify.com/test.png
```

> Expected output: Unique URL ready for pasting.

### Step 2: Inject and Send URL

**Context**: Enter the payload into the chat to induce the request.

Manual browser action:

```bash
# Paste into chat input: https://your-collaborator.oastify.com/test.png
# Click 'Send'
```

> Expected output: Message sent; server processes in background.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Collaborator]]

## Tags

- [[ssrf]]
- [[payload-injection]]
