---
id: proc-concrete-proxy-config-001
tags:
  - proxy-config
  - mitm
  - concrete-cms
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
updated_at: '2025-12-14T17:23:24.129Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Configure-Arbitrary-Proxy-in-Concrete-CMS

## Summary

This procedure sets an arbitrary outgoing proxy in Concrete CMS admin settings, allowing interception of HTTP requests to the update server via tools like Burp Suite, facilitating MITM attacks without root certificate installation.

## Description

Concrete CMS permits administrators to configure outgoing proxies without validation, enabling traffic interception. This is exploited by pointing the proxy to a local instance (e.g., Burp Suite at 127.0.0.1:8080). The attack scenario requires admin access and targets the HTTP fetch from www.concrete5.org. Prerequisites include a running proxy tool; expected outcome is all outgoing HTTP traffic routed through the attacker-controlled proxy.

## Requirements

1. Administrator privileges in Concrete CMS
2. Running Burp Suite or similar proxy on localhost:8080
3. Access to dashboard settings (System & Settings > Basics > Proxy)

## Defense

Defensive measures and detection strategies:

- Disable or validate proxy configurations in CMS settings
- Monitor for unusual outgoing connections from the web server
- Use HTTPS-only for all external fetches to prevent MITM

## Objectives

1. Route update JSON requests through attacker proxy
2. Enable interception without TLS issues
3. Set up for JSON tampering in subsequent steps

## Instructions

### Step 1: Access Proxy Settings

**Context**: Navigate to the proxy configuration in the admin dashboard.

No command; go to Dashboard > System & Settings > Basics > Proxy Settings.

> Fill in the proxy host (127.0.0.1) and port (8080).

### Step 2: Save Configuration

**Context**: Apply the proxy settings to activate interception.

Click Save.

> Expected output: Settings updated; test by triggering a network request and verifying interception in Burp Suite.

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

- proxy-config
- mitm
- concrete-cms
