---
id: proc-uuid-2
tags:
  - ssrf
  - error-analysis
  - connection-reset
type: procedure
tools:
  - '[[tools/ruby]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/check-clone-error]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:08:48.687Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Analyze-Cloning-Error-to-Confirm-SSRF

## Summary

This procedure examines the error output from a failed GitLab repository import to confirm SSRF, where connection resets indicate an attempt to access internal localhost ports.

## Description

After triggering the import with a malformed URL, GitLab's cloning process fails with a specific error revealing the internal connection. This step validates the bypass by correlating the error with local resolution tests, highlighting the discrepancy between Ruby Resolv and OS inet_aton.

## Requirements

1. Recent failed import attempt in GitLab
2. Access to error messages in UI or logs
3. Local Ruby environment for testing

## Defense

Defensive measures and detection strategies:

- Log all import URLs and flag non-standard IPs
- Implement WAF rules for octal/hex/decimal patterns in URLs
- Alert on frequent cloning failures with internal error signatures

## Objectives

1. Identify SSRF indicators in error messages
2. Correlate with local resolution behaviors
3. Confirm vulnerability for further exploitation

## Instructions

### Step 1: Review Import Error

**Context**: Check the GitLab UI or logs for the cloning failure details.

**Command** ([[commands/check-clone-error]]):
```bash
# Expected error in GitLab logs/UI:
# Cloning into bare repository '/path/{username}/{project}.git'...
# fatal: unable to access 'http://0177.1:22/': Recv failure: Connection reset by peer
```

> The "Connection reset by peer" confirms an active connection to localhost:22 was attempted.

### Step 2: Test Baseline Resolution

**Context**: Use Ruby to verify why the filter was bypassed.

**Command** ([[commands/ruby-resolv-standard-ip]]):
```ruby
require 'resolv'; Resolv.getaddresses("127.0.0.1")
```

> Expected: ["127.0.0.1"], showing standard IPs are blocked correctly.

### Step 3: Contrast with Malformed

**Context**: Repeat for the octal to see empty result.

**Command** ([[commands/ruby-resolv-octal-ip]]):
```ruby
require "resolv"; Resolv.getaddress "0177.1"
```

> Expected: Resolv::ResolvError, allowing the URL to pass validation.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/check-clone-error]]
- [[commands/ruby-resolv-standard-ip]]
- [[commands/ruby-resolv-octal-ip]]

## Tools Used

- [[tools/irb]]

## Tags

- ssrf-confirmation
- error-log
- resolv-test

