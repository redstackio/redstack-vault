---
id: proc-reddit-xss-url-craft-001
tags:
  - xss
  - url-injection
  - phishing
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:56:04.006Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Craft-Malicious-Verification-URL-for-XSS

## Summary

This procedure involves constructing a malicious URL targeting Reddit's /verification endpoint by injecting a JavaScript payload into the token parameter, enabling reflected XSS when accessed by a victim.

## Description

In the context of Reddit's email verification feature, the /verification endpoint fails to sanitize the token string in the URL path, allowing attackers to inject JavaScript that reflects back into the interstitial page. This sets up the attack by luring a victim (e.g., via phishing) to the crafted URL, where the payload awaits triggering. Expected outcomes include preparation for code execution, leading to impacts like session theft or phishing. Prerequisites include knowledge of URL encoding and basic social engineering.

## Requirements

1. Access to a web browser for testing the URL
2. Understanding of JavaScript payloads and URL encoding (e.g., %20 for spaces)
3. Victim interaction via email or link sharing

## Defense

Defensive measures and detection strategies:

- Implement output encoding and sanitization for all user-controlled inputs in URL paths
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous access patterns to verification endpoints

## Objectives

1. Inject JavaScript payload into the verification token
2. Deliver the URL to a victim without detection
3. Prepare for payload execution upon user interaction

## Instructions

### Step 1: Design the Payload

**Context**: Select a JavaScript payload suitable for testing or exploitation, such as a simple alert or cookie exfiltration.

Encode the payload to bypass basic filters, e.g., `alert(document.location)` becomes `%27%2c%20alert(document.location)%2c%20%27`.

### Step 2: Construct the Malicious URL

**Context**: Append the encoded payload to the base endpoint path.

Build the URL as `https://www.reddit.com/verification/[base-token][payload]`, e.g., `https://www.reddit.com/verification/asd',%20alert(document.location),%20'`. Test in a browser to ensure the page loads with the parameter reflected in the source.

### Step 3: Distribute the URL

**Context**: Use social engineering to get the victim to access the URL, mimicking a legitimate verification link.

Send via email or messaging, claiming it's a required email verification step.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Drive-by Compromise]] Drive-by Compromise

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[url-injection]]
