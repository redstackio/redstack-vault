---
id: 74c88a1d-9ced-41b1-beea-19dcd4fcb63f
name: Directory-Traversal-Fuzzing-with-DotDotPwn
type: procedure
verified: true
submitted: true
created_at: '2020-09-03T18:36:33.294218+00:00'
updated_at: '2023-05-26T01:30:49.285818+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - directory-traversal
  - owasp
  - owasp-top-10
  - web-applications
commands:
  - '[[commands/dotdotpwn-http-fuzzing]]'
platforms:
  - Web
tools:
  - '[[tools/dotdotpwn]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
validated: true
---

# Directory-Traversal-Fuzzing-with-DotDotPwn

## Summary

This procedure uses the DotDotPwn tool to fuzz web applications for directory traversal vulnerabilities, allowing attackers to read or write files outside the intended directory. By generating and testing various traversal patterns (e.g., ../, %2f, null byte injections), it automates the detection of path manipulation flaws in HTTP requests, commonly found in vulnerable file inclusion endpoints.

## Description

Directory traversal (also known as path traversal) vulnerabilities enable unauthorized access to files and directories on the server by manipulating input parameters to navigate the filesystem. DotDotPwn is a specialized fuzzer that creates thousands of traversal payloads, including variations with dots, slashes, URL encoding, and special characters, and sends them against a target host. It supports HTTP GET/POST methods and can target specific paths or fuzz broadly. This technique is particularly useful during web application penetration testing to identify misconfigurations in file handlers, such as those in PHP includes or image upload features. Successful exploitation could lead to sensitive data disclosure (e.g., /etc/passwd) or remote code execution if combined with other flaws. The procedure assumes a Unix-like target OS but can adapt for Windows.

## Requirements

1. Network access to the target web application (e.g., firewall allows HTTP/HTTPS traffic).
2. Installed DotDotPwn tool (see [[tools/dotdotpwn]] for installation).
3. Basic knowledge of web vulnerabilities and HTTP requests.
4. Perl runtime environment, as DotDotPwn is Perl-based.
5. Optional: A wordlist of target files (e.g., /etc/passwd, /etc/shadow) for custom fuzzing.

## Defense

Defensive measures include input validation and sanitization to block traversal sequences (e.g., using whitelisting for paths), running web apps in chroot jails or containers, and employing web application firewalls (WAFs) like ModSecurity with rules for ../ patterns. Detection strategies involve logging anomalous HTTP requests with encoded paths, monitoring for access to sensitive files via IDS/IPS (e.g., Snort rules for T1083), and reviewing server access logs for 200 OK responses to traversal attempts.

## Objectives

1. Identify vulnerable endpoints susceptible to directory traversal attacks.
2. Generate a report of tested paths and any successful traversals.
3. Confirm the presence of flaws that could lead to arbitrary file read/write.

## Instructions

### Step 1: Verify Tool Installation and Target Accessibility

**Context**: Ensure DotDotPwn is installed and the target host is reachable to avoid false negatives from connectivity issues. This step confirms prerequisites before fuzzing.

Use a basic ping or curl command to test connectivity (not a specific DotDotPwn command, but essential setup).

```bash
ping -c 3 $_TARGET_HOST
curl -I http://$_TARGET_HOST
```

> This verifies the host responds to HTTP requests. If the target requires a specific path (e.g., /upload.php), note it for the next step; DotDotPwn will fuzz from the root if not specified.

### Step 2: Configure Fuzzing Parameters

**Context**: Prepare the fuzzing session by setting depth, mode, and target details. DotDotPwn uses flags like -d for traversal depth and -f for custom files. This customizes the attack to the target's likely OS and sensitive files.

Review or create a custom file list if needed (e.g., unix_files.txt with paths like /etc/passwd).

```bash
# Example: Create a simple file list if not using defaults
echo -e "/etc/passwd\n/etc/issue\n/proc/version" > unix_files.txt
```

> Defaults to common Unix files if no -f flag. Set depth to 6-10 for deeper traversals, balancing thoroughness and time.

### Step 3: Execute Directory Traversal Fuzzing

**Context**: Run the core fuzzing command to send traversal payloads and monitor for successful file access, indicated by HTTP 200 responses or file content in replies.

**Command** ([[commands/dotdotpwn-http-fuzzing]]):
```bash
dotdotpwn -m http -h $_TARGET_HOST -M GET -d 6 -f unix_files.txt
```

> This launches HTTP GET requests with traversal patterns against the target host. The tool generates ~11,000 tests (mix of ../, %2f, %c0%af, etc.) at ~3-5 per second. Press Enter to start; Ctrl+C to stop. A report saves to Reports/$_TARGET_HOST_YYYY-MM-DD_HH-MM.txt. Success shows [*] HTTP Status: 200 | Testing Path: ... with file contents; otherwise, 404/400/403.

### Step 4: Analyze Results and Report

**Context**: Review the generated report for successful traversals and validate any hits manually to confirm the vulnerability.

Open the report file:

```bash
cat Reports/$_TARGET_HOST_*.txt
```

> Look for "Total Traversals found: >0" and paths with 200 status. Manually test hits with curl (e.g., curl "http://$_TARGET_HOST/../../etc/passwd") to retrieve content and assess impact. If no hits, increase depth (-d 10) or try POST mode (-M POST) for form-based inputs.

### Step 5: Clean Up and Document Findings

**Context**: Securely store results and remove temporary files to maintain operational security.

```bash
rm -f unix_files.txt
# Archive report if needed
zip findings.zip Reports/$_TARGET_HOST_*.txt
```

> Document vulnerable paths, potential impacts (e.g., data leak), and remediation steps for reporting.
