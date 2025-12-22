---
id: proc-identify-curl-flaw
tags:
  - curl
  - url-parsing
  - validation
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-parse-test]]'
verified: false
platforms:
  - Software Library
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:17.305Z'
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
# Identify-curl-URL-Parsing-Flaw

## Summary

This procedure identifies the CVE-2022-27780 flaw in curl's URL parser, where percent-encoded separators like %2F are accepted and decoded in the host name without validation, allowing potential URL manipulation.

## Description

In curl versions 7.80.0 to 7.83.0, a commit added support for percent-encoded IP literals in hosts but failed to reject decoded URL separators (e.g., '/'). This leads to the parser transposing the decoded characters into the path, altering the URL structure. The procedure involves reviewing the source or testing parsing to confirm the issue, applicable in auditing applications using libcurl for URL handling.

## Requirements

1. Vulnerable curl installation (7.80.0-7.83.0)
2. Access to curl trace output
3. Basic knowledge of URL encoding

## Defense

Defensive measures and detection strategies:

- Upgrade curl to 7.83.1 or later
- Implement custom URL validation rejecting encoded separators in hosts
- Monitor for anomalous URL patterns in logs

## Objectives

1. Confirm parser accepts invalid encoded hosts
2. Document the decoding behavior
3. Prepare for exploitation testing

## Instructions

### Step 1: Review Source Commit

**Context**: Examine the commit introducing the flaw to understand the root cause.

**Command** ([[commands/curl-parse-test]]):
```bash
curl --version
# Check version; then review commit 9a8564a920188e via git or source
```

> Outputs curl version; if vulnerable, proceed to test parsing. Expected: Version between 7.80.0 and 7.83.0.

### Step 2: Test Basic Parsing

**Context**: Send a URL with encoded separator to observe acceptance.

**Command** ([[commands/curl-parse-test]]):
```bash
curl -v "http://example.com%2Ftest" --trace-ascii - | grep Host
```

> Trace reveals host parsed without rejection. Expected: No error on %2F in host.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-parse-test]]

## Tools Used

- [[tools/curl]]

## Tags

- curl
- url-parsing
