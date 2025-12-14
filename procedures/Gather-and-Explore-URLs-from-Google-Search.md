---
id: proc-uuid-1
tags:
  - reconnaissance
  - url-scraping
type: procedure
tools:
  - '[[tools/Google-Search]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/google-search-scrape]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-13T23:52:38.855Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Gather-and-Explore-URLs-from-Google-Search

## Summary

This procedure involves using Google Search to gather URLs from the target domain (e.g., data.gov) and manually exploring them to identify potential injection points in forms and parameters.

## Description

In the context of web vulnerability hunting, reconnaissance is key to discovering endpoints vulnerable to injection attacks. This procedure scrapes URLs via Google dorks and manually tests for reflections, focusing on form parameters like media_url in WordPress-based sites. It sets the stage for targeted exploitation without requiring authenticated access.

## Requirements

1. Internet access to Google Search.
2. A text editor or script to process URL lists.
3. Browser like Firefox for manual testing.

## Defense

Defensive measures and detection strategies:

- Monitor search engine queries for domain-specific scraping.
- Implement rate limiting on public endpoints to hinder manual exploration.

## Objectives

1. Collect a comprehensive list of target URLs.
2. Identify endpoints with user-controllable parameters.
3. Uncover reflection points for injection testing.

## Instructions

### Step 1: Scrape URLs with Google Search

**Context**: Query Google for site-specific URLs to build a testing list.

**Command** ([[commands/google-search-scrape]]):
```bash
google-search "site:data.gov" > urls.txt
```

> This command (simulating a search tool or manual copy-paste) outputs a file with URLs. Manually review for forms on /issue/, /story/, etc.

### Step 2: Manual Exploration

**Context**: Test URLs for parameter reflections.

**Command** (No specific command; use browser dev tools):

Open urls.txt in Firefox and inspect responses for echoed inputs.

> Look for unescaped parameters in HTML output.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/google-search-scrape]]

## Tools Used

- [[tools/Google-Search]]

## Tags

- [[Reconnaissance]]
- [[url-scraping]]
