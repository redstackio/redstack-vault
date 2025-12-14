---
id: proc-002
tags:
  - mitm
  - traffic-capture
  - token-interception
type: procedure
tools:
  - '[[tools/Wireshark]]'
  - '[[tools/Local-Proxy-Tool]]'
tactics:
  - '[[Defense Evasion]]'
commands:
  - '[[commands/Verify-HTTP-Redirect-in-Password-Reset-Link]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Adversary-in-the-Middle]]'
updated_at: '2025-12-14T17:31:52.441Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Defense Evasion]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Intercept-Token-via-Network-Traffic-Capture

## Summary

This procedure simulates a man-in-the-middle attack by capturing network traffic with Wireshark and a local proxy while accessing the HTTP password reset link, exposing the security token in clear text before HTTPS redirection.

## Description

The password reset link from Mandrillapp uses HTTP, allowing interception of the initial GET request containing the token. Using Wireshark for packet capture and a local proxy (e.g., attached to the browser), the attacker observes the unencrypted transmission and redirect chain: HTTP to `http://instagram-brand.com/register/reset/<token>?email=<email>`, then to HTTPS. This reveals the token without real MITM setup, but demonstrates the risk in unsecured networks. Target environment is web-based with email delivery via Mandrillapp on PHP/nginx stack.

## Requirements

1. Wireshark installed for traffic analysis
2. Local proxy tool configured and attached to browser
3. Copied HTTP reset link from email
4. Local network access for capture

## Defense

Defensive measures and detection strategies:

- Mandate HTTPS for all authentication links and redirects
- Use HSTS to prevent downgrade attacks
- Log and alert on HTTP access to sensitive endpoints

## Objectives

1. Capture the initial HTTP request to Mandrillapp
2. Trace the redirect to expose the token
3. Validate token visibility in clear text

## Instructions

### Step 1: Setup Capture Tools

**Context**: Prepare Wireshark and local proxy to monitor browser traffic.

Launch Wireshark and start capture on the relevant interface. Configure the local proxy tool to intercept browser requests.

> Expected: Tools ready for traffic monitoring.

### Step 2: Access Link and Capture Traffic

**Context**: Request the copied HTTP link in the proxied browser to trigger the vulnerable flow.

Use the browser to GET the link; Wireshark will show the HTTP request to `mandrillapp.com`.

> Expected Output: Packet details revealing token in query parameters.

### Step 3: Verify Redirect Behavior

**Context**: Use [[commands/Verify-HTTP-Redirect-in-Password-Reset-Link]] to check the redirect without full capture.

Execute [[commands/Verify-HTTP-Redirect-in-Password-Reset-Link]]:

```bash
curl -I -s http://mandrillapp.com/track/click/30956340/instagram-brand.com?p=<REDACTED> | grep Location
```

> Expected Output: `Location: http://instagram-brand.com/register/reset/<token>?email=<email>`, confirming exposure.

### Step 4: Analyze Redirect Chain

**Context**: Follow the proxy logs to see the full chain, noting the HTTP leg before HTTPS.

Review proxy intercepts for the 302 redirect responses.

> Expected: Token visible in HTTP URL before secure upgrade.

## MITRE ATT&CK Mapping

### Tactics

- [[Defense Evasion]]

### Techniques

- [[Adversary-in-the-Middle]]

### Sub-Techniques


## Commands Used

- [[commands/Verify-HTTP-Redirect-in-Password-Reset-Link]]

## Tools Used

- [[tools/Wireshark]]
- [[tools/Local-Proxy-Tool]]

## Tags

- [[mitm]]
- [[traffic-capture]]
- [[token-interception]]
