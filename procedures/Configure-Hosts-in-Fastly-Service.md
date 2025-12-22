---
id: p-configure-hosts-fastly
tags:
  - domain-takeover
  - host-configuration
  - csp-bypass
type: procedure
tools:
  - '[[tools/Fastly-Management-Dashboard]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T04:51:10.673Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Configure-Hosts-in-Fastly-Service

## Summary

This procedure explains setting up host configurations in the Fastly service to serve malicious content via the taken-over subdomain, enabling CSP bypass.

## Description

Host configuration in Fastly defines how requests to the domain are handled, such as routing to backends or serving static content. For the attack, configure to host JavaScript payloads or redirects that GitLab's CSP would otherwise block. Since the domain is whitelisted, resources load without violation, allowing XSS or data exfiltration. Test by curling the subdomain to verify control. Expected outcome: Domain serves attacker-defined responses.

## Requirements

1. Service with attached domain
2. Desired backend or content (e.g., malicious script URL)
3. Understanding of VCL (Fastly's config language) basics

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP with nonce or hash validation instead of domain whitelists
- Monitor traffic to whitelisted domains for anomalous payloads
- Use web application firewalls to inspect CDN-originated content

## Objectives

1. Define request/response behaviors for the subdomain
2. Inject malicious elements for exploitation
3. Validate CSP bypass in GitLab context

## Instructions

### Step 1: Access Host Settings

**Context**: Enter the configuration area for hosts.

In the service, go to 'Settings' > 'Hosts' or use the VCL editor.

### Step 2: Set Configurations

**Context**: Apply rules to control content.

Add a backend (e.g., point to a malicious server) or inline script serving. Save and activate the configuration.

**Expected Output**: Configuration active; test with browser or curl to see custom response.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Fastly-Management-Dashboard]]

## Tags

- [[domain-takeover]]
- [[host-configuration]]
- [[csp-bypass]]
