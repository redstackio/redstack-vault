---
tags:
  - http-smuggling
  - behavior-observation
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-test-conflicting-headers]]'
platforms:
  - Linux
  - Windows
techniques:
  - '[[Adversary-in-the-Middle]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 2589b996-0881-482e-830a-2eb77fc41fd2
created_at: '2025-12-13T09:01:21.803Z'
updated_at: '2025-12-13T09:01:21.803Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Adversary-in-the-Middle]]'
---
# Observe cURL Header Behavior

## Summary

This procedure monitors cURL's handling of requests with conflicting headers to confirm it sends both without rejection, using chunked encoding while retaining Content-Length.

## Description

By enabling verbose output, observe that cURL does not validate or remove the conflicting Content-Length header when Transfer-Encoding is set to chunked. This can be exploited in environments with proxies that prioritize different headers, leading to smuggling.

## Requirements

1. cURL installed and configured
2. Test request from prior step
3. Ability to inspect command output

## Defense

Defensive measures and detection strategies:

- Monitor for anomalous HTTP headers in logs
- Use WAF rules to detect conflicting headers

## Objectives

1. Verify header presence in sent request
2. Confirm no rejection by cURL
3. Identify exploitation potential

## Instructions

### Step 1: Monitor Request Output

**Context**: Run the request and inspect verbose output for header confirmation.

**Command** ([[commands/curl-test-conflicting-headers]]):
```bash
curl -v -X POST -H "Transfer-Encoding: chunked" -H "Content-Length: 100" -d "0\r\n\r\nSMUGGLED_PAYLOAD" http://example.com/test
```

> The verbose output will show both headers and the processing details. Look for lines indicating headers sent and chunked encoding used.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Adversary-in-the-Middle]]

### Sub-Techniques



## Commands Used

- [[commands/curl-test-conflicting-headers]]

## Tools Used

- [[tools/curl]]

## Tags

- [[http-smuggling]]
- [[behavior-observation]]
