---
tags:
  - reconnaissance
  - dorking
  - api-discovery
type: procedure
tools:
  - '[[tools/Google-Search]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Hardware]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 9ec210d4-7d0d-475f-9acd-f64278c4ad1a
created_at: '2025-12-14T17:32:01.674Z'
updated_at: '2025-12-14T17:32:01.674Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Google-Dorking-for-Semrush-API-Endpoints

## Summary

This procedure uses Google dorking to identify publicly indexed API endpoints on Semrush subdomains, revealing unauthenticated access points for domain rank data.

## Description

In the context of reconnaissance against Semrush's API infrastructure, Google dorking leverages search engine indexing to uncover hidden or misconfigured endpoints. The target environment is the web-based Semrush API, where regional subdomains like uk.api.semrush.com expose raw data responses. Prerequisites include internet access and familiarity with advanced search operators. Expected outcomes are direct links to API responses containing sensitive analytics without authentication barriers.

## Requirements

1. Internet connection for Google searches
2. Knowledge of Google dorking syntax (e.g., site: operator)
3. No special tools beyond a web browser

## Defense

Defensive measures and detection strategies:

- Implement robots.txt and meta tags to prevent search engine indexing of API endpoints
- Use rate limiting and IP blocking on search engine crawlers
- Monitor Google search referrals in web logs for unusual dorking patterns

## Objectives

1. Discover indexed API endpoints on target subdomains
2. Identify potential unauthenticated access vectors
3. Gather initial intelligence on API structure and parameters

## Instructions

### Step 1: Craft and Execute Dorking Query

**Context**: Formulate a targeted search to limit results to Semrush API subdomains and reveal indexed responses.

No specific command; use Google Search interface:

Enter the query: `site:*.api.semrush.com`

> This restricts results to any subdomain under api.semrush.com. Expected output: A list of search results, typically 2-3, showing raw API responses with domain data from subdomains like uk.api.semrush.com.

### Step 2: Review and Collect Results

**Context**: Analyze the search results to extract usable endpoint URLs.

No specific command; manually note the URLs from the search snippets.

> Look for links that display JSON-like data in the preview, indicating direct API access. Expected output: URLs such as http://uk.api.semrush.com/?action=report&type=domain_rank&domain=example.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Google-Search]]

## Tags

- [[dorking]]
- [[api-discovery]]
