---
id: b542efdf-5eaf-40ef-821e-13d51baa3175
name: Scan-Web-Application-for-LFI-RFI-and-RCE-Using-Uniscan
type: procedure
verified: true
submitted: true
created_at: '2020-08-31T18:28:13.610101+00:00'
updated_at: '2023-05-26T01:28:09.813962+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - LFI
  - RFI
  - RCE
  - Web Applications
  - OWASP
  - OWASP Top 10
commands:
  - '[[commands/uniscan-scan-for-vulnerabilities]]'
tools:
  - '[[tools/uniscan]]'
platforms:
  - Web
validated: true
---

# Scan-Web-Application-for-LFI-RFI-and-RCE-Using-Uniscan

## Summary

This procedure uses the Uniscan tool to actively scan a web application for vulnerabilities such as Local File Inclusion (LFI), Remote File Inclusion (RFI), and Remote Code Execution (RCE). It crawls the target URL, checks for common misconfigurations, and identifies potential injection points, providing output on discovered issues like exposed phpinfo pages or external hosts that could indicate RFI paths.

## Description

Uniscan is a Perl-based web vulnerability scanner focused on file inclusion and command injection flaws, common in web applications vulnerable to OWASP Top 10 issues like A03: Injection and A05: Security Misconfiguration. The procedure targets a specified URL, performs crawling to discover linked resources, and tests for LFI/RFI by attempting to include local/remote files and execute commands. It is useful in reconnaissance phases to map attack surfaces on public-facing web apps. Success reveals sensitive information exposure or execution capabilities, enabling further exploitation. This maps to MITRE ATT&CK's Active Scanning technique under Reconnaissance, as it probes for weaknesses without assuming prior access.

## Requirements

1. Kali Linux or Ubuntu with Perl installed (Uniscan is Perl-based).
2. Network access to the target web application (no authentication required for basic scans).
3. Installed Uniscan tool (see [[tools/uniscan]] for installation).
4. Target URL (e.g., a login page or entry point likely to have parameters for inclusion attacks).

## Defense

Defensive measures include web application firewalls (WAFs) to block anomalous requests, input validation/sanitization to prevent file inclusion, and disabling allow_url_include in PHP configurations. Detection strategies involve logging unusual HTTP requests with payloads like '../../../../etc/passwd' for LFI, monitoring for Perl script executions from Uniscan, and using tools like Fail2Ban or IDS signatures for scan patterns.

## Objectives

1. Identify LFI vulnerabilities by testing for local file access (e.g., /etc/passwd).
2. Detect RFI by checking for remote file inclusion from external hosts.
3. Uncover RCE opportunities through command injection tests.
4. Gather auxiliary information like emails, phpinfo disclosures, and external dependencies.

## Instructions

### Step 1: Verify Uniscan Installation and Target Accessibility

**Context**: Ensure the Uniscan tool is available and the target URL is reachable to avoid false negatives from tool or network issues. This step confirms prerequisites before scanning.

Use [[commands/uniscan-scan-for-vulnerabilities]] with a basic test flag if available, or ping/curl the target manually.

```bash
curl -I http://$_TARGET_URL
```

> This command checks HTTP headers and status. Expected: 200 OK or redirect, confirming the server responds.

### Step 2: Launch the Full Vulnerability Scan

**Context**: Execute the core Uniscan command to crawl the application, test for LFI/RFI/RCE, and collect findings. The -qweds flags enable comprehensive checks: -q for quiet mode (minimal output), -w for web bugs, -e for encoding tests, -d for directory enumeration, -s for additional scans.

**Command** ([[commands/uniscan-scan-for-vulnerabilities]]):
```bash
uniscan -u $_TARGET_URL -qweds
```

> Replace $_TARGET_URL with the application entry point (e.g., http://192.168.1.11/vcart/login.php). This initiates crawling (up to 81 URLs in examples), loads plugins for external host detection, code disclosure, email harvesting, and phpinfo checks. It skips directory/file checks if 404 responses are inconsistent but proceeds with vulnerability probes.

### Step 3: Analyze Scan Output for Vulnerabilities

**Context**: Review the output for indicators of LFI/RFI/RCE, such as successful file inclusions, command echoes, or exposed sensitive data. Prioritize phpinfo disclosures or external hosts as RFI vectors.

Manually parse the console output or redirect to a file for review:

```bash
uniscan -u $_TARGET_URL -qweds > scan_results.txt
cat scan_results.txt | grep -E "Found|Disclosure|Vulnerability"
```

> Look for lines like '[+] phpinfo() page: http://...' indicating misconfigurations (allow_url_include: On), emails suggesting contact points, or external hosts for RFI payloads. If RCE is suspected, follow up with manual tests using tools like Burp Suite.

### Step 4: Validate and Escalate Findings

**Context**: Confirm any potential vulnerabilities with manual tests to rule out false positives, then document for exploitation in subsequent procedures.

For a detected phpinfo page, access it directly:

```bash
curl http://$_TARGET_URL/dashboard/phpinfo.php
```

> Expected: Detailed PHP config dump. If allow_url_include is On and disable_functions is empty, the app is highly vulnerable to RFI/RCE. Escalate by attempting a simple RFI payload like including a remote PHP shell.
