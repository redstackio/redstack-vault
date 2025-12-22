---
type: procedure
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Gather Victim Host Information]]'
sub_techniques: []
tags:
  - cryptography
  - data-exposure
  - web-applications
commands:
  - '[[commands/sslyze-enumerate-ssl-tls-certificate]]'
  - '[[commands/keytool-print-ssl-server-certificate]]'
platforms:
  - Web
tools:
  - '[[tools/SSLyze]]'
  - '[[tools/java-keytool]]'
skill_level: beginner
impact_level: low
detection_risk: low
verified: true
validated: true
---

# Enumerate and Analyze an SSL/TLS Certificate

## Summary

This procedure demonstrates how to enumerate and analyze SSL/TLS certificates from a target web server to extract organizational details, alternative domain names, validity periods, and potential vulnerabilities. Such information can reveal virtual host configurations, expiry dates, and weak cipher support, aiding in reconnaissance for further attack planning.

## Description

SSL/TLS certificates are publicly accessible and contain metadata about the issuing organization, subject names, alternative DNS entries (SANs), serial numbers, validity periods, and supported cipher suites. Attackers enumerate these to map the attack surface, identify subdomains or virtual hosts, detect expired or misconfigured certificates, and assess vulnerability to attacks like Heartbleed. This technique is passive if using public tools but can be active when probing servers directly. It applies to any HTTPS-enabled web application and requires only network connectivity to the target port (typically 443).

## Requirements

1. Network access to the target web server on port 443 (or custom HTTPS port).
2. Installed tools: SSLyze (Python-based) and Java Keytool (part of JDK).
3. Basic command-line proficiency; no elevated privileges needed on the attacker's machine.
4. Target must have a valid or invalid SSL/TLS certificate; self-signed certificates may reveal internal details.

## Defense

- Monitor for unusual certificate scanning traffic using network intrusion detection systems (NIDS) like Snort rules targeting SSLyze or keytool probes.
- Implement Certificate Transparency (CT) logging to track certificate issuance publicly.
- Use HTTP Strict Transport Security (HSTS) to enforce HTTPS and limit probing impacts.
- Regularly audit certificates for exposed sensitive information in SAN fields and rotate them to minimize exposure.

## Objectives

1. Extract certificate chain, subject details, and alternative names to map organizational domains.
2. Identify validity periods and potential expiry issues that could indicate neglect.
3. Detect supported ciphers and vulnerabilities like Heartbleed to inform exploitation paths.
4. Gather fingerprints and serial numbers for correlation with other OSINT sources.

## Instructions

### Step 1: Enumerate Certificate Details Using SSLyze

**Context**: Use SSLyze to perform a comprehensive scan of the target's SSL/TLS configuration, including the certificate chain, subject alternative names (SANs), expiry dates, and vulnerability checks like Heartbleed. This step provides a broad overview and highlights weak configurations without downloading the full certificate.

**Command** ([[commands/sslyze-enumerate-ssl-tls-certificate]]):
```bash
sslyze --regular $_TARGET_HOST
```

> Run this command against the target's hostname or IP to fetch and display certificate information. The --regular option enables standard enumeration including ciphers and vulnerabilities. Replace $_TARGET_HOST with the domain (e.g., example.com) or IP:port (e.g., 192.168.1.100:443). This step is useful first as it quickly identifies key fields like SANs and expiry without requiring Java.

### Step 2: Extract and Print Certificate Using Keytool

**Context**: If more detailed owner and issuer information is needed, use Java's Keytool to connect to the SSL server and print the certificate details, including fingerprints and public key info. This complements SSLyze by providing raw X.509 data for manual analysis or scripting.

**Command** ([[commands/keytool-print-ssl-server-certificate]]):
```bash
keytool -printcert -sslserver $_TARGET_IP:$_TARGET_PORT
```

> Execute this to retrieve and display the certificate chain starting from the server's presented cert. Specify the target's IP and port (default 443 for HTTPS). This command verifies the connection and outputs structured data like owner DN, issuer, and hashes. Use it when SSLyze output needs validation or for environments where Python tools are restricted.

### Step 3: Analyze Extracted Information

**Context**: Review the outputs from previous steps to identify actionable intelligence. Look for SANs suggesting additional hosts, short validity periods indicating poor maintenance, or weak ciphers enabling downgrade attacks.

**Instructions**: Manually inspect the output for fields like X509v3 Subject Alternative Name (virtual hosts), Not After (expiry), Certificate Chain (trust path), and Cipher Suites (supported protocols). Cross-reference SANs with DNS enumeration tools. If vulnerabilities like Heartbleed are flagged, note them for follow-up exploitation.

> No specific command here; use text processing tools like grep if automating (e.g., grep -i "subject alternative" output.txt).
