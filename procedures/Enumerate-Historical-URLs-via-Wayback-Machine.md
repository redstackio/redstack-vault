---
type: procedure
description: >-
  Fetches historical URLs from the Internet Archive's Wayback Machine for a
  target domain and its subdomains to expand the attack surface during
  reconnaissance.
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Search Victim-Owned Websites]]'
sub_techniques: []
tags:
  - reconnaissance
  - wayback
  - url-enumeration
  - domain-discovery
commands:
  - '[[commands/waybackurls-enumerate-historical-urls]]'
platforms:
  - Linux
  - macOS
tools:
  - '[[tools/waybackurls]]'
validated: true
---

# Enumerate-Historical-URLs-via-Wayback-Machine

## Summary

This procedure retrieves all known historical URLs associated with a target domain and its subdomains from the Internet Archive's Wayback Machine. It is useful during the reconnaissance phase to identify archived web pages, subpaths, and endpoints that may no longer be live but can reveal application structure, technologies, or sensitive information for further enumeration or exploitation.

## Description

The Wayback Machine archives snapshots of websites over time, providing a rich source of historical data. This procedure uses the waybackurls tool, which queries the Wayback Machine's CDX API to fetch URLs matching the provided domains. Input is typically a list of subdomains (e.g., from prior enumeration tools like subfinder), and output is a deduplicated list of URLs. This expands the attack surface by uncovering forgotten or deprecated paths that might be vulnerable. It maps to MITRE ATT&CK technique T1594 (Search Open Websites/Domains) under the Reconnaissance tactic, as it passively gathers public web data without direct interaction with the target.

## Requirements

1. A list of target subdomains in a text file (one per line), obtained from prior reconnaissance (e.g., via [[procedures/Enumerate-Subdomains]]).
2. The waybackurls tool installed on a Linux or macOS system with Go runtime access.
3. Network access to the Internet Archive's APIs (no special authentication required, but rate limiting may apply).
4. Basic command-line proficiency; output file should be writable in the current directory.

## Defense

Defensive measures and detection strategies:

- Monitor for bulk queries to archive APIs like the Wayback Machine CDX server from reconnaissance tools.
- Implement web application firewalls (WAFs) to detect scraping or enumeration patterns derived from historical data.
- Regularly audit and remove deprecated endpoints from production to minimize information disclosure via archives.
- Use robots.txt and archive.org exclusions to prevent crawling of sensitive paths.

## Objectives

1. Collect a comprehensive list of historical URLs for the target domain to identify potential entry points.
2. Deduplicate and filter URLs for relevance in subsequent testing phases.
3. Uncover application details like directories, parameters, or technologies from archived snapshots.

## Instructions

### Step 1: Prepare the Subdomain List

**Context**: Ensure you have a clean list of subdomains for the target domain. This step verifies the input file exists and is formatted correctly (one subdomain per line, e.g., 'app.target.com'). If the file is empty or malformed, the procedure will fail to produce useful output.

If you don't have a subdomain list, generate one first using tools like subfinder. For this procedure, assume 'subdomains.txt' is ready.

**Expected Output**: A text file with subdomains like:
```
www.target.com
app.target.com
api.target.com
```

### Step 2: Execute WaybackURLs Enumeration

**Context**: Pipe the subdomain list into waybackurls to query the Wayback Machine. This fetches all archived URLs matching the domains. The tool handles deduplication internally and outputs unique URLs to a file. Use this step to gather historical data without alerting the target, as it queries public archives.

**Command** ([[commands/waybackurls-enumerate-historical-urls]]):
```bash
cat subdomains.txt | waybackurls > historical-urls.txt
```

> This command reads subdomains from stdin and writes URLs to stdout. If the input file has many domains, it may take several minutes due to API rate limits. Monitor for errors like connection timeouts, which indicate network issues or excessive load on the archive.

**Expected Output**: A text file 'historical-urls.txt' containing URLs like:
```
https://www.target.com/login
https://app.target.com/admin
https://api.target.com/v1/users
http://www.target.com/old-page.html
```

### Step 3: Verify and Filter Output

**Context**: Review the generated URLs for relevance and quality. This step includes basic validation to ensure the output is usable (e.g., no empty file, URLs are well-formed). Optionally, filter for specific protocols or paths using grep to focus on high-value targets like admin panels or APIs.

Run a quick check:
```bash
wc -l historical-urls.txt
head -10 historical-urls.txt
```

If needed, filter HTTPS only:
```bash
grep '^https' historical-urls.txt > https-urls.txt
```

**Expected Output**: Confirmation of non-zero lines in the file and sample URLs. Filtered file if applied.

**Success Indicators**:
- Output file contains at least 10+ unique URLs per subdomain.
- No API errors in command output (e.g., 429 rate limit).
- URLs parse correctly (valid scheme, host, path).

### Step 4: Integrate with Further Reconnaissance

**Context**: Use the historical URLs as input for active probing tools like httpx or gobuster. This decision point checks if the URLs reveal new subpaths; if so, proceed to vulnerability scanning. If the output is sparse, consider alternative sources like Common Crawl.

If URLs look promising, probe for live endpoints:
```bash
cat historical-urls.txt | httpx -silent > live-historical-urls.txt
```

**Expected Output**: A list of responsive URLs from the historical set.

**Success Indicators**:
- At least 20% of historical URLs respond (indicating persistent endpoints).
- Discovery of new paths not found in live enumeration.
