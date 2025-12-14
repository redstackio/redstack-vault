---
id: proc-moodle-scan-nuclei-2024
tags:
  - xss
  - scanning
  - nuclei
  - moodle
type: procedure
tools:
  - '[[tools/Nuclei]]'
tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
commands:
  - '[[commands/nuclei-moodle-xss-scan]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-13T23:55:20.429Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Scan-for-Moodle-LTI-Reflected-XSS-Using-Nuclei

## Summary

This procedure uses the Nuclei vulnerability scanner to detect reflected XSS in Moodle's LTI module (CVE-2022-35653) by sending a crafted POST request to /mod/lti/auth.php and checking for payload reflection.

## Description

In a typical attack scenario, an attacker scans public-facing web applications for known vulnerabilities. Here, Nuclei automates the detection by emulating a POST request with a malicious payload like xxx"><img/src%3d'x'onerror%3dalert('document_domain')>=1. If vulnerable, the response reflects the payload, includes 'moodle-editor', has Content-Type text/html, and returns status 200. This confirms the insufficient sanitization in the LTI module, allowing further exploitation. Prerequisites include network access to the target and Nuclei installed with the CVE template.

## Requirements

1. Network access to the Moodle instance (HTTPS/HTTP)
2. Nuclei scanner installed with CVE-2022-35653 template
3. Basic understanding of HTTP requests and XSS payloads

## Defense

Defensive measures and detection strategies:

- Enable Content Security Policy (CSP) to block inline scripts
- Sanitize all user inputs in LTI module parameters
- Monitor for anomalous POST requests to /mod/lti/auth.php with script tags
- Use WAF rules to detect common XSS payloads like <img src=x onerror=alert

## Objectives

1. Identify if the target Moodle LTI endpoint is vulnerable to reflected XSS
2. Gather evidence of reflection for proof-of-concept
3. Prepare for payload delivery in subsequent exploitation

## Instructions

### Step 1: Prepare Nuclei Template

**Context**: Ensure the CVE-2022-35653 template is available in Nuclei's templates directory.

Download or verify the template configuration: id CVE-2022-35653, severity medium, max-request 1, matchers for reflected payload, moodle-editor, text/html, and 200 status.

### Step 2: Execute Scan

**Context**: Run Nuclei against the target URL to send the POST request and match responses.

**Command** ([[commands/nuclei-moodle-xss-scan]]):
```bash
nuclei -u https://target.com -t cves/2022/CVE-2022-35653.yaml -v
```

> This command scans the target, sends the POST with the payload to /mod/lti/auth.php, and outputs vulnerability details if matched. Expected output includes vulnerability confirmation and reflected indicators.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/nuclei-moodle-xss-scan]]

## Tools Used

- [[tools/Nuclei]]

## Tags

- xss
- scanning
- nuclei
- moodle
