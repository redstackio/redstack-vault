---
id: proc-uuid-report-vuln
tags:
  - responsible-disclosure
  - bug-bounty
  - reporting
type: procedure
tools: []
tactics: []
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques: []
updated_at: '2025-12-14T04:38:49.615Z'
skill_level: beginner
impact_level: low
detection_risk: none
sub_techniques: []
validated: true
---
# Report-Dangling-Subdomain

## Summary

This procedure outlines responsible disclosure of a subdomain takeover vulnerability, including initial contact and formal submission, as done for the Roblox creatorforum.roblox.com issue.

## Description

After discovery, send an initial report via email to general security contacts, follow up with dedicated bug bounty emails, and submit a detailed report on platforms like HackerOne. This ensures the vulnerability is addressed without exploitation.

## Requirements

1. Email access and knowledge of target contacts (e.g., info@roblox.com)
2. Access to bug bounty programs like HackerOne
3. Clear documentation of findings

## Defense

Defensive measures and detection strategies:

- Establish clear reporting channels and respond promptly to disclosures
- Use bug bounty programs to incentivize ethical reporting
- Track and audit disclosed vulnerabilities for patterns

## Objectives

1. Notify the organization of the vulnerability
2. Provide evidence for reproduction
3. Facilitate remediation to prevent exploitation

## Instructions

### Step 1: Initial Email Report

**Context**: Send a concise alert to general security email.

Compose an email to info@roblox.com describing the dangling CNAME on creatorforum.roblox.com and potential risks like phishing.

**Expected Output**: Delivery receipt or initial acknowledgment.

### Step 2: Follow-Up with Bug Bounty Contact

**Context**: Escalate to specialized security team.

Email bugbounty@roblox.com with more details, including screenshots of the inactive page and DNS queries.

**Expected Output**: Response from bounty team.

### Step 3: Formal HackerOne Submission

**Context**: Submit comprehensive report for verification and reward.

Create a HackerOne report (ID 264494) with full narrative, steps, and impact assessment.

## MITRE ATT&CK Mapping

### Tactics


### Techniques


### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[responsible-disclosure]]
- [[bug-bounty]]
- [[reporting]]
