---
tags:
  - subdomain-takeover
  - web
  - execution
type: procedure
tools: []
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
updated_at: '2025-12-14T04:51:10.534Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: f4c1b51b-9625-400c-a3d1-de1bb6bc5a1c
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Remote File Copy]]'
---
# Demonstrate Control by Hosting Custom Content

## Summary

This procedure uploads and serves custom content on a taken-over subdomain to prove control, simulating defacement or phishing scenarios.

## Description

After claiming the service, attackers deploy arbitrary content like a blog or malicious page. In the Uber example, the attacker hosted a personal blog on translate.uber.com and de.uber.com, showing potential for brand impersonation. This step confirms full subdomain hijacking.

## Requirements

1. Claimed service from prior step
2. Content ready for upload (e.g., HTML files)
3. Access to the service's deployment interface

## Defense

Defensive measures and detection strategies:

- Implement content security policies (CSP) on subdomains
- Monitor for unexpected content changes via web scanners
- Use certificate pinning to detect hijacked domains

## Objectives

1. Deploy custom content to the subdomain
2. Verify accessibility and functionality
3. Highlight impact for reporting or exploitation

## Instructions

### Step 1: Prepare Custom Content

**Context**: Create files to host, e.g., index.html with proof-of-concept text.

No command; manual file creation.

> Expected: HTML file ready for upload.

### Step 2: Upload to Claimed Service

**Context**: Deploy content via service-specific method (e.g., Git push for GitHub Pages).

For Heroku-like:

```bash
git push heroku main
```

> Expected: Deployment success message.

### Step 3: Access and Verify

**Context**: Test the subdomain loads the content.

Fetch via curl:

```bash
curl https://fr.uber.com
```

> Expected: Returns your custom HTML.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[Remote File Copy]] Ingress Tool Transfer

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[content-hosting]]
- [[proof-of-concept]]
