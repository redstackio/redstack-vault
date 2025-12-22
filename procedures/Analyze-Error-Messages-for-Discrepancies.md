---
id: proc-analyze-error-messages-uber
tags:
  - error-analysis
  - ssrf
  - recon
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:39:10.105Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze-Error-Messages-for-Discrepancies

## Summary

This procedure focuses on examining server error messages from XXE payload responses to detect differences that reveal internal port connectivity on the Uber suppliers portal.

## Description

After sending XXE OOB payloads, the server's error handling may leak information through inconsistent messages, such as "connection refused" for closed ports versus timeouts for open ones. This manual analysis infers network topology without direct access. It targets web applications with poor error uniformity and assumes collected response logs from prior steps.

## Requirements

1. Saved response files from payload sends
2. Text editor or diff tool for comparison
3. Understanding of common error patterns (e.g., ECONNREFUSED vs. ETIMEDOUT)

## Defense

Defensive measures and detection strategies:

- Enforce generic error pages without technical details
- Log and alert on XML parsing errors
- Use WAF rules to block suspicious XML entities

## Objectives

1. Identify patterns in error messages
2. Correlate discrepancies to port status
3. Prepare data for port mapping

## Instructions

### Step 1: Collect and Review Responses

**Context**: Gather all response files and scan for error texts.

Open response files in a text editor and note key phrases.

> For example, a response for port 80 might show "Request timed out" (open), while port 22 shows "No route to host" (closed).

### Step 2: Compare Across Payloads

**Context**: Use manual diff or scripting to highlight differences.

For multiple ports, create a table:

| Port | Error Message | Inference |
|------|---------------|-----------|
| 80   | Timed out     | Open      |
| 22   | Refused       | Closed    |

> This step reveals which internal requests succeeded via OOB.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- error-analysis
- recon
