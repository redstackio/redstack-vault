---
tags:
  - content-hosting
  - phishing
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/dig-dns-lookup]]'
platforms:
  - Web
  - Cloud
techniques:
  - '[[Remote File Copy]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: becb0a81-9766-48a4-8f60-98b90b3c7035
created_at: '2025-12-14T05:32:23.717Z'
updated_at: '2025-12-14T05:32:23.717Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Host-Arbitrary-Content-on-Subdomain

## Summary

This procedure demonstrates control over a taken-over subdomain by uploading and serving arbitrary content, such as phishing pages or redirects, to exploit the trusted domain for malicious purposes.

## Description

After claiming the subdomain under mozgcp.net, the attacker hosts content on the associated service (e.g., GCP App Engine or Storage). This allows serving HTML, scripts, or redirects, compromising Mozilla's reputation. Prerequisites: Subdomain control and hosting access. Outcomes: Live malicious site under the trusted domain.

## Requirements

1. Control of the subdomain via provider console
2. Hosting service (e.g., static site host or server)
3. Content files (e.g., HTML for PoC)

## Defense

Defensive measures and detection strategies:

- Implement subdomain monitoring for unexpected content
- Use web application firewalls to block anomalous traffic
- Regularly scan owned domains for unauthorized hosting

## Objectives

1. Upload and deploy custom content to the subdomain
2. Verify accessibility and functionality
3. Enable attacks like phishing or malware distribution

## Instructions

### Step 1: Upload Content

**Context**: Transfer files to the controlled hosting environment.

Use the provider's upload tool (e.g., gsutil for GCP Storage) or SCP to deploy an index.html file with proof-of-concept content.

Example gsutil command (inferred for GCP):
```bash
gsutil cp index.html gs://your-bucket/
gsutil web set -m index.html gs://your-bucket/
```

### Step 2: Verify Hosting

**Context**: Confirm the content is served correctly.

Execute [[commands/dig-dns-lookup]] to ensure resolution, then access the URL in a browser.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig @8.8.8.8 controlled-subdomain.mozgcp.net
```

> Expected: Resolution to your hosting IP, and browser shows your uploaded page.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Remote File Copy]]

### Sub-Techniques



## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used



## Tags

- [[phishing-setup]]
- [[arbitrary-hosting]]
