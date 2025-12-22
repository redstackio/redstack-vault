---
id: 9b853166-0a76-4174-8572-1ae69da6acd0
name: Wayback-Machine-Lookup
type: procedure
verified: true
submitted: false
created_at: '2020-07-24T17:11:26.088948+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[Search Victim-Owned Websites]]'
sub_techniques: []
tags:
  - osint
  - reconnaissance
  - web-archive
  - wayback-machine
commands:
  - '[[commands/waybackurls-fetch-domain-urls]]'
platforms:
  - Linux
  - Web
tools:
  - '[[tools/waybackurls]]'
validated: true
---

# Wayback-Machine-Lookup

## Summary

This procedure uses the Wayback Machine to retrieve historical snapshots of a target domain's web pages, helping to identify archived content, past subdomains, directories, and endpoints that may reveal sensitive information or attack surfaces not visible on the live site. It is commonly used in reconnaissance phases of penetration testing or OSINT investigations to expand the attack surface.

## Description

The Wayback Machine, operated by the Internet Archive, stores billions of web pages over time, allowing users to access historical versions of websites. In security contexts, this procedure enables attackers or testers to discover forgotten or removed content such as old login pages, API endpoints, admin panels, or leaked data that could aid in further exploitation. The technique involves querying the archive via command-line tools for efficiency, focusing on a target domain to extract unique URLs. This maps to MITRE ATT&CK's Reconnaissance tactic, specifically searching open websites and domains to gather victim information without direct interaction with the live target.

## Requirements

1. Internet access to query the Wayback Machine API.
2. The waybackurls tool installed (see [[tools/waybackurls]] for installation).
3. Target domain name (e.g., example.com) resolved and in scope for reconnaissance.
4. Basic command-line proficiency; no elevated privileges required.

## Defense

Defensive measures include monitoring for automated scraping of public archives (though difficult to attribute), implementing robots.txt historically to discourage archiving, or using private CDNs/services that limit public snapshots. Detection can involve anomaly detection in OSINT tool usage logs or web application firewalls alerting on reconnaissance patterns.

## Objectives

1. Retrieve a comprehensive list of historical URLs for the target domain.
2. Identify potential sensitive endpoints or subdomains from archived content.
3. Expand reconnaissance data for mapping the attack surface.

## Instructions

### Step 1: Prepare the Target Domain

**Context**: Start by confirming the target domain and ensuring you have a clean working directory to store output. This step sets up the environment and avoids querying irrelevant data.

No command required here; manually note the target domain (e.g., target.com) and create an output file if needed.

> This preparation ensures focused queries and easy verification of results.

### Step 2: Fetch Historical URLs Using Waybackurls

**Context**: Use the waybackurls tool to query the Wayback Machine API and extract all unique URLs associated with the target domain. This step performs the core lookup, filtering out duplicates and non-HTTP/HTTPS schemes for relevance in web reconnaissance.

**Command** ([[commands/waybackurls-fetch-domain-urls]]):
```bash
waybackurls $_TARGET_DOMAIN > wayback_urls.txt
```

> Run this command from a terminal with internet access. The tool will contact the Wayback Machine's CDX API to retrieve and deduplicate URLs. Expected runtime is 10-60 seconds depending on the domain's archive size. Verify the output file contains URLs like http://target.com/old-endpoint or https://sub.target.com/admin.

### Step 3: Review and Filter Results

**Context**: Examine the output file to identify valuable URLs, such as those pointing to admin panels, backups, or JavaScript files that might contain secrets. Use grep or manual inspection to filter for patterns like /admin, .js, or /backup.

**Command** (using standard bash tools, no custom command):
```bash
grep -i "admin\|login\|backup" wayback_urls.txt > interesting_urls.txt
```

> This step refines the data for actionable intelligence. Success is indicated by the presence of URLs that reveal hidden site structure or potential vulnerabilities.

### Step 4: Validate Live URLs (Optional)

**Context**: Cross-check archived URLs against the live site to see if they still exist or redirect, using a tool like httpx for probing. This helps prioritize live attack surfaces discovered via archives.

Reference [[commands/httpx-probe-live-urls]] (not included in this procedure's commands array, but recommended for chaining).

> If any URLs respond (status 200), they may be exploitable; otherwise, note for historical context only.
