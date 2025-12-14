---
tags:
  - intercept
  - http-proxy
  - api-analysis
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:25:18.068Z'
sub_techniques: []
id: cb6ffaac-eb5c-4b9b-8ef7-53e496b2a36e
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Intercept-GIF-Send-Request-with-Burp-Suite

## Summary

This procedure uses Burp Suite to capture and analyze the HTTP requests generated when sending a GIF via LinkedIn's messaging interface, revealing the vulnerable API endpoint and payload structure.

## Description

LinkedIn's GIF sending feature relies on the messaging API, which can be intercepted to understand normal traffic. By proxying through Burp Suite, attackers identify the createMessage endpoint and the externalMedia URL parameter. This is performed in a controlled environment, typically on the web version, and sets up for payload modification. Prerequisites include Burp Suite installation and browser proxy configuration.

## Requirements

1. Burp Suite Professional or Community edition installed
2. Browser (e.g., Chrome) configured to use Burp as HTTP proxy (127.0.0.1:8080)
3. Active LinkedIn session in the proxied browser
4. Test victim or self for sending GIFs

## Defense

Defensive measures and detection strategies:

- Enforce HTTPS with certificate pinning to hinder proxy interception
- Monitor for anomalous API request patterns from known tools like Burp
- Implement client-side request signing to detect tampering

## Objectives

1. Capture the JSON payload for GIF sending
2. Identify the vulnerable externalMedia URL field
3. Forward irrelevant requests to isolate the target endpoint

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp Suite to intercept LinkedIn traffic.

No specific command; in Burp Suite:

1. Launch Burp and ensure Proxy listener is running on 127.0.0.1:8080
2. In browser settings, set HTTP proxy to 127.0.0.1:8080
3. Install Burp's CA certificate in browser to handle HTTPS

> Expected output: Traffic from browser routed through Burp without errors.

### Step 2: Send GIF and Intercept

**Context**: Trigger the GIF send to capture requests.

In LinkedIn messaging:

1. Open a conversation
2. Click GIF icon, select a GIF, and send
3. In Burp Proxy > HTTP history, observe intercepted requests
4. Forward all until reaching createMessage endpoint

> Expected output: JSON payload visible with legitimate GIF URL in externalMedia.media.url.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Adversary-in-the-Middle]] Adversary-in-the-Middle

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[intercept]]
- [[http-proxy]]
- [[api-analysis]]
