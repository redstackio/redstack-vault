---
type: procedure
description: >-
  Uses Nmap's ssl-enum-ciphers script to scan and analyze SSL/TLS configurations
  on web servers for misconfigurations like weak ciphers.
verified: true
submitted: true
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - ssl
  - tls
  - nmap
  - reconnaissance
  - web-applications
  - owasp
  - owasp-top-10
commands:
  - '[[commands/nmap-enum-ssl-tls-ciphers]]'
tools:
  - '[[tools/Nmap]]'
platforms:
  - Web
skill_level: beginner
impact_level: low
detection_risk: low
created_at: '2020-09-03T14:25:24.589585+00:00'
updated_at: '2023-05-26T18:52:13.527834+00:00'
validated: true
---

# Enumerate-SSL-TLS-Ciphers-with-Nmap-Script

## Summary

This procedure employs Nmap's built-in ssl-enum-ciphers script to perform an active scan of a target web server's SSL/TLS configuration. It enumerates supported protocol versions (e.g., TLS 1.0, 1.1, 1.2, 1.3) and cipher suites, assigning security grades to highlight potential misconfigurations such as support for deprecated protocols or weak ciphers like RC4 or 3DES. This is useful for reconnaissance in penetration testing to identify vulnerabilities that could lead to man-in-the-middle attacks or protocol downgrade exploits.

## Description

SSL/TLS is crucial for securing communications between clients and web servers, but improper configurations can expose systems to risks. The ssl-enum-ciphers script connects to the target's HTTPS port, negotiates handshakes with various cipher suites, and reports the results in a graded format (A-F) based on security best practices. This procedure targets public-facing web applications and requires only network connectivity to the standard HTTPS port (443). It maps to MITRE ATT&CK's Active Scanning technique, aiding in the discovery of host information during reconnaissance phases. Outcomes include a list of supported ciphers, enabling further assessment of compliance with standards like PCI-DSS or OWASP guidelines.

## Requirements

1. Nmap version 6.0 or later installed on the attacker's machine.
2. Network access to the target web server's HTTPS port (default 443).
3. Basic knowledge of SSL/TLS protocols to interpret results.
4. Optional: Firewall rules allowing outbound connections from the scanner to the target.

## Defense

Defensive measures include configuring servers to support only strong ciphers (e.g., AES-GCM) and modern TLS versions (1.2+), disabling legacy protocols via server configurations (e.g., Apache's SSLProtocol directive). Detection strategies involve monitoring network traffic for unusual port probes using tools like Snort or Suricata rules targeting Nmap signatures, logging SSL handshakes, and implementing rate limiting on HTTPS endpoints to thwart scanning attempts.

## Objectives

1. Identify all supported SSL/TLS protocol versions on the target server.
2. Enumerate and grade the strength of supported cipher suites.
3. Detect misconfigurations that could enable cryptographic attacks.
4. Generate a report for remediation recommendations.

## Instructions

### Step 1: Identify Target and Verify Accessibility

**Context**: Before scanning, confirm the target's hostname or IP and ensure the HTTPS service is reachable. This step prevents wasted scans on non-responsive hosts and focuses efforts on valid web applications.

Use a basic connectivity check with tools like telnet or curl to verify port 443 is open.

**Expected Output**: Successful connection confirmation, e.g., a 200 OK response or handshake initiation.

### Step 2: Execute Nmap SSL/TLS Cipher Enumeration

**Context**: Run the core scan using Nmap's ssl-enum-ciphers script to probe the target's SSL/TLS implementation. This step performs multiple handshake attempts to discover supported configurations without exploiting vulnerabilities.

**Command** ([[commands/nmap-enum-ssl-tls-ciphers]]):
```bash
nmap --script ssl-enum-ciphers $_TARGET:$_PORT
```

> This command initiates the script, which outputs supported protocols, ciphers, and an overall security grade. Replace placeholders with actual values (e.g., demo.testfire.net:443). The scan may take 1-5 minutes depending on the target's responsiveness.

### Step 3: Analyze Scan Results for Misconfigurations

**Context**: Review the output to identify weak elements, such as support for TLS 1.0 or low-grade ciphers. This involves manual inspection or piping output to grep for keywords like "A-" or "weak".

For example, pipe the output to search for insecure ciphers:
```bash
grep -i "rc4\|3des\|md5" output.txt
```

**Expected Output**: Flagged weak ciphers or protocols, e.g., warnings about fallback to SSLv3.

### Step 4: Document and Recommend Remediations

**Context**: Compile findings into a report, noting any F or E grades, and suggest fixes like updating server cipher lists.

Save the full output to a file for reference:
```bash
nmap --script ssl-enum-ciphers $_TARGET:$_PORT > ssl_scan_results.txt
```

**Expected Output**: A documented report with prioritized issues, e.g., "Disable TLS 1.0 to improve grade from C to A".
