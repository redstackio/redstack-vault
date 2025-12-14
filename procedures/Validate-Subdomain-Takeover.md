---
tags:
  - validation
  - xss
  - subdomain-takeover
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - AWS
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T04:51:10.542Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: eed63eee-dc89-496f-b38a-67688f7d190b
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Validate Subdomain Takeover

## Summary

This procedure verifies successful takeover by accessing the subdomain to load uploaded content and execute XSS payloads, confirming control.

## Description

Post-upload, revisit the subdomain to ensure DNS resolves to the attacker's bucket. View source for markers and trigger XSS to prove impact, such as stealing cookies under a DoD-linked domain.

## Requirements

1. Web browser for execution
2. HTTP client for checks
3. Uploaded files in place

## Defense

Defensive measures and detection strategies:

- Continuously monitor subdomains for unexpected content
- Use certificate transparency logs for subdomain changes
- Implement CSP and XSS protections on parent domain

## Objectives

1. Confirm content serving
2. Execute PoC to show impact
3. Document for reporting

## Instructions

### Step 1: Access Index Page

**Context**: Load the root URL to check default file.

No command; visit http://example-subdomain.target.com in browser or curl:

```bash
curl http://example-subdomain.target.com
```

> Displays uploaded index.html; view source for "<!-- Demonstrated subdomain takeover by chron0x -->".

### Step 2: Execute XSS Payload

**Context**: Trigger the malicious script.

Visit http://example-subdomain.target.com/xss_poc_998877665544332211.html.

> Alert box pops with "XSS via takeover"; confirms injection under trusted domain.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[validation]]
- [[xss]]
