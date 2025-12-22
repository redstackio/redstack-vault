---
type: procedure
verified: true
submitted: true
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Search Victim-Owned Websites]]'
sub_techniques: []
tags:
  - reconnaissance
  - web-archives
  - wayback-machine
  - osint
commands:
  - '[[commands/waybackmachine-search-archived-links]]'
tools:
  - '[[tools/waybackmachine]]'
platforms:
  - Linux
skill_level: beginner
impact_level: low
detection_risk: low
validated: true
---

# Search-Archived-Domain-Content-with-Wayback-Machine

## Summary

This procedure uses the Wayback Machine crawler script to query the Internet Archive's Wayback Machine for archived snapshots of a target domain. It retrieves historical URLs, parameters, and pages that may reveal outdated vulnerabilities, exposed endpoints, or forgotten subdomains useful for further reconnaissance or exploitation in penetration testing.

## Description

The Wayback Machine, operated by the Internet Archive, stores snapshots of websites over time. This procedure leverages a Python script to automate querying these archives for a given domain, outputting a list of captured URLs. These can include old versions of web applications with insecure configurations, backup files, or directory listings that are no longer live but provide valuable intelligence. It is particularly useful in the reconnaissance phase to expand the attack surface beyond the current website state. The script interacts with the Wayback Machine's API to fetch CDX index data and reconstruct URLs. Prerequisites include Python 3 and the script's dependencies like requests library. This maps to MITRE ATT&CK technique T1594 for searching open websites and domains to gather victim information.

## Requirements

1. Python 3.6+ installed on a Linux system (e.g., Kali Linux).
2. Access to the [[tools/waybackmachine]] script, cloned from its GitHub repository.
3. Internet connectivity to query archive.org.
4. No special credentials or target access required; this is passive reconnaissance.

## Defense

Defensive measures and detection strategies:

- Monitor for unusual outbound traffic to archive.org from security tools or analysts, though this is typically benign.
- Implement web application firewalls (WAFs) to detect scraping or automated queries, but Wayback Machine access is public.
- Use historical analysis tools on your side to identify what has been archived and request removal via robots.txt or direct contact with the Internet Archive.
- Rate limiting on your domain can prevent excessive crawling, but archives are historical.

## Objectives

1. Retrieve a comprehensive list of archived URLs for the target domain to identify potential entry points.
2. Analyze output for sensitive parameters, subpaths, or technologies no longer in use.
3. Expand reconnaissance data for mapping the target's digital footprint over time.
4. Expected outcome: A text file or console output listing hundreds to thousands of historical URLs for manual review.

## Instructions

### Step 1: Install and Prepare the Tool

**Context**: Ensure the Wayback Machine script is installed and ready. This involves cloning the repository and installing any Python dependencies to avoid runtime errors.

Navigate to your working directory and clone the repository using git. Then, install required libraries if not already present.

**Command** ([[commands/git-clone-waybackmachine]]):
```bash
git clone https://github.com/ghostlulzhacks/waybackMachine.git
```

> This downloads the script. Expected output: Repository cloned successfully into a local directory.

**Command** ([[commands/pip-install-requests]]):
```bash
pip3 install requests
```

> Installs the requests library used by the script. Expected output: Successfully installed requests.

### Step 2: Execute the Wayback Machine Query

**Context**: Run the script against the target domain to fetch archived links. This step performs the core reconnaissance by querying the archive.

Change into the script's directory and execute the Python script with the target domain as the argument. The script will output URLs to the console or a file if redirected.

**Command** ([[commands/waybackmachine-search-archived-links]]):
```bash
python3 waybackMachine.py example.com
```

> Replace example.com with the target domain. This queries the Wayback Machine CDX API for snapshots. Expected output: A list of URLs in the format timestamp, original URL, MIME type, and status code, e.g., '20060101120000/http://example.com/oldpage.html text/html 200'.

### Step 3: Parse and Review Output

**Context**: Process the results to identify actionable intelligence, such as unique paths or parameters that could be tested for vulnerabilities.

Redirect the output to a file for easier analysis, then use grep or similar to filter interesting entries (e.g., those containing 'admin' or '.bak').

**Command** ([[commands/waybackmachine-search-archived-links-with-output]]):
```bash
python3 waybackMachine.py example.com > archived_urls.txt
```

> Saves results to a file. Expected output: File populated with archived URL data.

**Command** (grep-filter-archived-urls):
```bash
grep -i "admin" archived_urls.txt
```

> Filters for potential admin paths. Expected output: Lines matching the pattern, revealing possible hidden directories.

## Expected Output

Successful execution produces a stream or file of archived snapshots, typically in CDX format: each line represents a captured URL with metadata like capture date and HTTP status. For a well-archived domain like owasp.com, expect thousands of entries spanning years, including old subdomains and query parameters that may indicate legacy features.
