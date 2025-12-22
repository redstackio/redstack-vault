---
id: proc-demonstrate-non-destructive-poc-for-takeover
tags:
  - subdomain-takeover
  - poc
  - exploitation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-content-serve-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:51:10.592Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate-Non-Destructive-PoC-for-Takeover

## Summary

This procedure demonstrates a subdomain takeover using a non-destructive proof-of-concept, as applied to openapi.starbucks.com, by serving custom benign content from unused URLs via the flawed approval process.

## Description

The PoC exploits inconsistencies in human-approval for domain usage, allowing control over unused paths without disrupting services. It involves claiming a dangling resource (if applicable) and hosting a simple page (e.g., "PoC Demo - No Harm"). This proves arbitrary content serving potential for phishing, resolved via comments on June 20, 2017.

## Requirements

1. Evidence from reconnaissance (dangling DNS).
2. Access to claim the resource (e.g., third-party account).
3. Ability to host static content.

## Defense

Defensive measures and detection strategies:

- Automate domain approvals and monitor for unauthorized claims.
- Use DNS monitoring tools to alert on changes.
- Require PoC validation before closure.

## Objectives

1. Prove takeover control without damage.
2. Reopen the report with evidence.
3. Highlight process vulnerabilities.

## Instructions

### Step 1: Identify and Claim Resource

**Context**: Based on DNS findings, access the third-party service dashboard to claim the unused subdomain pointer.

Manual step: Log into service (e.g., AWS Console), search for the CNAME target, and add content.

### Step 2: Host Custom Content

**Context**: Upload a benign HTML file to the claimed resource.

Example content: <html><body>PoC: Subdomain takeover demonstrated safely.</body></html>

### Step 3: Verify Serving

**Context**: Test access to confirm content loads under the subdomain.

**Command** ([[commands/curl-content-serve-test]]):
```bash
curl -I https://openapi.starbucks.com/unused-url
```

> Expected output: HTTP 200 with custom content headers, or direct browser view showing the PoC page.

### Step 4: Document and Share

**Context**: Capture screenshots and add to report comments.

Include repro steps: "Visit /unused-url to see custom content."

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-content-serve-test]]

## Tools Used

- None

## Tags

- [[poc]]
- [[takeover-demo]]
