---
tags:
  - xxe
  - data-exfiltration
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 1d2dd6c9-ec82-4add-95ba-b52e37994225
created_at: '2025-12-13T09:00:27.809Z'
updated_at: '2025-12-13T09:00:27.809Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Analyze XXE Response for Leaked Data

## Summary

This procedure involves examining the server's response to an XXE injection attempt to extract and verify leaked sensitive data, such as file contents embedded in error messages.

## Description

After sending a malicious XXE payload, the server may return a 400 Bad Request with the requested file's contents included in the XML error response. This step focuses on parsing that response to confirm successful exploitation and gather intelligence. It applies to web applications vulnerable to XXE where responses leak data.

## Requirements

1. Captured response from XXE injection request
2. Basic text processing tools (e.g., grep or manual inspection)
3. Understanding of XML structure in error messages

## Defense

Defensive measures and detection strategies:

- Implement proper error handling to avoid leaking sensitive data in responses
- Use WAF rules to block XXE payloads
- Log and alert on 400 errors with unusual XML content

## Objectives

1. Verify successful file disclosure
2. Extract usable sensitive information
3. Assess further exploitation potential

## Instructions

### Step 1: Inspect Response Body

**Context**: Review the HTTP response for embedded file contents within the XML error structure.

> Manually check the response text for lines resembling file contents, such as user entries from /etc/passwd. Use tools like grep if automated: grep -E '^[a-z]+:x:' response.txt

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[xxe]]
- [[data-exfiltration]]
