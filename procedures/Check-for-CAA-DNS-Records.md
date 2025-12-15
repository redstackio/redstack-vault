---
tags:
  - dns
  - caa
  - reconnaissance
  - misconfiguration
type: procedure
tools:
  - '[[tools/CAA-Test-Tool]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
  - DNS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:28:36.599Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: c90da327-b452-49f9-b73e-3b635ce0603d
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Check-for-CAA-DNS-Records

## Summary

This procedure involves querying a domain's DNS records for Certificate Authority Authorization (CAA) resource records (type 257) to determine if the domain specifies authorized certificate authorities. A missing CAA record allows any compliant CA to issue certificates, increasing the risk of misissuance by malicious actors who could impersonate the domain.

## Description

In an attack scenario, reconnaissance actors scan for DNS misconfigurations like absent CAA records to identify domains vulnerable to certificate forgery. This is particularly relevant for web-facing domains where HTTPS is used. The procedure uses online DNS lookup services to query the CAA RR, expecting an empty response if no record exists. Prerequisites include internet access and the target domain name. Expected outcomes include confirmation of the vulnerability, enabling further risk assessment or reporting.

## Requirements

1. Internet access for DNS queries.
2. Target domain name (e.g., gratipay.com).
3. Access to a DNS lookup tool like the CAA Test Tool.

## Defense

Defensive measures and detection strategies:

- Implement CAA records in DNS to specify allowed CAs (e.g., issue ";";" for no issuance).
- Monitor DNS changes for unauthorized modifications.
- Use certificate transparency logs to detect unexpected issuances.

## Objectives

1. Verify the presence or absence of CAA records.
2. Assess risk of unauthorized certificate issuance.
3. Report misconfiguration for remediation.

## Instructions

### Step 1: Perform CAA DNS Lookup

**Context**: Query the target domain for CAA resource records using an online tool to check for misconfigurations.

**Tool Usage** ([[tools/CAA-Test-Tool]]):

Navigate to https://caatest.co.uk/ and enter the domain (e.g., gratipay.com) to query type 257 records.

> This performs a DNS lookup and displays any CAA records or confirms their absence. For gratipay.com, the output shows no records, indicating unrestricted CA issuance.

### Step 2: Analyze Results

**Context**: Review the query output to confirm the vulnerability.

**Instructions**:

If no CAA records are returned, note the impact: increased risk of malicious certificate issuance.

> Expected output: "No CAA records found" or similar, validating the misconfiguration.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/CAA-Test-Tool]]

## Tags

- [[DNS]]
- [[caa]]
- [[Reconnaissance]]
