---
tags:
  - file-upload
  - testing
type: procedure
tools:
  - '[[tools/sqlmap]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sqlmap-tamper-htmlencode]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: ec0dad4a-82d0-44e6-880e-25b3d5f9bbd7
created_at: '2025-12-11T06:10:30.918Z'
updated_at: '2025-12-11T06:10:30.918Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Test Unrestricted File Uploads in XML Endpoint

## Summary

This procedure tests for unrestricted file uploads by attempting to upload malicious files and observing server behavior.

## Description

In the context of XML-processing endpoints, uploads are tested to see if non-XML files like PHP shells are accepted or parsed, revealing potential vulnerabilities.

## Requirements

1. Access to the upload endpoint
2. Sample malicious files (e.g., PHP shell)
3. HTTP client like curl or Burp Suite

## Defense

Defensive measures and detection strategies:

- Enforce strict file type validation
- Monitor upload logs for suspicious file types

## Objectives

1. Determine if files are saved or processed
2. Identify parsing behavior
3. Expose error messages

## Instructions

### Step 1: Attempt Malicious Upload

**Context**: Upload a PHP shell to test restrictions.

Use curl to upload:

```bash
curl -F "file=@shell.php" https://target/upload
```

> Observe if the file is processed as XML with errors.

### Step 2: Analyze Response

**Context**: Check for verbose error messages.

Review server responses for indications of XML parsing.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used



## Tags

- [[file-upload]]
- [[testing]]
