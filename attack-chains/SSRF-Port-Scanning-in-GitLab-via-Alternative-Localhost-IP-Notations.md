---
tags:
  - ssrf
  - gitlab
  - localhost-bypass
  - port-scanning
  - ruby-resolv
type: attack_chain
tools:
  - '[[tools/irb]]'
  - '[[tools/ltrace]]'
  - '[[tools/ping]]'
  - '[[tools/nc]]'
  - '[[tools/ruby]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Import-Repository-with-Octal-Localhost-IP-for-SSRF]]'
  - '[[procedures/Analyze-Cloning-Error-to-Confirm-SSRF]]'
  - '[[procedures/Bypass-SSRF-Filters-with-Hex-and-Decimal-IPs]]'
step_count: 3
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:08:48.699Z'
description: >-
  Multi-stage attack exploiting SSRF in GitLab's project import feature by using
  octal, hexadecimal, and decimal representations of localhost to bypass IP
  validation filters, enabling internal port scanning.
id: 2fd36242-2066-468a-b109-0e9fa5ee5e35
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Active Scanning]]'
---
# SSRF Port Scanning in GitLab via Alternative Localhost IP Notations

Multi-stage attack chain demonstrating exploitation of an SSRF vulnerability in GitLab's project import feature. Attackers bypass IP validation by using non-standard localhost representations (octal, hex, decimal), allowing connections to internal ports for reconnaissance.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Prepare Malformed URL] --> B[Trigger Import with Octal IP]
    B --> C[Observe Connection Error]
    C --> D[Repeat with Hex/Decimal IPs for Scanning]
    D --> E[Internal Port Access Confirmed]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
    style E fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/irb]]
- [[tools/ltrace]]
- [[tools/ping]]
- [[tools/nc]]
- [[tools/ruby]]

### Target Environment

- GitLab CE/EE instance (e.g., gitlab.com)
- Required services/ports: Port 22 (SSH) or other internal ports
- Network access requirements: Authenticated access to GitLab project creation

### Initial Access Requirements

- Valid GitLab user account
- Ability to create new projects
- No prior internal access needed; exploits public-facing import feature

## Detailed Attack Procedures

### Step 1: Trigger SSRF with Octal IP Notation
procedure: [[procedures/Import-Repository-with-Octal-Localhost-IP-for-SSRF]]

**Objective**: Bypass GitLab's localhost filter by importing a repository using an octal IP representation, forcing a connection to an internal port like 22.

**Instructions**: Create a new project in GitLab and attempt to import from a URL like `http://0177.1:22/`. This uses the octal notation for 127.0.0.1, which evades Ruby's Resolv validation but resolves at the OS level.

**Expected Output**: GitLab attempts to clone, resulting in a connection reset error indicating internal access.

**Success Indicators**:
- Error message shows cloning failure with "Connection reset by peer"
- Confirms connection to localhost:22

### Step 2: Confirm SSRF via Error Analysis
procedure: [[procedures/Analyze-Cloning-Error-to-Confirm-SSRF]]

**Objective**: Analyze the import error to verify that an internal connection was attempted, proving the SSRF bypass.

**Instructions**: After the import fails, review the error logs or UI message for details like "fatal: unable to access 'http://0177.1:22/': Recv failure: Connection reset by peer". Use [[commands/ruby-resolv-octal-ip]] to test why Resolv fails:

```ruby
require "resolv"; Resolv.getaddress "0177.1"
```

Then trace OS resolution with [[commands/ltrace-ping-hex-ip]] on a test system:

```bash
ltrace ping 0x7f.1 2>&1 | grep 0x7f.1
```

**Expected Output**: Resolv error (no address) but ltrace shows inet_aton resolving to 127.0.0.1.

**Success Indicators**:
- Resolv returns empty/no address
- OS traces confirm resolution to localhost

### Step 3: Extend Bypass with Hex and Decimal IPs
procedure: [[procedures/Bypass-SSRF-Filters-with-Hex-and-Decimal-IPs]]

**Objective**: Repeat the import with hexadecimal (0x7f.1) and decimal (2130706433) notations to scan multiple internal ports and expand reconnaissance.

**Instructions**: In the project import field, use URLs like `http://0x7f.1:22/` or `http://2130706433:80/`. Test resolution locally with [[commands/ruby-resolv-hex-ip]] and [[commands/ruby-resolv-decimal-ip]] to confirm bypass:

```ruby
require "resolv"; Resolv.getaddress "0x7f.1"
```

Set up a listener with [[commands/nc-listen-port-80]] to capture requests:

```bash
echo -e "HTTP/1.1 200 OK\n\nHello from netcat :)" | sudo nc -l 80
```

**Expected Output**: Similar cloning errors for each notation, with potential response from listener if port is open.

**Success Indicators**:
- Multiple notations bypass validation
- Internal ports scanned successfully
- Listener captures SSRF traffic

## Attack Chain Summary

### Key Achievements

1. Bypassed GitLab's SSRF protection using alternative IP formats
2. Confirmed internal connections via error analysis and OS tracing
3. Enabled port scanning for further reconnaissance on GitLab instances

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Active Scanning]] Active Scanning

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Reconnaissance]] Reconnaissance

---
*Last updated: 2023-10-01T00:00:00Z*
