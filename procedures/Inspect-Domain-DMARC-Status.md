---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - dmarc
  - dns
  - recon
type: procedure
tools:
  - '[[tools/DMARC-Inspector]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - DNS
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:30:59.007Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Inspect Domain DMARC Status

## Summary

This procedure checks a domain's DMARC configuration by querying DNS TXT records for the _dmarc subdomain, identifying if a policy is published to prevent email spoofing.

## Description

In an attack scenario, reconnaissance of email authentication mechanisms is crucial for phishing preparation. Without DMARC, domains like paragonie.com are vulnerable to spoofing as receivers (e.g., Gmail) cannot enforce alignment between From headers and authentication results. This procedure uses online tools to inspect records, confirming the absence of a DMARC policy despite possible SPF or DKIM setups. Expected outcome: Report showing no policy, enabling further spoofing tests.

## Requirements

1. Internet access for DNS queries
2. Access to an online DMARC inspection tool
3. Target domain name (e.g., paragonie.com)

## Defense

Defensive measures and detection strategies:

- Publish a DMARC TXT record with p=reject or p=quarantine policy
- Monitor DMARC reports for spoofing attempts
- Use tools like dmarcian for ongoing compliance checks

## Objectives

1. Verify absence of DMARC policy to assess spoofing risk
2. Identify supporting records like SPF and DKIM
3. Provide evidence for vulnerability reporting

## Instructions

### Step 1: Query DMARC Records

**Context**: Use an online inspector to retrieve and analyze the _dmarc TXT record without manual DNS tools.

No command required; navigate to [[tools/DMARC-Inspector]] at https://dmarcian.com/dmarc-inspector/ and enter the domain "paragonie.com".

> The tool will display DNS results, confirming no DMARC policy (e.g., "No DMARC record found").

### Step 2: Analyze Results

**Context**: Review the output for policy details and authentication alignment.

Interpret the tool's report to note the lack of enforcement on non-compliant emails.

> Expected: Absence of v=DMARC1 tag in TXT record, indicating bypass opportunity.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/DMARC-Inspector]]

## Tags

- dmarc
- dns-recon
- email-auth
