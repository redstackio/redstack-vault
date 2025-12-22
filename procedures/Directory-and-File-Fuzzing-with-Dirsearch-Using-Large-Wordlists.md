---
type: procedure
description: >-
  Use dirsearch to brute-force directories and files on a list of subdomains
  using large wordlists like SecLists' Top 1000 Robots.txt entries for
  discovering hidden web content.
verified: true
submitted: true
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Active Scanning]]'
  - '[[Vulnerability Scanning]]'
sub_techniques: []
tags:
  - reconnaissance
  - web-fuzzing
  - directory-brute-force
  - dirsearch
commands:
  - '[[commands/dirsearch-scan-multiple-targets-with-custom-wordlist]]'
tools:
  - '[[tools/dirsearch]]'
platforms:
  - Web
skill_level: beginner
impact_level: low
detection_risk: medium
validated: true
---

# Directory-and-File-Fuzzing-with-Dirsearch-Using-Large-Wordlists

## Summary

This procedure uses the dirsearch tool to perform brute-force fuzzing of directories and files across a list of subdomains or websites. It leverages large wordlists, such as the Top 1000 Robots.txt entries from SecLists, to uncover hidden paths that basic scans might miss. This is useful in reconnaissance phases to map the web application attack surface, identify administrative interfaces, backup files, or other sensitive endpoints.

## Description

Directory and file fuzzing involves systematically requesting potential paths on a web server to discover non-linked or hidden resources. Dirsearch is a Python-based tool that supports multithreading, custom wordlists, and various output formats, making it efficient for scanning multiple targets. This procedure focuses on using large wordlists like SecLists' RobotsDisallowed-Top1000.txt, which contains disallowed paths from robots.txt files across top websites, providing a targeted list for discovery. If results are sparse, alternatives like raft-large-directories.txt or raft-large-files.txt can be substituted for broader coverage. The technique aligns with active scanning in reconnaissance, helping identify potential entry points for further exploitation. Prerequisites include a list of target subdomains (e.g., from prior enumeration) and access to wordlists from SecLists repository.

## Requirements

1. A list of target subdomains or URLs in a text file (one per line).
2. Dirsearch tool installed (see [[tools/dirsearch]] for installation).
3. SecLists wordlists downloaded, specifically RobotsDisallowed-Top1000.txt from https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content.
4. Network access to the targets (no authentication required for basic fuzzing).
5. Optional: Larger wordlists like raft-large-directories.txt or raft-large-files.txt for extended scans.

## Defense

Defensive measures include enabling web application firewalls (WAFs) to detect and block brute-force patterns, disabling directory listings on web servers, implementing rate limiting on HTTP requests, and monitoring access logs for anomalous path requests. Tools like ModSecurity or Cloudflare can signature-match fuzzing attempts. Detection involves log analysis for high-volume requests from single IPs targeting non-existent paths.

## Objectives

1. Discover hidden directories and files on target websites to expand the attack surface.
2. Identify potentially sensitive endpoints like admin panels or configuration files.
3. Generate a report of discovered paths with HTTP status codes for prioritization.

## Instructions

### Step 1: Prepare the Target List and Wordlist

**Context**: Gather your list of subdomains (e.g., from tools like subfinder or Amass) into a file named subdomains.txt. Download the wordlist from SecLists; place it in your working directory as RobotsDisallowed-Top1000.txt. This step ensures you have inputs ready for efficient scanning.

If using alternatives, download raft-large-directories.txt or raft-large-files.txt from the SecLists Web-Content directory.

### Step 2: Execute the Dirsearch Scan

**Context**: Run dirsearch against the subdomain list using the custom wordlist. The -L flag loads multiple URLs, -e .* enables all extensions, -w specifies the wordlist, --simple-report outputs results to a file, and -t sets threads for speed (adjust based on target tolerance to avoid detection).

**Command** ([[commands/dirsearch-scan-multiple-targets-with-custom-wordlist]]):
```bash
python3 dirsearch.py -L subdomains.txt -e .* -w RobotsDisallowed-Top1000.txt --simple-report=output.txt -t 50
```

> This command will iterate through each subdomain, fuzzing paths from the wordlist and reporting findings like 200 OK responses for discovered resources. Monitor for rate limits; reduce -t if blocked.

### Step 3: Analyze the Output

**Context**: Review the generated output.txt for successful discoveries (status codes 200, 403, etc.). Cross-reference with HTTP status meanings: 200 indicates accessible content, 403 suggests protected but existent paths worth probing further.

Use grep to filter: `grep -E '200|403' output.txt`. Prioritize paths for manual verification or inclusion in subsequent procedures like vulnerability scanning.
