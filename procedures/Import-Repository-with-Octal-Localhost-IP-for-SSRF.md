---
id: proc-uuid-1
tags:
  - ssrf
  - gitlab-import
  - octal-ip
type: procedure
tools:
  - '[[tools/ruby]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/import-url-octal]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:08:48.691Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# Import-Repository-with-Octal-Localhost-IP-for-SSRF

## Summary

This procedure exploits SSRF in GitLab's project import by using an octal IP notation for localhost (0177.1), bypassing Ruby's Resolv validation while triggering an OS-level connection to internal ports.

## Description

In GitLab, the project import feature clones repositories from user-provided URLs. A prior fix blocked standard localhost (127.0.0.1, localhost), but overlooked octal notations. Ruby's Resolv.getaddresses returns an empty array for '0177.1', passing the blacklist, but the OS resolves it via inet_aton during socket operations, enabling SSRF to ports like 22 for scanning internal services.

## Requirements

1. Authenticated GitLab account with project creation permissions
2. Target GitLab CE/EE instance (version with vulnerable import feature)
3. Access to browser or API for project import

## Defense

Defensive measures and detection strategies:

- Replace Resolv.getaddresses with Socket.getaddrinfo for OS-level validation
- Monitor import logs for malformed URLs and connection resets
- Rate-limit project imports and scan for internal IP attempts

## Objectives

1. Trigger SSRF to connect to internal localhost ports
2. Bypass IP blacklists using alternative notations
3. Enable reconnaissance of exposed internal services

## Instructions

### Step 1: Prepare Malformed URL

**Context**: Construct a URL using octal localhost to target an internal port, e.g., SSH on 22.

**Command** ([[commands/ruby-resolv-octal-ip]]):
```ruby
require "resolv"; Resolv.getaddress "0177.1"
```

> This confirms Resolv fails (expected: Resolv::ResolvError: no address for 0177.1), allowing bypass.

### Step 2: Initiate Project Import

**Context**: Create a new project and import from the malformed URL to trigger cloning.

**Command** ([[commands/import-url-octal]]):
```bash
# Via GitLab UI: New Project > Import Project > Enter URL: http://0177.1:22/
# Project path: {username}/{project}.git
```

> GitLab clones from the URL, attempting connection to 127.0.0.1:22. Expect failure if port closed.

### Step 3: Verify OS Resolution

**Context**: Test OS-level resolution to confirm SSRF potential.

**Command** ([[commands/ltrace-ping-octal-ip]]):
```bash
ltrace ping 0177.1 2>&1 | grep 0177.1
```

> Expected: inet_aton("0177.1", {0x100007f}) = 1, showing resolution to 127.0.0.1.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/ruby-resolv-octal-ip]]
- [[commands/import-url-octal]]
- [[commands/ltrace-ping-octal-ip]]

## Tools Used

- [[tools/irb]]
- [[tools/ltrace]]
- [[tools/ping]]

## Tags

- ssrf
- octal-bypass
- gitlab

