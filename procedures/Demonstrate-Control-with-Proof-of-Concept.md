---
id: proc-poc-subdomain-control
tags:
  - proof-of-concept
  - subdomain-takeover
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
updated_at: '2025-12-14T04:51:26.318Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate Control with Proof-of-Concept

## Summary

This procedure deploys a simple payload on the taken-over subdomain to prove control and highlight potential impacts like phishing.

## Description

After claiming course.oberlo.com, upload content to showcase takeover, such as a warning message, and archive it to document the vulnerability without causing harm.

## Requirements

1. Control of the Kajabi site
2. Web browser for uploading and viewing
3. Wayback Machine for archiving

## Defense

Defensive measures and detection strategies:

- Monitor subdomains for unexpected content changes
- Use certificate pinning or HSTS to limit trust
- Alert on anomalous traffic to subdomains

## Objectives

1. Upload and display custom content
2. Verify accessibility
3. Archive for reporting

## Instructions

### Step 1: Upload POC Payload

**Context**: Add a simple page to the Kajabi site.

In Kajabi editor: Create a page with text like "POC: This subdomain has been taken over via dangling DNS." Publish.

### Step 2: Verify and Archive

**Context**: Test access and preserve evidence.

```bash
curl https://course.oberlo.com
```

> Output shows your custom content.

Then, visit archive.org and submit the URL for snapshot.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

-

## Commands Used

-

## Tools Used

-

## Tags

- [[proof-of-concept]]
- [[Phishing]]
