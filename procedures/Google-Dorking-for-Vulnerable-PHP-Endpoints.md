---
id: proc-003
tags:
  - google-dorking
  - reconnaissance
  - php-vuln
type: procedure
tools:
  - '[[tools/Google-Dorking]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T03:46:25.975Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Google-Dorking-for-Vulnerable-PHP-Endpoints

## Summary

This reconnaissance procedure uses Google dorking to identify exposed PHP endpoints on target subdomains likely vulnerable to SQL injection, such as search or user pages with query parameters.

## Description

Google dorking leverages advanced search operators to uncover hidden web assets. In this attack, dorks like site:subdomain.gov inurl:.php were used to find injectable endpoints after initial access failed. Targets are PHP apps with poor input validation; outcomes include a list of URLs for targeted exploitation, expanding scope to shared databases.

## Requirements

1. Internet access to Google Search
2. Target domain/subdomain knowledge
3. Familiarity with dork syntax (site:, inurl:, ext:)

## Defense

Defensive measures and detection strategies:

- Use robots.txt and meta tags to limit search engine indexing
- Regularly audit exposed endpoints and remove unnecessary files
- Monitor search engine queries for domain-specific dorks

## Objectives

1. Discover hidden PHP files and forms
2. Identify potential SQLi entry points
3. Map subdomain attack surface

## Instructions

### Step 1: Basic Subdomain Dork

**Context**: Search for all PHP files on the subdomain.

Use Google: site:target-subdomain.gov filetype:php

> Expected: List of indexed PHP pages; note those with parameters like ?q= or ?id=.

### Step 2: Refine for Vulnerable Patterns

**Context**: Target forms or dynamic scripts.

Search: site:target-subdomain.gov inurl:search.php OR inurl:user.php

> Expected: Specific endpoints like search.php, ideal for SQLi testing; repeat for other subdomains.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Search Engines

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Dorking]]

## Tags

- [[recon]]
- [[dorking]]
