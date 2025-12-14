---
id: p1q2r3s4-t5u6-7890-bcde-fg1234567890
tags:
  - proxy
  - interception
  - burp
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.515Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Setup-Burp-Proxy-for-Interception

## Summary

This procedure sets up Burp Suite as an interception proxy to capture and analyze HTTP traffic from a browser to the target application, essential for identifying and exploiting client-side enforcement flaws.

## Description

In the context of web application testing, configuring a proxy like Burp Suite allows real-time inspection and modification of requests. For HackerOne's GraphQL endpoint, this enables capturing the UpdateInvitationPreferencesMutation triggered by UI interactions. Prerequisites include a running Burp instance and browser proxy configuration. Expected outcome: All traffic intercepted without disruption.

## Requirements

1. Burp Suite installed and launched
2. Browser (e.g., Chrome) configured to use HTTP proxy at 127.0.0.1:8080
3. No upstream proxy conflicts

## Defense

Defensive measures and detection strategies:

- Monitor for unusual proxy traffic or tool signatures in network logs
- Enforce certificate pinning to block MITM proxies
- Use WAF rules to detect tampered GraphQL payloads

## Objectives

1. Establish interception for request analysis
2. Ensure seamless traffic routing
3. Prepare for request modification

## Instructions

### Step 1: Launch Burp Suite

**Context**: Start the tool and configure the proxy listener.

No command required; use the GUI to set Proxy > Options > Add listener on 127.0.0.1:8080.

> Burp listens for traffic; confirm in the dashboard.

### Step 2: Configure Browser Proxy

**Context**: Route browser traffic through Burp.

In browser settings, set proxy to manual HTTP proxy 127.0.0.1 port 8080; install Burp's CA certificate for HTTPS.

> Browser now proxies all requests; test with a simple site.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- proxy-setup
- interception
