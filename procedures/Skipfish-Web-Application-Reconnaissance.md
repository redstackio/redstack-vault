---
id: 7ccedcdd-5665-433c-9ed8-6c93b66aaf55
name: Skipfish-Web-Application-Reconnaissance
type: procedure
verified: true
submitted: true
created_at: '2020-09-01T18:19:32.774528+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
sub_techniques: []
tags:
  - '[[tags/owasp]]'
  - '[[tags/owasp top 10]]'
  - '[[tags/Web Applications]]'
  - reconnaissance
  - web-scanning
commands:
  - '[[commands/skipfish-perform-reconnaissance]]'
platforms:
  - Web
tools:
  - '[[tools/skipfish]]'
skill_level: beginner
impact_level: low
detection_risk: medium
validated: true
---

# Skipfish-Web-Application-Reconnaissance

## Summary

This procedure uses Skipfish, a web application security reconnaissance tool, to perform active scanning of a target web application. It crawls the site, identifies directories, parameters, and potential entry points, generating a report that highlights issues such as hidden files, unusual responses, and structural anomalies. Ideal for initial mapping of web attack surfaces during penetration testing or red team engagements.

## Description

Skipfish is an active web application security reconnaissance tool developed by Google, designed to efficiently spider and probe web applications for vulnerabilities and information disclosure. In this procedure, Skipfish is configured to scan a target URL, such as an e-commerce site like vCart, outputting results to an HTML report for easy analysis. The tool follows links, tests for common web flaws, and categorizes findings by severity. This technique maps the application's structure, revealing endpoints that could be exploited later in an attack chain, such as for injection or authentication bypass. It operates in a dictionary-based crawling mode, making it fast and thorough for medium-sized applications. Prerequisites include network access to the target and Skipfish installed on a Linux-based system like Kali.

## Requirements

1. Network access to the target web application (e.g., HTTP/HTTPS connectivity).
2. Skipfish tool installed (see [[tools/skipfish]] for installation).
3. Basic knowledge of web technologies and command-line usage.
4. Sufficient disk space for output reports (typically 100MB+ for large sites).

## Defense

Defensive measures and detection strategies:

- Implement Web Application Firewalls (WAFs) like ModSecurity to detect and block anomalous scanning patterns from Skipfish's user-agent or request signatures.
- Rate-limit incoming requests to prevent automated crawling; monitor for high-volume probes from single IPs.
- Use server-side logging (e.g., Apache/Nginx access logs) to identify recursive crawling and unusual path enumerations.
- Deploy honeypots or canary tokens on hidden directories to alert on reconnaissance attempts.

## Objectives

1. Map the web application's directory structure and discover hidden endpoints.
2. Identify potential input points for further vulnerability testing.
3. Generate a categorized report of reconnaissance findings for analysis.
4. Establish baseline knowledge of the application's attack surface.

## Instructions

### Step 1: Prepare the Target and Output Directory

**Context**: Before running the scan, ensure the target URL is accessible and create an output directory to store the generated report. This prevents clutter and allows for organized result review. Skipfish will create an index.html file in the specified output folder summarizing the scan.

**Command** ([[commands/skipfish-perform-reconnaissance]]):
```bash
skipfish -o ./output-directory http://target-ip-or-domain/path
```

> This command initiates the reconnaissance scan. Replace `./output-directory` with your desired path (e.g., `./test`) and `http://target-ip-or-domain/path` with the actual target (e.g., `http://192.168.1.3/vcart`). The scan will crawl the site, probe for issues, and save results. Expect the process to take several minutes depending on site size; monitor progress via console output showing discovered pages and errors.

### Step 2: Review the Generated Report

**Context**: Once the scan completes, navigate to the output directory to examine the index.html file. This file provides a sitemap, issue list, and severity ratings, helping identify low-hanging fruit like exposed admin panels or error messages.

No specific command is needed here; use a web browser to open `output-directory/index.html`.

> The report categorizes findings into sections like "Attack Surface" (total pages discovered), "Issues" (potential vulnerabilities flagged by response codes or content), and "Signatures" (matched patterns). Look for high-severity items first, such as 200 responses on non-standard paths indicating information disclosure.

### Step 3: Analyze Specific Issues

**Context**: Dive deeper into the report's issue list to prioritize findings. Each issue links to details, including request/response samples, allowing validation of potential exploits.

No command; manually inspect the HTML report sections.

> Success is indicated by a populated issues list with actionable insights, such as unusual HTTP responses (e.g., 403 on admin paths) or parameter discoveries. Cross-reference with tools like Burp Suite for manual verification if needed.
