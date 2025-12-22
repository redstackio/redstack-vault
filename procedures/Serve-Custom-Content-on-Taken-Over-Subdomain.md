---
tags:
  - content-serving
  - poc
  - impersonation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-url]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 39cbeb7c-6ba3-45ab-a48b-4c02e0c76bda
created_at: '2025-12-14T04:38:39.951Z'
updated_at: '2025-12-14T04:38:39.951Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Serve-Custom-Content-on-Taken-Over-Subdomain

## Summary

This procedure demonstrates control by hosting custom content on the taken-over subdomain, proving the ability to impersonate the victim for attacks like phishing or XSS.

## Description

Once claimed, configure Fastly to serve a proof-of-concept file, such as an HTML page at a specific path. Accessing it via the original subdomain URL confirms takeover, allowing arbitrary content delivery under the trusted domain, leading to severe impacts like cookie theft or malware distribution.

## Requirements

1. Control of Fastly service with claimed domain
2. Content to upload (e.g., HTML file)
3. HTTP client for testing

## Defense

Defensive measures and detection strategies:

- Monitor traffic anomalies on subdomains
- Implement certificate pinning or HSTS to detect content changes
- Use content security policies to block unexpected scripts

## Objectives

1. Validate takeover with PoC
2. Enable malicious content delivery
3. Simulate real attacks like phishing

## Instructions

### Step 1: Configure Content in Fastly

**Context**: Upload or define custom response in Fastly VCL or backend.

**Command** (Manual):
In Fastly dashboard, set up a response object or origin for /haveanicetakeover-poc.html with custom HTML.

> HTML could be a simple page saying 'Takeover Successful'.

### Step 2: Test Access

**Context**: Verify content serves correctly.

**Command** ([[commands/curl-access-url]]):
```bash
curl http://addons-preview-cdn.mozilla.net/haveanicetakeover-poc.html
```

> Output should display the custom HTML, confirming successful serving.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-access-url]]

## Tools Used


## Tags

- [[content-serving]]
- [[poc]]
- [[impersonation]]
