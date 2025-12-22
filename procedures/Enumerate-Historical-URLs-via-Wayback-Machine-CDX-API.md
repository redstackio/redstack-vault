---
type: procedure
verified: true
submitted: true
tactics:
  - '[[Reconnaissance]]'
techniques:
  - '[[T1594.001]]'
sub_techniques: []
tags:
  - recon
  - osint
  - wayback
  - archive
  - url-enumeration
commands:
  - '[[commands/curl-wayback-cdx-query]]'
tools:
  - '[[tools/concurl]]'
platforms:
  - Web
skill_level: beginner
impact_level: low
detection_risk: low
created_at: '2020-07-24T17:11:26.639013+00:00'
updated_at: '2023-05-26T00:48:41.057884+00:00'
validated: true
---

# Enumerate-Historical-URLs-via-Wayback-Machine-CDX-API

## Summary

This procedure allows security testers to directly query the Internet Archive's Wayback Machine CDX API to retrieve a flattened list of historical URLs captured for a specific domain. This is useful during reconnaissance to identify past website versions, exposed directories, files, or endpoints that may reveal sensitive information, outdated vulnerabilities, or changes in site structure not visible on the live site.

## Description

The Wayback Machine at archive.org stores snapshots of websites over time. Its CDX (Capture Data eXtended) API provides a programmatic way to search and retrieve metadata about archived captures without browsing the web interface. By querying with a wildcard pattern like `*.example.com/*`, you can obtain a text list of original URLs that were archived, collapsed by unique URL key to avoid duplicates. This technique falls under reconnaissance as it gathers publicly available historical data about a target domain, potentially uncovering hidden assets or legacy content. It requires no authentication and works over standard HTTP, but rate limits may apply for heavy usage. For concurrent queries across multiple domains, tools like concurl can parallelize requests to improve efficiency.

## Requirements

1. Internet access to reach archive.org.
2. curl installed (standard on most Linux/macOS systems; available via package managers on Windows).
3. Target domain name (e.g., example.com) to enumerate.
4. Optional: concurl tool for handling multiple concurrent queries if enumerating many domains.

## Defense

Defensive measures and detection strategies:

- Monitor for automated scraping of archive.org, though this is public data and hard to block.
- Implement website changes to remove sensitive endpoints from future crawls (e.g., via robots.txt, though not retroactive).
- Use web application firewalls (WAFs) to detect reconnaissance patterns on live sites informed by historical data.
- Regularly audit and clean historical exposures by requesting removals from archive.org if eligible (e.g., for personal data under GDPR).

## Objectives

1. Retrieve a comprehensive list of historical URLs for the target domain.
2. Identify potential attack surfaces from past site structures.
3. Support further OSINT by feeding URLs into other tools for content retrieval.

## Instructions

### Step 1: Construct the CDX API Query URL

**Context**: Build the API endpoint using the target's domain. The wildcard `*.domain/*` captures all subpaths under the domain, `output=text` returns plain text, `fl=original` limits output to the original URL field, and `collapse=urlkey` deduplicates entries based on normalized URL keys.

Replace `$_DOMAIN` with the target (e.g., example.com). No command needed here; this is manual URL construction.

> This step ensures the query is targeted and efficient, avoiding unnecessary data.

### Step 2: Execute the CDX API Query Using curl

**Context**: Use curl to fetch the list of historical URLs. This sends a GET request to the CDX server and saves the output to a file for analysis. The response is a newline-separated list of URLs, one per archived capture.

**Command** ([[commands/curl-wayback-cdx-query]]):
```bash
curl "http://web.archive.org/cdx/search/cdx?url=*.$_DOMAIN/*&output=text&fl=original&collapse=urlkey" -o wayback_urls.txt
```

> Run this in a terminal. If the domain has many captures, the file may be large (e.g., thousands of lines). Success is indicated by a 200 OK response and non-empty output file. For example, querying a popular site like google.com might return URLs like `https://google.com/search?q=term` from past snapshots.

### Step 3: Analyze and Filter Results (Optional Enhancement with concurl)

**Context**: If querying multiple domains or needing faster parallel execution, use concurl to run concurrent curl requests. This step processes the output file to filter for interesting paths (e.g., admin panels) or feeds into other tools like httpx for live checks.

First, prepare a list of domains in a file (domains.txt), then use concurl:

**Command** (using [[tools/concurl]]):
```bash
concurl -input domains.txt -c 10 -o results/wayback_%d.txt 'http://web.archive.org/cdx/search/cdx?url=*.$_DOMAIN/*&output=text&fl=original&collapse=urlkey'
```

> Here, `-c 10` sets 10 concurrent connections. Each output file (wayback_1.txt, etc.) contains URLs for one domain. Grep for patterns like `/admin` or `/backup` to find valuables: `grep -i 'admin\|backup' wayback_urls.txt`. This enhances scalability for broad recon.
