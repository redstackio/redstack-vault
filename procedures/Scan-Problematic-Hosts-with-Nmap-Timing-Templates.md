---
type: procedure
verified: true
tactics:
  - '[[tactics/Discovery|TA0007 - Discovery]]'
techniques:
  - '[[techniques/Network Service Scanning|T1046 - Network Service Scanning]]'
tags:
  - Enumeration
  - Network
commands:
  - '[[commands/nmap-fin-scan-with-service-enumeration]]'
  - '[[commands/nmap-scan-with-hostgroup-template]]'
  - '[[commands/nmap-scan-with-host-timeout-template]]'
  - '[[commands/nmap-scan-with-max-rate-template]]'
  - '[[commands/nmap-scan-with-max-retries-template]]'
  - '[[commands/nmap-scan-with-min-max-parallelism-template]]'
  - '[[commands/nmap-scan-with-min-max-rtt-timeout-template]]'
  - '[[commands/nmap-scan-with-min-rate-template]]'
  - '[[commands/nmap-scan-with-scan-delay-template]]'
  - '[[commands/nmap-scan-with-initial-rtt-timeout-template]]'
platforms:
  - Linux
  - Windows
tools:
  - '[[tools/Nmap]]'
skill_level: intermediate
impact_level: low
detection_risk: medium
validated: true
---

# Scan-Problematic-Hosts-with-Nmap-Timing-Templates

## Summary

This procedure uses specialized Nmap timing and scan templates to enumerate open ports and services on hosts that do not respond well to standard scans, often due to rate limiting, firewalls, or network congestion. By adjusting parameters like retries, delays, and parallelism, it increases the chances of accurate discovery without triggering excessive alerts.

## Description

Standard Nmap port scans may fail on certain hosts because of protective measures like intrusion detection systems (IDS), firewalls that drop packets, or network throttles that limit scan speed. This procedure outlines multiple Nmap timing templates to mitigate these issues, allowing for reliable network service discovery in reconnaissance phases. It is particularly useful in red team engagements where initial scans yield incomplete results, and targets are expected to have open ports based on prior intelligence. Each template targets a specific evasion or optimization aspect, and users should experiment iteratively, starting with conservative settings to avoid detection.

## Requirements

1. Network access to the target host (e.g., from an external or internal vantage point).
2. Nmap installed and updated to the latest version.
3. Basic knowledge of networking concepts like TCP flags and timing parameters.
4. Optional: Privileged access for raw socket operations (root/admin on Linux/Windows).

## Defense

Defensive measures include configuring firewalls to drop anomalous scan packets (e.g., FIN scans), implementing rate limiting on edge devices, and deploying IDS/IPS tools like Snort or Suricata to alert on slow or fragmented scans. Network segmentation and anomaly-based detection can further reduce the effectiveness of these templates.

## Objectives

1. Identify open ports and services on unresponsive or protected hosts.
2. Bypass basic scan evasion techniques without increasing noise excessively.
3. Gather actionable intelligence for subsequent exploitation phases.

## Instructions

### Step 1: Adjust Max Retries for Packet Reliability

**Context**: When hosts intermittently drop packets due to congestion, increasing retries ensures more reliable responses without speeding up the scan.

**Command** ([[commands/nmap-scan-with-max-retries-template]]):
```bash
nmap -p- --max-retries 5 $_TARGET_IP
```

> This command retries failed probes up to 5 times, helping in noisy networks. Expect a full port scan report; success is indicated by fewer 'filtered' ports compared to default scans.

### Step 2: Set Host Timeout for Quick Failure on Dead Hosts

**Context**: For hosts that appear unresponsive, a short timeout prevents wasting time on false positives while focusing on viable targets.

**Command** ([[commands/nmap-scan-with-host-timeout-template]]):
```bash
nmap -p- --host-timeout 100ms $_TARGET_IP
```

> Limits per-host scanning to 100ms, useful for batch scanning multiple IPs. Output shows quick 'host down' if unresponsive, or partial results if partially reachable.

### Step 3: Control Parallelism with Hostgroup Limits

**Context**: Limits simultaneous host probes to avoid overwhelming the network or triggering rate limits.

**Command** ([[commands/nmap-scan-with-hostgroup-template]]):
```bash
nmap -p- --min-hostgroup 3 --max-hostgroup 4 $_TARGET_IP
```

> Scans 3-4 hosts in parallel if multiple targets; for single host, it paces port probes. Look for balanced discovery of open ports without timeouts.

### Step 4: Introduce Scan Delays to Evade Time-Based Filters

**Context**: Firewalls may block rapid probes; adding delays mimics legitimate traffic.

**Command** ([[commands/nmap-scan-with-scan-delay-template]]):
```bash
nmap -p- --scan-delay 10s $_TARGET_IP
```

> Delays 10 seconds between probes, ideal for strict IDS. Scans take longer but yield more accurate open/closed states.

### Step 5: Limit Maximum Packet Rate

**Context**: Caps outgoing packets to stay under network or host thresholds.

**Command** ([[commands/nmap-scan-with-max-rate-template]]):
```bash
nmap -p- --max-rate 2 $_TARGET_IP
```

> Sends no more than 2 packets per second. Expected: Slower but stealthier scan with detailed port states.

### Step 6: Enforce Minimum Packet Rate for Consistency

**Context**: Ensures steady pacing to avoid bursty traffic that alerts monitors.

**Command** ([[commands/nmap-scan-with-min-rate-template]]):
```bash
nmap -p- --min-rate 2 $_TARGET_IP
```

> Maintains at least 2 packets per second. Useful in low-latency environments; output should show consistent timing.

### Step 7: Tune Probe Parallelism

**Context**: Controls concurrent probes per port to balance speed and stealth.

**Command** ([[commands/nmap-scan-with-min-max-parallelism-template]]):
```bash
nmap -p- --min-parallelism 2 --max-parallelism 2 $_TARGET_IP
```

> Keeps exactly 2 parallel probes. Results in even distribution of efforts, reducing detection risk.

### Step 8: Adjust RTT Timeouts for Latency Handling

**Context**: Adapts to variable network latency by setting response wait times.

**Command** ([[commands/nmap-scan-with-min-max-rtt-timeout-template]]):
```bash
nmap -p- --min-rtt-timeout 5ms --max-rtt-timeout 100ms $_TARGET_IP
```

> Waits 5-100ms for round-trip responses. Ideal for mixed latency; expect fewer false negatives on open ports.

### Step 9: Set Initial RTT Timeout

**Context**: Fine-tunes the first probe's wait time, distinct from ongoing RTT.

**Command** ([[commands/nmap-scan-with-initial-rtt-timeout-template]]):
```bash
nmap -p- --initial-rtt-timeout 50ms $_TARGET_IP
```

> Uses 50ms for initial probes to quickly gauge responsiveness. Output reflects faster startup with accurate early results.

### Step 10: Perform FIN Scan for Firewall Evasion

**Context**: Bypasses some stateful firewalls that mishandle FIN packets instead of SYN.

**Command** ([[commands/nmap-fin-scan-with-service-enumeration]]):
```bash
nmap -sV -sF -p- $_TARGET_IP
```

> Sends FIN packets and enumerates services on open ports. Success: Reveals ports hidden from SYN scans, with version details.
