---
tags:
  - host-header-injection
  - proxy-manipulation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
  - Cloud
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 412c9f36-6515-4fa5-b651-538b8d63a582
created_at: '2025-12-14T03:15:05.039Z'
updated_at: '2025-12-14T03:15:05.039Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Services-with-Burp-Suite-Host-Replacement

## Summary

This procedure configures Burp Suite to automatically replace Host headers in proxied requests, enabling scalable access to multiple internal instances on exposed origin IPs.

## Description

Burp acts as a man-in-the-middle proxy to intercept and modify HTTP traffic, useful for testing various subdomains without manual curl commands. Targets services like Grafana on IPs without proper access controls.

## Requirements

1. Burp Suite Professional or Community edition
2. Browser configured to proxy through Burp (e.g., 127.0.0.1:8080)
3. List of IPs and subdomains from reconnaissance

## Defense

Defensive measures and detection strategies:

- Deploy WAF rules to block mismatched Host-IP pairs
- Use certificate pinning to prevent proxy interception
- Monitor for traffic patterns indicative of header manipulation

## Objectives

1. Automate Host replacement for efficient testing
2. Access credential-required services like Grafana
3. Identify additional misconfigurations

## Instructions

### Step 1: Configure Host Replacement Rule

**Context**: Set up Burp to swap IP-based Hosts with subdomain targets.

**Command** (Burp GUI):
No CLI; use Options > Rules > Replace & Match.

> Add rule: Match 'Host: <IP>' (e.g., Host: 35.244.200.254), Replace with 'Host: pghero.dev-go.exchange'. Expected: Automatic header changes in proxied requests.

### Step 2: Proxy Requests to Origin IPs

**Context**: Browse or request internal paths through the proxy.

**Command** (Manual via Browser):
```bash
# Point browser to https://35.244.200.254/ via Burp proxy
```

> Observe replaced requests accessing Grafana or TokenModel.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[host-header-injection]]
- [[proxy-manipulation]]
