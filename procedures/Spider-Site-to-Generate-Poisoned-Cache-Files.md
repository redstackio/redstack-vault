---
tags:
  - web-crawling
  - cache-poisoning
  - stored-xss
type: procedure
tools:
  - '[[tools/Link-Spider]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/wget-spider-crawl]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: 5c07b375-ef89-43df-99be-5e83b7173b1c
created_at: '2025-12-14T03:15:26.542Z'
updated_at: '2025-12-14T03:15:26.542Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Spider-Site-to-Generate-Poisoned-Cache-Files

## Summary

This procedure uses a link spider to crawl a target site under a fake domain resolution, triggering full page caching in Concrete CMS to store pages with the attacker-controlled hostname embedded in links and BASE_URL, setting up stored XSS.

## Description

With the hosts file overridden, crawling the site causes the CMS's URL resolver to generate absolute URLs using the fake domain. These get cached server-side. The attack targets Concrete CMS without canonical URLs, where caching persists the manipulation. Prerequisites: Hosts override in place, caching enabled. Expected outcome: Server caches poisoned pages that serve the fake domain to future visitors, enabling XSS via malicious relative link alterations.

## Requirements

1. Hosts file overridden to map target IP to fake domain
2. Access to a web crawling tool like wget or a dedicated spider
3. Target site with full page caching enabled and no canonical URL

## Defense

Defensive measures and detection strategies:

- Set canonical URLs to lock hostname in URL generation
- Implement cache busting or validation to detect hostname anomalies
- Rate-limit crawling to prevent abuse; monitor for rapid page fetches

## Objectives

1. Force generation of cache files with fake hostname
2. Embed BASE_URL and links pointing to attacker-controlled domain
3. Enable stored XSS delivery without direct injection

## Instructions

### Step 1: Initiate Recursive Crawl

**Context**: Start spidering from the site's root under the fake domain to hit multiple pages and trigger caching.

**Command** ([[commands/wget-spider-crawl]]):
```bash
wget --spider --recursive --no-parent -U "Mozilla/5.0" -e robots=off https://fake-site.com/
```

> The --spider flag simulates requests without downloading; --recursive follows links. -U mimics a browser to avoid blocking. Expected output: List of fetched URLs; HTTP 200 responses indicating caching triggered.

### Step 2: Monitor Crawl Progress

**Context**: Ensure the crawl covers key pages where links are generated.

**Command** ([[commands/wget-spider-crawl]] with limits):
```bash
wget --spider --recursive --level=2 --no-parent https://fake-site.com/
```

> Limit depth with --level=2 to focus on main pages. Expected output: Completion log showing pages visited; verify via browser that fake domain loads target content.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/wget-spider-crawl]]

## Tools Used

- [[tools/Link-Spider]]

## Tags

- [[web-crawling]]
- [[cache-poisoning]]
