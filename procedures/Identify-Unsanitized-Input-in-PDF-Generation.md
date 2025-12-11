---
tags:
  - ssrf
  - html-injection
  - vulnerability-discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-inject-ssrf-iframe]]'
  - '[[commands/aws-ssm-send-command]]'
platforms:
  - Web
  - AWS
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 3096558f-daad-4852-aa29-59fa623bbd73
created_at: '2025-12-11T06:10:22.564Z'
updated_at: '2025-12-11T06:10:22.564Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1190]]'
---
# Identify Unsanitized Input in PDF Generation

## Summary

This procedure involves testing the PDF generation feature for lack of input sanitization by submitting HTML tags and observing their reflection in error messages, setting the stage for SSRF exploitation.

## Description

In web applications using PDF conversion libraries, unsanitized user input in error messages can allow HTML injection. This is tested by providing invalid template values and checking if injected tags are processed without escaping during PDF rendering, potentially enabling SSRF to internal services like AWS metadata.

## Requirements

1. Access to the PDF generation endpoint.
2. Ability to submit POST requests with custom parameters.
3. Network access to the target web application.

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding for all user-supplied data.
- Use allowlists for URL validation in PDF generators to block internal requests.
- Monitor for anomalous requests to internal metadata services in logs.

## Objectives

1. Confirm presence of HTML injection vulnerability.
2. Identify potential for SSRF exploitation.
3. Gather evidence for reporting.

## Instructions

### Step 1: Test Input Reflection

**Context**: Submit a request with a test HTML tag to check for sanitization in error messages.

**Command** ([[commands/curl-inject-ssrf-iframe]]):
```bash
curl -X POST 'https://target.com/analytics/reports/generate' -d 'template=<b>test</b>' --header 'Content-Type: application/x-www-form-urlencoded'
```

> This command sends a POST request with a bold tag; check if it appears unescaped in the response or PDF.

### Step 2: Analyze Response

**Context**: Examine the generated PDF or error output for reflected input.

> If the HTML is rendered as-is, the vulnerability is confirmed; proceed to exploitation.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-inject-ssrf-iframe]]

## Tools Used



## Tags

- [[commands/curl-inject-ssrf-iframe]]
- [[html-injection]]
