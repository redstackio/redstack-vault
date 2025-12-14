---
tags:
  - dos
  - verification
  - nmap
type: procedure
tools:
  - '[[tools/nmap]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/nmap-scan-for-service-verification]]'
verified: false
platforms:
  - Linux
  - Network
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:48.333Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: c8fcf55d-c5a5-44a3-8d65-431c3bd3b73a
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Verify-DoS-with-Nmap-Scan

## Summary

This procedure uses nmap to scan the target network and EdgeRouter ports post-exploitation, confirming ports appear open but services (web, SSH, DHCP, DNS) are non-responsive due to resource exhaustion DoS.

## Description

After /run and /var/log are filled, the device halts services despite open ports. Nmap SYN scan shows ports like 53, 67, 80, 443 as open/filtered, but actual connections (e.g., HTTP requests, SSH logins, DHCP leases) fail. Recovery needs power cycle or deleting files in /var/run/beaker/container_file/.

## Requirements

1. Nmap installed on attacker's machine
2. Network access to scan the local subnet (e.g., 192.168.1.0/24)
3. Post-DoS state from prior procedures

## Defense

Defensive measures and detection strategies:

- Implement service health checks and auto-reboot on high resource usage
- Block excessive scans with firewall rules
- Log and alert on port scans combined with high disk I/O
- Regular cleanup of /var/run/beaker/ to prevent buildup

## Objectives

1. Validate DoS by showing open ports with no service response
2. Confirm impact on multiple services (DHCP, SSH, etc.)
3. Document the attack's effectiveness

## Instructions

### Step 1: Perform SYN Scan

**Context**: Scan key ports on the router and network to check status.

**Command** ([[commands/nmap-scan-for-service-verification]]):
```bash
nmap -sS -p 22,53,67,80,443 192.168.1.0/24
```

> This stealth SYN scan targets SSH (22), DNS (53), DHCP (67), HTTP (80), HTTPS (443). Expected: Ports open on router (192.168.1.1) but no further responses.

### Step 2: Test Service Responsiveness

**Context**: Manually probe services to confirm failure.

No command; try `ssh admin@192.168.1.1`, `curl http://192.168.1.1/`, or DHCP request via client.

> Expect timeouts or refusals despite open ports.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used

- [[commands/nmap-scan-for-service-verification]]

## Tools Used

- [[tools/nmap]]

## Tags

- dos
- verification
- network-scan
