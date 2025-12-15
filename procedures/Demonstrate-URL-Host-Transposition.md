---
id: proc-demonstrate-transposition
tags:
  - curl
  - url-transposition
  - demo
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-transpose-demo]]'
verified: false
platforms:
  - Software Library
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:17.302Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Demonstrate-URL-Host-Transposition

## Summary

This procedure demonstrates how curl transposes a percent-encoded separator in the host name into the path, altering the effective URL (e.g., http://example.com%2F127.0.0.1/ becomes http://example.com/127.0.0.1/).

## Description

The flaw causes the parser to decode %2F early and shift subsequent parts, changing the host from 'example.com%2F127.0.0.1' to 'example.com' with path '/127.0.0.1/'. This is key for understanding bypass potential in filtered environments. Test in isolated curl or libcurl-integrated apps.

## Requirements

1. Vulnerable curl version
2. Ability to capture verbose output
3. Sample target URL

## Defense

Defensive measures and detection strategies:

- Validate URLs pre-parsing with strict host regex
- Log and alert on encoded separators in hosts
- Use updated libcurl with fix

## Objectives

1. Visualize URL alteration
2. Confirm transposition effect
3. Generate proof-of-concept traces

## Instructions

### Step 1: Craft Malformed URL

**Context**: Build URL with encoded separator in host.

**Command** ([[commands/curl-transpose-demo]]):
```bash
echo "http://example.com%2F127.0.0.1/" > test.url
cat test.url
```

> Displays the input URL for verification.

### Step 2: Parse and Trace

**Context**: Execute curl to observe decoded transposition.

**Command** ([[commands/curl-transpose-demo]]):
```bash
curl -v "http://example.com%2F127.0.0.1/" --trace-ascii - > trace.txt
grep -i "host\|url" trace.txt
```

> Output shows effective host as example.com and path including 127.0.0.1. Expected: Transposed URL in trace.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-transpose-demo]]

## Tools Used

- [[tools/curl]]

## Tags

- curl
- transposition
