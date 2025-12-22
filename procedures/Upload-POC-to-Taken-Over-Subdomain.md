---
id: proc-uuid-4
tags:
  - subdomain-takeover
  - poc
  - upload
  - xss
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T05:32:23.539Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Upload-POC-to-Taken-Over-Subdomain

## Summary

This procedure deploys a proof-of-concept file to the now-controlled subdomain, verifying takeover and demonstrating potential for malicious payloads like phishing pages or XSS scripts.

## Description

Once the domain is claimed, the service's deployment tools allow uploading static files or code. A simple HTML POC (e.g., displaying 'Taken Over') is uploaded and accessed via the subdomain URL. This confirms control and highlights risks such as distributing malware or conducting phishing on the DoD domain, where users might trust the legitimate-looking URL.

## Requirements

1. Successful domain claiming from prior step
2. Basic HTML or text file for POC
3. Access to the service's file management or deployment interface

## Defense

Defensive measures and detection strategies:

- Monitor web traffic for unexpected content on subdomains
- Implement content security policies (CSP) on all subdomains
- Use certificate pinning or HSTS to detect hijacked domains

## Objectives

1. Verify subdomain control through content serving
2. Demonstrate exploitation potential
3. Enable further attacks like XSS or malware hosting

## Instructions

### Step 1: Prepare POC File

**Context**: Create a simple file to upload as evidence of control.

Draft an HTML file, e.g., <html><body><h1>Subdomain Taken Over - POC</h1></body></html>, and save as poc.html.

### Step 2: Upload and Deploy

**Context**: Use the service's tools to host the file.

In the app's file or deployment section, upload poc.html to the root directory. Deploy if required, then visit http://affected-subdomain.dod.gov/poc.html.

> Expected output: POC page loads, confirming the subdomain serves attacker content.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[subdomain-takeover]]
- [[poc]]
