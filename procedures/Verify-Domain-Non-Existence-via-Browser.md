---
tags:
  - dns
  - verification
  - reconnaissance
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Hardware]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: c04d1d68-7914-47c0-9411-774e61534592
created_at: '2025-12-14T04:38:39.400Z'
updated_at: '2025-12-14T04:38:39.400Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Verify-Domain-Non-Existence-via-Browser

## Summary

This procedure uses a web browser to test if a domain resolves, confirming potential availability for takeover by observing DNS errors.

## Description

Attackers access the suspicious domain (e.g., '3737signals.com') in a browser to trigger DNS lookup. A failure indicates non-registration, a key step in domain takeover reconnaissance. This is low-risk and requires only internet access; outcomes validate the dangling reference from app analysis.

## Requirements

1. Web browser with internet connectivity
2. The target domain name from prior code analysis
3. No special permissions needed

## Defense

Defensive measures and detection strategies:

- Register defensive domains (typosquatting variants)
- Use DNS monitoring tools to alert on unresolved queries
- Implement app-level URL validation to avoid dangling refs

## Objectives

1. Confirm domain does not resolve to a live site
2. Capture error page details for further investigation
3. Rule out false positives from code findings

## Instructions

### Step 1: Navigate to Domain

**Context**: Initiate DNS resolution via HTTP request.

Open a browser and enter 'http://3737signals.com' in the address bar. Press Enter to load.

**Expected Output**: Page fails to load, showing a DNS error like 'This site can’t be reached' or 'DNS_PROBE_FINISHED_NXDOMAIN'.

### Step 2: Inspect Error Page

**Context**: Gather additional metadata from the failure response.

View the full error message and any default pages (e.g., registrar placeholders). Note any branding or links.

**Expected Output**: Error details confirming non-existence.

### Step 3: Test Variations

**Context**: Ensure thorough verification.

Try HTTPS version and ping the domain from command line (if available) to confirm consistent failure.

**Expected Output**: Uniform DNS failure across protocols.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[DNS]]
- [[verification]]
- [[Reconnaissance]]
