---
id: 9bbc637e-7c86-4276-9ef9-82511b366a9d
name: using-nikto-to-scan-for-common-web-vulnerabilities
type: procedure
verified: true
submitted: true
created_at: '2020-08-19T16:08:59.051053+00:00'
updated_at: '2023-05-26T18:10:40.891006+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - '[[tags/owasp]]'
  - '[[tags/vulnerability-scanning]]'
  - '[[tags/web-applications]]'
commands:
  - '[[commands/nikto-scan-web-application]]'
platforms:
  - Web
tools:
  - '[[tools/Nikto]]'
validated: true
---

# using-nikto-to-scan-for-common-web-vulnerabilities

## Summary

This procedure uses the Nikto web vulnerability scanner to identify common misconfigurations, outdated software, and potential vulnerabilities in web applications and servers. It performs an automated scan against a target URL, checking for issues like missing security headers, exposed directories, and known server vulnerabilities, making it a quick initial reconnaissance step in web penetration testing.

## Description

Nikto is an open-source web server scanner that tests for over 6,700 potentially dangerous files, outdated server versions, and insecure configurations. In a typical attack scenario, this procedure is used during the reconnaissance phase to map out weaknesses in public-facing web applications. It sends multiple HTTP requests to probe the target, analyzing responses for indicators of vulnerabilities such as HTTP TRACE enabled (suggesting XST risks), missing security headers like X-Frame-Options, and directory traversal issues. The scan is non-intrusive but can generate significant traffic, so it's best run from a controlled environment. Expected outcomes include a report listing vulnerabilities with OSVDB/CVE references, which can guide further manual testing or exploitation.

## Requirements

1. Network access to the target web application (direct connectivity or via proxy).
2. Nikto tool installed on a Linux-based system (e.g., Kali Linux).
3. Basic knowledge of HTTP protocols and web security concepts.
4. Optional: A proxy like Burp Suite for traffic interception and modification during scans.

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAFs) like ModSecurity to block anomalous scanning patterns.
- Enable logging for HTTP requests and monitor for high-volume probes from single IPs (e.g., using tools like Fail2Ban or SIEM systems).
- Use rate limiting and CAPTCHA on web endpoints to deter automated scans.
- Regularly update server software and security headers to mitigate identified issues.

## Objectives

1. Identify common web server misconfigurations and outdated components.
2. Detect potential entry points for further exploitation, such as exposed admin panels or vulnerable CGI scripts.
3. Generate a vulnerability report to prioritize remediation or targeted attacks.

## Instructions

### Step 1: Prepare the Target and Launch Scan

**Context**: Begin by verifying network connectivity to the target URL and then execute the Nikto scan to probe for common vulnerabilities. This step automates the detection of server banners, HTTP methods, and file/directory exposures.

**Command** ([[commands/nikto-scan-web-application]]):
```bash
nikto -h $_TARGET_URL
```

> This command initiates a comprehensive scan of the specified URL, outputting details on server information, security headers, and potential vulnerabilities. Replace $_TARGET_URL with the full path to the web application endpoint (e.g., http://example.com/login.php). The scan may take several minutes depending on the target's response time and complexity.

### Step 2: Review and Validate Scan Results

**Context**: Analyze the output for high-priority issues like enabled TRACE methods or exposed sensitive files. Cross-reference findings with vulnerability databases and perform manual verification if needed.

**Command** ([[commands/nikto-scan-web-application]]):
```bash
nikto -h $_TARGET_URL -o $_OUTPUT_FILE -Format txt
```

> Save results to a file for easier review and sharing. Use the -Format option to export in HTML, XML, or TXT for integration with reporting tools. Manually test flagged vulnerabilities (e.g., attempt XST if TRACE is enabled) to confirm exploitability.

### Step 3: Follow-Up on Specific Findings

**Context**: If the scan identifies directory listings or outdated software, use additional tools to explore deeper. This ensures the procedure leads to actionable intelligence.

No specific command here; refer to related procedures like [[procedures/manual-directory-brute-force]] for enumeration if directories are found.
