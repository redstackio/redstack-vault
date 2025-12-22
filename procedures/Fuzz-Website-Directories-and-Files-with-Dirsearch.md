---
id: fc08321a-93f2-453f-9c55-94b88fae1cb4
name: Fuzz-Website-Directories-and-Files-with-Dirsearch
type: procedure
verified: true
submitted: true
created_at: '2020-07-24T17:11:43.608472+00:00'
updated_at: '2023-05-26T18:35:38.799780+00:00'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[File and Directory Discovery]]'
sub_techniques: []
tags:
  - reconnaissance
  - web-scanning
  - directory-bruteforce
  - file-discovery
commands:
  - '[[commands/dirsearch-enumerate-directories-and-files]]'
platforms:
  - web
tools:
  - '[[tools/Dirsearch]]'
skill_level: beginner
impact_level: low
detection_risk: medium
validated: true
---

# Fuzz-Website-Directories-and-Files-with-Dirsearch

## Summary

This procedure utilizes the dirsearch tool to perform automated brute-force scanning for hidden directories, files, and endpoints on a target website. It helps in mapping the web application's structure, identifying configuration files, administrative panels, and potential API paths such as gRPC or GraphQL endpoints, which can reveal the attack surface during reconnaissance.

## Description

Directory and file fuzzing, also known as brute-forcing, involves systematically requesting common paths and filenames against a web server to discover unprotected resources. Dirsearch is a fast, multi-threaded Python tool that uses built-in wordlists to test for existence via HTTP status codes (e.g., 200 for found, 403 for forbidden). This technique is particularly useful in the initial reconnaissance phase of web application testing to uncover hidden content that might not be linked from the main site. It maps to MITRE ATT&CK's Discovery tactic, specifically File and Directory Discovery (T1083), as it enumerates server resources without exploitation. Prerequisites include network access to the target and basic knowledge of HTTP responses. Expected outcomes include a list of discoverable paths that can guide further enumeration or exploitation.

## Requirements

1. Network connectivity to the target website (no firewall blocking outbound HTTP requests).
2. Python 3 environment with dirsearch installed (see [[tools/Dirsearch]] for installation).
3. Optional: Custom wordlists for targeted fuzzing (dirsearch includes defaults).
4. Basic understanding of HTTP status codes to interpret results.

## Defense

Defensive measures and detection strategies:

- Implement Web Application Firewalls (WAFs) like ModSecurity to detect and block patterns of rapid, sequential HTTP requests to non-existent paths.
- Enable server-side rate limiting and IP reputation checks to throttle brute-force attempts.
- Monitor access logs for high volumes of 404/403 responses from a single source, using tools like Fail2Ban or SIEM systems for alerting.
- Use directory indexing restrictions (e.g., Options -Indexes in Apache) and robots.txt to obscure structure, though these are not foolproof.

## Objectives

1. Identify hidden directories and files that expand the known attack surface.
2. Locate sensitive files like configuration backups (.bak, .old) or API documentation.
3. Uncover potential entry points for further web exploitation, such as admin panels or debug endpoints.
4. Generate a report of discovered resources for integration into broader reconnaissance efforts.

## Instructions

### Step 1: Verify Tool Installation and Prepare Target

**Context**: Ensure dirsearch is installed and accessible, then define the target URL and extensions to focus the scan. This step prevents runtime errors and tailors the fuzzing to relevant file types, reducing noise from irrelevant requests.

Install or verify dirsearch using the instructions in [[tools/Dirsearch]]. Identify the base URL (e.g., http://example.com) and common extensions like php, html, js, or use .* for all supported types. This preparation ensures the scan is efficient and targeted.

**Expected Output**: Confirmation that dirsearch runs with `python3 dirsearch.py --help` without errors, displaying available options.

### Step 2: Execute Directory and File Enumeration

**Context**: Run the core fuzzing command to probe the target. This step sends HTTP requests for each path in dirsearch's wordlist, checking responses for indications of existence (e.g., 200 OK, 301 Redirect) versus absence (404 Not Found). The -u flag specifies the base URL, and -e defines extensions to append, allowing discovery of both directories and specific files.

**Command** ([[commands/dirsearch-enumerate-directories-and-files]]):
```bash
python3 dirsearch.py -u $_TARGET_URL -e $_EXTENSIONS
```

> This command initiates the scan, outputting results in real-time. Monitor for status codes: 200 indicates a found resource, 403 suggests access denied but existent, and 301/302 may reveal redirects to valid paths. If using a custom wordlist, add -w /path/to/wordlist.txt for more comprehensive coverage. Run this from a Kali Linux or similar environment for best performance.

**Expected Output**: Real-time console output listing discovered paths, such as:

[+] http://redstack.io/admin (CODE:200|SIZE:1543)
[+] http://redstack.io/config.php (CODE:403|SIZE:0)
[+] http://redstack.io/api/graphql (CODE:200|SIZE:2890)

A summary at the end shows scan statistics, including requests made and response code breakdowns.

### Step 3: Review and Save Results for Analysis

**Context**: Capture the output for offline review and integration with other tools. This step verifies findings and prepares data for manual validation or chaining with procedures like vulnerability scanning. Use the --output flag (add to the command if needed) to save results to a file, enabling searching for keywords like 'admin' or 'config'.

Modify the command if needed: `python3 dirsearch.py -u $_TARGET_URL -e $_EXTENSIONS --output=scan_results.txt`. Manually inspect the output file or console for interesting paths, then test them with a browser or [[commands/curl-basic-http-request]] to confirm accessibility.

**Expected Output**: A saved text file (if using --output) mirroring the console output, or clipboard-copied results. Success is indicated by at least one 200/301 response beyond the root path, suggesting hidden content.

> If no interesting findings, iterate by adding extensions (-e bak,old,txt) or using a larger wordlist (-w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt).
