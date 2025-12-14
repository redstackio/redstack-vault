---
tags:
  - search-engine
  - dorking
  - information-disclosure
type: procedure
tools:
  - '[[tools/Google-Search]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/google-dork-passenger-site-grab]]'
  - '[[commands/google-dork-allinurl-email-site-target]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Social Media]]'
updated_at: '2025-12-14T17:24:44.767Z'
sub_techniques: []
id: b7569f48-56fe-43bd-a61a-1e5c06910cca
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Social Media]]'
---
# Verify-Search-Engine-Indexing-with-Google-Dorks

## Summary

This procedure uses Google dorks to check if the exposed Grab endpoint is indexed and cached by search engines, revealing publicly accessible sensitive data like partial auth_tokens.

## Description

Search engines like Google can index URLs with query parameters if not blocked, caching private content. By crafting dorks limited to the domain, attackers can retrieve cached pages showing disclosed information, amplifying the vulnerability's impact to potential privilege escalation.

## Requirements

1. Access to Google Search
2. Knowledge of the target domain (grab-attention.grabtaxi.com)
3. Basic understanding of Google dork syntax

## Defense

Defensive measures and detection strategies:

- Deploy robots.txt to disallow crawling of sensitive paths
- Add X-Robots-Tag: noindex headers to endpoints with tokens
- Regularly audit search engine caches and request removals via Google Search Console

## Objectives

1. Retrieve indexed or cached versions of the exposed endpoint
2. Confirm public availability of private data
3. Identify patterns for broader reconnaissance

## Instructions

### Step 1: Execute Domain-Specific Dork

**Context**: Search for the 'passenger' keyword on the target site to find indexed pages.

**Command** ([[commands/google-dork-passenger-site-grab]]):

Search query:
```
passenger site:grab-attention.grabtaxi.com
```

> This limits results to the domain and matches pages containing 'passenger', revealing cached passenger.html with exposed data.

### Step 2: Check for Email Leaks with Advanced Dork

**Context**: Use a general dork to detect URL-embedded emails, applicable to token leaks.

**Command** ([[commands/google-dork-allinurl-email-site-target]]):

Search query:
```
allinurl:@<mailbox_domain> site:<target_domain>
```

> Replace placeholders; expected to show URLs with leaked sensitive info like emails or tokens.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Social Media]] Search Engines

### Sub-Techniques


## Commands Used

- [[commands/google-dork-passenger-site-grab]]
- [[commands/google-dork-allinurl-email-site-target]]

## Tools Used

- [[tools/Google-Search]]

## Tags

- [[search-engine]]
- [[dorking]]
- [[information-disclosure]]
