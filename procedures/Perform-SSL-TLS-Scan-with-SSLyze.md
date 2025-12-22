---
id: 3e4f1bfb-c209-407a-9f02-5cd38a8909a1
name: Perform-SSL-TLS-Scan-with-SSLyze
type: procedure
verified: true
submitted: true
created_at: '2020-09-03T13:49:07.614494+00:00'
updated_at: '2023-05-26T18:22:32.819104+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - ssl
  - tls
  - scanning
  - reconnaissance
  - owasp
  - web-applications
commands:
  - '[[commands/sslyze-regular-scan]]'
platforms:
  - Web
tools:
  - '[[tools/SSLyze]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Perform-SSL-TLS-Scan-with-SSLyze

## Summary

This procedure uses the SSLyze tool to perform a comprehensive scan of a target's SSL/TLS configuration, identifying misconfigurations such as weak ciphers, vulnerable protocols, certificate issues, and other security weaknesses that could lead to man-in-the-middle attacks or data exposure.

## Description

SSL/TLS is critical for secure communication between clients and servers, but misconfigurations can expose sensitive data to interception or exploitation. SSLyze is a fast and powerful tool that automates the assessment of SSL/TLS implementations by checking for supported cipher suites, protocol versions, certificate validity, heartbleed vulnerability, compression support, and more. This procedure is typically used during reconnaissance phases of web application testing to map out cryptographic weaknesses without exploiting them directly. It requires direct network access to the target host's port (usually 443 for HTTPS) and helps prioritize remediation efforts based on identified risks like deprecated algorithms or untrusted certificates.

## Requirements

1. Network access to the target host on the specified port (e.g., TCP/443).
2. Installed SSLyze tool (see [[tools/SSLyze]] for installation).
3. Basic understanding of SSL/TLS concepts to interpret scan results.
4. No authentication required for external scans, but internal scans may need VPN or proxy access.

## Defense

Defensive measures and detection strategies:

- Implement certificate transparency logging and monitoring for unexpected certificate changes.
- Use web application firewalls (WAFs) to detect and block anomalous scanning traffic patterns.
- Enable logging of TLS handshakes on servers to identify repeated connection attempts from scanners.
- Regularly audit and update SSL/TLS configurations using tools like Qualys SSL Labs for ongoing validation.

## Objectives

1. Identify supported SSL/TLS protocols and cipher suites to detect weak or deprecated options.
2. Validate certificate chain, trust, and extensions for potential trust issues.
3. Check for known vulnerabilities like Heartbleed or compression attacks.
4. Generate a report of findings to guide secure configuration improvements.

## Instructions

### Step 1: Install and Verify SSLyze

**Context**: Ensure the SSLyze tool is installed and functional before scanning. This step confirms the tool's availability and lists available plugins to understand scan capabilities.

Run the installation if needed (refer to [[tools/SSLyze]]), then verify:

**Command** ([[commands/sslyze-show-plugins]]):
```bash
sslyze --help
```

> This displays the tool's help, including available plugins like Heartbleed, Compression, and CipherSuites checks. Expected output includes a list of plugins confirming the tool is ready.

### Step 2: Perform Regular SSL/TLS Scan

**Context**: Execute the core scan using the regular mode, which runs a standard set of checks on the target's SSL/TLS endpoint. This identifies common misconfigurations and vulnerabilities.

**Command** ([[commands/sslyze-regular-scan]]):
```bash
sslyze --regular $_TARGET_HOST:$_TARGET_PORT
```

> Replace $_TARGET_HOST with the domain or IP (e.g., demo.testfire.net) and $_TARGET_PORT with the port (e.g., 443). This command probes the endpoint for availability, then runs plugins to assess compression, certificates, heartbleed, session resumption, and cipher suites across protocols like TLSv1, TLSv1.1, and TLSv1.2. If the target is unavailable, it will error out; otherwise, it outputs detailed results.

### Step 3: Analyze and Document Results

**Context**: Review the scan output for key indicators of misconfigurations, such as failed trust validations, supported weak ciphers, or unsupported secure features like OCSP stapling. Document findings for reporting.

No specific command needed; parse the output manually or pipe to a file for review:

```bash
sslyze --regular $_TARGET_HOST:$_TARGET_PORT > scan_results.txt
```

> Look for 'OK' or 'FAILED' statuses. For example, failed certificate trust across multiple stores indicates chain issues, while accepted weak ciphers (e.g., SSLv3) signal high risk. Cross-reference with OWASP guidelines for severity.
