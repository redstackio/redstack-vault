---
id: proc-uuid-4
tags:
  - zendesk
  - ssl
  - security-bypass
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.593Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Enable SSL for Custom Domain in Zendesk

## Summary

This procedure activates SSL on the mapped custom domain in Zendesk to ensure secure HTTPS access and prevent insecure redirects.

## Description

After mapping, enable SSL to provision a certificate for the subdomain, making the takeover site appear legitimate. This is crucial for phishing as it avoids browser warnings in web contexts.

## Requirements

1. Mapped custom domain in Zendesk
2. Admin access to security settings
3. Valid DNS propagation

## Defense

Defensive measures and detection strategies:

- Monitor SSL certificate issuances for owned subdomains
- Implement certificate transparency logs monitoring
- Restrict custom SSL to verified domains only

## Objectives

1. Secure the subdomain with HTTPS
2. Prevent fallback to HTTP or redirects
3. Enhance phishing realism

## Instructions

### Step 1: Access Security Settings

**Context**: Navigate to custom domain security options.

In Zendesk, go to Settings > Security > Custom domains.

> Expected: List of mapped domains.

### Step 2: Enable SSL

**Context**: Activate certificate for the domain.

Select 'help.tictail.com' and enable SSL provisioning.

> Expected: SSL enabled, certificate issued shortly after.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[zendesk]]
- [[ssl]]
- [[security-bypass]]
