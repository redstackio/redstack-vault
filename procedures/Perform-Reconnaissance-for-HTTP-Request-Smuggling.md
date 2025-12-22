---
tags:
  - http-request-smuggling
  - reconnaissance
  - web-vuln
type: procedure
tools:
  - '[[tools/Smuggler]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/smuggler-test-url]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 8b876879-262f-41f6-b934-b0d50c4c8806
created_at: '2025-12-13T09:01:26.247Z'
updated_at: '2025-12-13T09:01:26.247Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Perform Reconnaissance for HTTP Request Smuggling

## Summary

This procedure involves using specialized tools to scan and test web endpoints for HTTP Request Smuggling vulnerabilities, focusing on desyncs between frontend and backend servers in processing headers like Transfer-Encoding and Content-Length.

## Description

In this attack scenario, reconnaissance is performed on Slack web assets to identify potential smuggling vulnerabilities. The procedure targets advanced exploits by running exhaustive tests, which can reveal mismatches in header interpretation leading to request smuggling. Prerequisites include access to the target URL over HTTPS and the smuggler tool installed. Expected outcomes include logs of test failures indicating vulnerable configurations.

## Requirements

1. Internet access to the target URL (e.g., https://slackb.com)
2. Smuggler tool installed and configured
3. Basic understanding of HTTP headers and smuggling techniques

## Defense

Defensive measures and detection strategies:

- Implement strict header validation in web servers and proxies
- Monitor for anomalous HTTP requests with malformed headers in logs

## Objectives

1. Identify potential HTTP Request Smuggling vulnerabilities
2. Gather data on desync behaviors for further exploitation
3. Confirm target susceptibility to advanced exploits

## Instructions

### Step 1: Run Smuggler Tool on Target

**Context**: Execute the smuggler tool to perform automated tests for smuggling vulnerabilities.

**Command** ([[commands/smuggler-test-url]]):
```bash
smuggler -u https://slackb.com
```

> This command targets the specified URL and runs tests for desyncs, outputting results on potential vulnerabilities like CL.TE.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/smuggler-test-url]]

## Tools Used

- [[tools/Smuggler]]

## Tags

- http-request-smuggling
- reconnaissance
