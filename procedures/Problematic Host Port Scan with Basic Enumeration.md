---
id: 2f628342-775c-4ecf-b39d-f3f7f5c61c61
name: Problematic Host Port Scan with Basic Enumeration
type: procedure
verified: true
submitted: true
created_at: '2019-11-13T01:16:38.573559+00:00'
updated_at: '2023-05-26T00:41:58.455021+00:00'
tactics:
- '[[Discovery|TA0007 - Discovery]]'
techniques:
- '[[Network Service Scanning|T1046 - Network Service Scanning]]'
platforms:
- Linux
- Windows
tags:
- '[[Enumeration]]'
- '[[Network]]'
commands:
- '[[Nmap FIN Scan with Service Enumeration]]'
- '[[Nmap Scan Services with Hostgroup Template]]'
- '[[Nmap Scan Services with Host Timeout Template]]'
- '[[Nmap Scan Services with Max Rate Template]]'
- '[[Nmap Scan Services with Max Retries Template]]'
- '[[Nmap Scan Services with Min and Max Parallelism Templates]]'
- '[[Nmap Scan Services with Min and Max RTT Templates]]'
- '[[Nmap Scan Services with Min Rate Template]]'
- '[[Nmap Scan Services with Scan Delay Template]]'
- '[[Nmap Service Scan with Initial RTT Timeout Template]]'
---

# Problematic Host Port Scan with Basic Enumeration

**Status**: ✓ Verified

## Summary

Some systems can not be reliably scanned using standard Nmap scans, and will fail to disclose open ports. This is can be due to rate limiting, firewall rules, network congestion, etc. Nmap includes a number of templates designed to help when scanning problematic hosts, and should be used when a tar

## Description

# Description

Some systems can not be reliably scanned using standard Nmap scans, and will fail to disclose open ports. This is can be due to rate limiting, firewall rules, network congestion, etc. Nmap includes a number of templates designed to help when scanning problematic hosts, and should be used when a target is not responding on ports that are expected to be open. By specifying delays, maximum packets sent, maximum simultaneous scans, and other options, it may be possible to bypass issues that prohibit an accurate scan.

This procedure deals with various approaches to scanning problematic hosts. It should be noted that some scans may take much longer than usual.

# Instructions

## Max Retries

Specify the number of times a packet is re-sent to a port.

**Command** ([[Nmap Scan Services with Max Retries Template]]):

```bash
nmap -p- --max-retries 5 $_TARGET_IP
```

## Host timeout

Specify the amount of time before giving up on an unresponsive host

**Command** ([[Nmap Scan Services with Host Timeout Template]]):

```bash
nmap -p- --host-timeout 100ms $_TARGET_IP
```

## Hostgroup

Use the hostgroup templates to set the minimum and maximum number of simultaneous scans.

**Command** ([[Nmap Scan Services with Hostgroup Template]]):

```bash
nmap -p- --min-hostgroup 3 --max-hostgroup 4 $_TARGET_IP
```

## Scan Delay

Specify the time to delay each packet to attempt to bypass time based firewall rules. Experiment with different scan delay values if unsuccessful initially.

**Command** ([[Nmap Scan Services with Scan Delay Template]]):

```bash
nmap -p- --scan-delay 10s $TARGET_IP
```

## Maximum Rate

Specify the maximum number of packets that can be sent at once.

**Command** ([[Nmap Scan Services with Max Rate Template]]):

```bash
nmap -p- --max-rate 2 $_TARGET_IP
```

## Minimum Rate

Specify the minimum number of packets that can be sent at once.

**Command** ([[Nmap Scan Services with Min Rate Template]]):

```bash
nmap -p- --min-rate 2 $_TARGET_IP
```

## Parallelism

Specify the minimum and maximum number of packets to be sent in parallel.

**Command** ([[Nmap Scan Services with Min and Max Parallelism Templates]]):

```bash
nmap -p- --min-parallelism 2 --max-parallelism 2 $_TARGET_IP
```

## Round Trip Timeout

Specify the minimum and maximum time for a packet to return with a reply.

**Command** ([[Nmap Scan Services with Min and Max RTT Templates]]):

```bash
nmap -p- --min-rtt-timeout 5ms --max-rtt-timeout 100ms $_TARGET_IP
```

## Initial Round Trip Timeout

Specify the timeout for the initial round trip timeout. This value is distinct from min and max round trip timeout, as it specifies the time taken to reply, not for the packet's transmission.

**Command** ([[Nmap Service Scan with Initial RTT Timeout Template]]):

```bash
nmap -p- --initial-rtt-timeout 50ms $_TARGET_IP
```

## FIN Scan

Some firewalls may not display all ports when responding to a SYN scan. In such cases, a FIN scan may be preferable, as it sends a FIN packet rather than SYN, and based on the firewall's response, may be able to identify open ports.

**Command** ([[Nmap FIN Scan with Service Enumeration]]):

```bash
nmap -sV -sF -p- $_TARGET_IP
```

## Platforms

- Linux
- Windows

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery|TA0007 - Discovery]]

### Techniques

- [[Network Service Scanning|T1046 - Network Service Scanning]]

## Commands Used

- [[Nmap FIN Scan with Service Enumeration]]
- [[Nmap Scan Services with Hostgroup Template]]
- [[Nmap Scan Services with Host Timeout Template]]
- [[Nmap Scan Services with Max Rate Template]]
- [[Nmap Scan Services with Max Retries Template]]
- [[Nmap Scan Services with Min and Max Parallelism Templates]]
- [[Nmap Scan Services with Min and Max RTT Templates]]
- [[Nmap Scan Services with Min Rate Template]]
- [[Nmap Scan Services with Scan Delay Template]]
- [[Nmap Service Scan with Initial RTT Timeout Template]]

## Tags

- [[Enumeration]]
- [[Network]]
