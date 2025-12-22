---
id: e6cf3310-ce05-4839-ab91-b1d24932eb55
name: Scan-SSL-TLS-Configuration-with-TLSSLed
type: procedure
verified: true
submitted: true
created_at: '2020-09-03T15:26:43.807515+00:00'
updated_at: '2023-05-26T18:51:59.389838+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Network Service Scanning]]'
sub_techniques: []
tags:
  - owasp
  - owasp-top-10
  - ssl
  - tls
  - web-applications
  - reconnaissance
commands:
  - '[[commands/tlssled-scan-target-host]]'
platforms:
  - Web
tools:
  - '[[tools/TLSSLed]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Scan-SSL-TLS-Configuration-with-TLSSLed

## Summary

This procedure uses the TLSSLed tool to perform a comprehensive scan of a web application's SSL/TLS configuration, identifying supported protocol versions, cipher suites, certificate details, security headers like HSTS, and cookie secure flags. It is useful during reconnaissance to detect misconfigurations that could lead to vulnerabilities such as weak ciphers or outdated protocols.

## Description

SSL/TLS secures communication between clients and web servers, but improper implementations can expose applications to attacks like downgrade attacks, man-in-the-middle, or information disclosure. TLSSLed, built on sslscan and OpenSSL, automates the testing of these aspects by probing the target host on a specified port (typically 443 for HTTPS). The scan reveals supported TLS versions (e.g., TLS 1.0-1.3), cipher strengths, certificate validity, renegotiation support, and HTTP security headers. This procedure is applicable in web penetration testing to assess the security posture of public-facing web applications and identify potential weaknesses for further exploitation or reporting.

## Requirements

1. Network access to the target host and port (e.g., TCP/443 for HTTPS).
2. TLSSLed tool installed on a Linux-based system like Kali Linux.
3. Basic command-line knowledge; no special credentials required as this is passive reconnaissance.
4. OpenSSL library (usually pre-installed with TLSSLed).

## Defense

Defensive measures include enforcing modern TLS versions (1.2+), strong cipher suites (AES-based), HSTS headers, and secure cookie flags. Detection can involve monitoring for unusual SSL/TLS probes via tools like Fail2Ban or IDS signatures for sslscan-like traffic patterns.

- Regularly audit SSL/TLS configurations with automated tools.
- Implement certificate pinning and strict transport security.

## Objectives

1. Identify supported SSL/TLS protocols and ciphers to detect weak configurations.
2. Extract certificate details for validity and issuer analysis.
3. Verify security headers and cookie attributes for compliance.
4. Generate a report of potential vulnerabilities for remediation.

## Instructions

### Step 1: Install and Verify TLSSLed

**Context**: Ensure the TLSSLed tool is available and functional before scanning. This step confirms the tool's presence and OpenSSL integration.

Install TLSSLed if not present using the package manager or from source.

**Command** ([[commands/tlssled-scan-target-host]]):
```bash
# Installation example on Kali/Ubuntu
tlssled --version
```

> Run `tlssled --help` to verify installation. Expected output includes tool version and usage options. If not installed, download from the official repository.

### Step 2: Execute the TLSSLed Scan

**Context**: Launch the scan against the target host and port to gather SSL/TLS details. This probes the service for protocol support, ciphers, and headers without disrupting the target.

**Command** ([[commands/tlssled-scan-target-host]]):
```bash
tlssled $_TARGET_IP $_PORT
```

> Replace $_TARGET_IP with the target's IP (e.g., 65.61.137.117) and $_PORT with the service port (e.g., 443). The tool creates an output directory with logs and results. This step typically takes 1-2 minutes depending on the target's responsiveness.

### Step 3: Analyze the Output

**Context**: Review the generated files and console output to identify key findings, such as weak ciphers or missing HSTS.

Navigate to the output directory (e.g., TLSSLed_1.3_$_TARGET_IP_$_PORT_TIMESTAMP) and examine files like sslscan_*.log for cipher details and openssl_HEAD_*.log for headers.

> Look for indicators like "Accepted TLSv1.0" (outdated) or absence of HSTS. Success is confirmed by the presence of detailed cipher lists and certificate info without errors.
