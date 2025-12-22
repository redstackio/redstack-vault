---
type: procedure
verified: true
submitted: true
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Network Service Scanning]]'
sub_techniques: []
tags:
  - owasp
  - ssl
  - web-applications
  - reconnaissance
  - enumeration
commands:
  - '[[commands/nmap-ssl-cert-enumeration]]'
platforms:
  - Web
tools:
  - '[[tools/Nmap]]'
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Enumerate-SSL-Certificate-Details-with-Nmap

## Summary

This procedure uses Nmap's ssl-cert script to enumerate detailed information about an SSL/TLS certificate on a target web server, including the subject, issuer, public key details, signature algorithm, and validity periods. It is useful during reconnaissance to identify potential weaknesses in certificate configuration, such as expired certificates, weak algorithms, or misconfigurations that could aid in further attacks like man-in-the-middle or trust exploitation.

## Description

SSL/TLS certificates are critical for secure communication in web applications, but their details can reveal valuable information to attackers, such as the certificate authority, key strength, and expiration dates. This procedure leverages Nmap, a powerful network scanning tool, to connect to the target's HTTPS port and extract certificate metadata without exploiting vulnerabilities. It is typically used in the early stages of penetration testing to map the attack surface and inform decisions on whether to pursue certificate-related attacks, like forging or downgrading encryption. The technique aligns with passive reconnaissance to avoid alerting defenses while gathering host and service information.

## Requirements

1. Network access to the target host on the specified port (e.g., TCP/443 for HTTPS).
2. Nmap installed with NSE (Nmap Scripting Engine) support, including the ssl-cert script.
3. Basic knowledge of command-line tools and networking concepts.
4. No special credentials required, as this is an external enumeration technique.

## Defense

Defensive measures and detection strategies:

- Implement certificate pinning or HSTS to limit reconnaissance value.
- Monitor network traffic for Nmap scans using tools like Snort or Suricata with signatures for NSE scripts.
- Use firewalls to rate-limit or block unusual port probes on HTTPS endpoints.
- Regularly audit and rotate certificates to minimize exposure of sensitive details.

## Objectives

1. Extract comprehensive SSL/TLS certificate metadata from the target server.
2. Identify potential misconfigurations, such as weak ciphers or expired validity.
3. Gather information to support subsequent attack planning, like targeting weak encryption.
4. Verify the certificate chain without disrupting service.

## Instructions

### Step 1: Identify Target and Port

**Context**: Before running the scan, determine the target hostname or IP and the port running the SSL/TLS service (commonly 443 for HTTPS). This ensures the scan is focused and avoids unnecessary noise. Use prior reconnaissance if available to confirm the service is active.

Resolve the target's IP if using a hostname, or use tools like [[commands/nmap-host-discovery]] for initial ping sweeps.

### Step 2: Execute SSL Certificate Enumeration

**Context**: Run the Nmap ssl-cert script to connect to the target port and retrieve the certificate details. This script performs a non-intrusive handshake to dump the certificate without sending malicious payloads, making it stealthy for reconnaissance.

**Command** ([[commands/nmap-ssl-cert-enumeration]]):
```bash
nmap --script ssl-cert $_TARGET -p$_PORT
```

> This command initiates an NSE script scan specifically for ssl-cert, outputting structured details like subject alternative names (SANs), issuer information, and hash fingerprints. Replace $_TARGET with the hostname/IP and $_PORT with the service port (e.g., 443). The scan should complete in seconds for a single host.

### Step 3: Analyze Output for Insights

**Context**: Review the scan results to identify actionable intelligence, such as expired certificates (check 'Not valid after' date) or weak algorithms (e.g., MD5 or SHA1 signatures). Cross-reference with known vulnerabilities in the issuer or key type to decide on next steps, like attempting SSL stripping if weak ciphers are detected.

Parse the output manually or pipe to tools like grep for specific fields:
```bash
grep -A 10 'ssl-cert' nmap_output.txt
```

> Look for indicators like short key lengths (<2048 bits) or self-signed issuers, which could indicate development environments or misconfigurations exploitable in attacks.
