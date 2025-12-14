---
id: proc-host-content-takeover
tags:
  - content-hosting
  - phishing-setup
  - proof-of-concept
type: procedure
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Remote File Copy]]'
updated_at: '2025-12-14T05:32:23.368Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host Arbitrary Content on Taken-Over Subdomain

## Summary

This procedure deploys custom content on a hijacked subdomain to demonstrate control, potentially enabling phishing, spam, or brand impersonation attacks.

## Description

After claiming the subdomain under mozaws.net, attackers upload and serve arbitrary files via the third-party hosting service. This step proves the takeover's viability, as seen in the report where researchers hosted a proof-of-concept page, highlighting risks to Mozilla's domain reputation without accessing sensitive data.

## Requirements

1. Control over the registered resource
2. Basic web content (HTML, scripts)
3. Access to the provider's deployment interface

## Defense

Defensive measures and detection strategies:

- Monitor subdomains for unauthorized content via web scanners
- Use certificate pinning or HSTS to limit impersonation
- Conduct regular subdomain audits

## Objectives

1. Serve malicious or PoC content under target domain
2. Simulate phishing or reputation attacks
3. Validate full takeover

## Instructions

### Step 1: Prepare Content

**Context**: Create a simple page to host, e.g., an HTML file announcing the takeover.

Develop content that loads without errors, such as a static page.

### Step 2: Upload and Deploy

**Context**: Use the provider's tools to publish the content.

Upload files via the dashboard or CLI, ensuring the subdomain serves it.

### Step 3: Test Accessibility

**Context**: Verify the content is live and accessible globally.

Browse to the subdomain and check for correct rendering; monitor DNS resolution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Phishing]]
- [[arbitrary-hosting]]
