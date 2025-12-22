---
id: 918bd23b-4f51-4bf1-b5e4-99c53eb27eb4
name: Nmap-Identify-Web-Response-Headers
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T19:08:46.868113+00:00'
updated_at: '2023-05-26T15:57:43.937610+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Network Service Scanning]]'
sub_techniques: []
tags:
  - HTTP Headers
  - owasp
  - owasp top 10
  - Web Applications
  - reconnaissance
  - nmap
commands:
  - '[[commands/nmap-identify-http-headers]]'
platforms:
  - Web
tools:
  - '[[tools/Nmap]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Nmap-Identify-Web-Response-Headers

## Summary

This procedure uses Nmap's http-headers script to enumerate HTTP response headers from web servers, revealing server technologies, versions, and security configurations such as exposed software details that could aid in further reconnaissance or vulnerability identification.

## Description

HTTP response headers provide critical information about the web server's software stack, including server type (e.g., Apache, Nginx), versions, modules, and security headers like Content-Security-Policy or X-Frame-Options. The Nmap http-headers script performs a HEAD request to targeted ports (typically 80 and 443) and parses the response headers, helping attackers map the attack surface during reconnaissance. This technique is commonly used in web application assessments to identify misconfigurations or outdated components that may be exploitable. It assumes network access to the target and focuses on non-intrusive scanning to avoid detection.

## Requirements

1. Network connectivity to the target web server (ports 80/443 open).
2. Nmap installed with NSE (Nmap Scripting Engine) support.
3. Basic knowledge of IP addressing and port scanning.
4. No authentication required for public-facing web servers.

## Defense

Defensive measures and detection strategies:

- Configure web servers to minimize header exposure (e.g., remove Server token in Apache/Nginx).
- Implement Web Application Firewalls (WAF) to detect and block Nmap scans.
- Monitor network logs for unusual HEAD requests or port scans using tools like Snort or Suricata.
- Use security headers to obscure server details without revealing vulnerabilities.

## Objectives

1. Identify web server software and versions from response headers.
2. Detect potential security misconfigurations in headers (e.g., missing HSTS).
3. Gather intelligence for targeted exploitation in subsequent attack phases.

## Instructions

### Step 1: Verify Target and Prerequisites

**Context**: Confirm the target IP or domain is reachable and Nmap is ready. This ensures the scan targets the correct asset and avoids unnecessary noise.

Run a basic ping or connectivity check if needed, but for Nmap, proceed directly if the target is known.

> No specific command here; use [[tools/Nmap]] documentation for installation verification.

### Step 2: Execute Nmap Scan for HTTP Headers

**Context**: Launch the Nmap scan using the http-headers script combined with service version detection (-sV) to enumerate headers on open web ports. This step sends HEAD requests to ports 80/tcp and 443/tcp, parsing responses for header details.

**Command** ([[commands/nmap-identify-http-headers]]):
```bash
nmap -sV --script=http-headers $_TARGET
```

> This command detects services with -sV and runs the http-headers NSE script. Replace $_TARGET with the IP or hostname. Expected output includes port states, service versions, and a breakdown of headers like Server, Date, Content-Type. Look for indicators of outdated software (e.g., old Apache versions) or missing security headers.

### Step 3: Analyze and Document Results

**Context**: Review the scan output to identify actionable intelligence, such as exposed versions that match known CVEs. This step involves manual parsing or piping output to a file for further analysis.

Save output to a file for review:
```bash
nmap -sV --script=http-headers $_TARGET -oN headers_scan.txt
```

> Open the output file and search for headers like "Server:" or "X-Powered-By:". Cross-reference versions with vulnerability databases (e.g., CVE search). If headers reveal PHP or specific modules, note them for targeted exploits.

Decision point: If no web ports are open, expand the scan with -p- for all ports; otherwise, proceed to vulnerability scanning procedures.
