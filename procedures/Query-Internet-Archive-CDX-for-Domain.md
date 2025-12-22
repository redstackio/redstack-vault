---
id: proc-cdx-query-2380084
tags:
  - osint
  - reconnaissance
  - internet-archive
type: procedure
tools:
  - '[[tools/Web-Archive-CDX-Search]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-cdx-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Search Open Websites-Domains]]'
updated_at: '2025-12-14T17:32:29.092Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques:
  - '[[Search Engines]]'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Search Open Websites-Domains]]'
---
# Query Internet Archive CDX for Domain

## Summary

This procedure retrieves a list of archived URLs for a specified domain using the Internet Archive's CDX (Capture Index) search API, enabling reconnaissance of historical web content that may contain sensitive information.

## Description

The Internet Archive's Wayback Machine indexes web pages, and the CDX API allows querying for captures of a domain. This is useful in OSINT scenarios to find exposed data in archived client-side files, such as JavaScript configurations. In the Mozilla case, this exposed API keys in subscriptions.firefox.com archives. Prerequisites include internet access; no authentication needed.

## Requirements

1. Internet connection to access web.archive.org
2. curl or similar HTTP client installed
3. Target domain known (e.g., subscriptions.firefox.com)

## Defense

Defensive measures and detection strategies:

- Request domain exclusion from Internet Archive via robots.txt or direct contact
- Avoid embedding secrets in client-side code; use server-side rendering
- Monitor archives periodically for sensitive data exposure

## Objectives

1. Gather archived URLs for the target domain
2. Identify potential sources of information disclosure
3. Enable further analysis of historical content

## Instructions

### Step 1: Construct and Execute CDX Query

**Context**: Build the CDX search URL with parameters to filter by domain and retrieve original URLs.

**Command** ([[commands/curl-cdx-query]]):
```bash
curl "https://web.archive.org/cdx/search/cdx?url=TARGET_DOMAIN/*&collapse=urlkey&output=text&fl=original" > archived_urls.txt
```

> This command queries the CDX endpoint, collapses duplicates, outputs in text format, and saves to a file. Replace TARGET_DOMAIN with the actual domain (e.g., subscriptions.firefox.com). Expected output is a list of archived original URLs.

### Step 2: Verify Query Results

**Context**: Check the file for successful retrieval and domain matches.

**Command** ([[commands/cat-display]]):
```bash
cat archived_urls.txt | head -10
```

> Displays the first 10 lines to confirm URLs from the target domain are present.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Search Open Websites-Domains]] Search Open Technical Databases or Platforms

### Sub-Techniques

- [[Search Engines]] Search Open Domains and DNS

## Commands Used

- [[commands/curl-cdx-query]]
- [[commands/cat-display]]

## Tools Used

- [[tools/Web-Archive-CDX-Search]]

## Tags

- [[osint]]
- [[Reconnaissance]]
- [[internet-archive]]
