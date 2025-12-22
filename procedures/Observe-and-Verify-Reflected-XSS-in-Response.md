---
id: proc-observe-xss-response
name: Observe-and-Verify-Reflected-XSS-in-Response
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:31.875Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[JavaScript]]'
sub_techniques: []
tags:
  - xss
  - reflected-xss
  - debugging
commands:
  - '[[commands/gdb-print-vec]]'
  - '[[commands/gdb-print-payload]]'
platforms:
  - Web
tools:
  - '[[tools/GDB]]'
skill_level: advanced
impact_level: high
detection_risk: medium
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[JavaScript]]'
---

# Observe-and-Verify-Reflected-XSS-in-Response

## Summary

This procedure captures the server's response after sending a malformed chunked request and verifies the XSS payload reflection, optionally using GDB to inspect the response brigade for root cause confirmation.

## Description

Upon receiving the crafted request, Apache with PHP generates a 400 Bad Request due to parsing issues, but the unconsumed payload is appended to the response via brigade mishandling. Observation confirms the script executes in a browser context, while GDB debugging reveals the payload in the iovec structure, proving the vulnerability in sapi_apache2.c.

## Requirements

1. Prior request sent and response pending
2. GDB installed and permissions to attach to Apache process
3. Access to server logs or memory for verification

## Defense

Defensive measures and detection strategies:

- Log all 400 responses and scan for script tags
- Use WAF to block chunked requests with mismatched lengths
- Harden brigade handling in custom PHP modules

## Objectives

1. Confirm payload reflection in HTTP response
2. Validate JS execution potential
3. Debug memory to expose root cause

## Instructions

### Step 1: Monitor Response in nc Session

**Context**: After sending the request, observe the output in the Netcat session for the reflected payload.

**Command** (No specific command; observe output):

> The response will show standard 400 HTML followed by '<script>alert(1)</script>\r\n'. Expected: Payload appended after error message, confirming injection.

### Step 2: Attach GDB and Inspect Brigade

**Context**: For verification, attach GDB to the Apache process during request handling and print the vector containing the payload.

**Command** ([[commands/gdb-print-vec]]):
```bash
gdb -p $(pgrep httpd)
p vec[2]
```

> Prints the iovec array index; expected: '{iov_base = 0x7f5115c1b17b, iov_len = 27}' showing payload storage.

### Step 3: Print Payload from Memory

**Context**: Cast and display the memory contents to confirm the exact XSS string.

**Command** ([[commands/gdb-print-payload]]):
```bash
p (char *)0x7f5115c1b17b
```

> Displays the string at the address; expected: '"<script>alert(1)</script>\r\n"' verifying the injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/gdb-print-vec]]
- [[commands/gdb-print-payload]]

## Tools Used

- [[tools/GDB]]

## Tags

- [[xss]]
- [[debugging]]
