---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
name: Discover-Archived-Endpoints-with-Wayback-Machine
tags:
  - reconnaissance
  - web-archive
type: procedure
tools:
  - '[[tools/Wayback-Machine]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/wayback-machine-cdx-query]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-13T23:55:38.084Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Discover-Archived-Endpoints-with-Wayback-Machine

## Summary

This procedure uses the Wayback Machine to query archived web content and uncover hidden or deprecated endpoints on a target application, such as /reviews/ratings/{uuid}, to identify potential injection points for vulnerabilities like XSS.

## Description

In web application testing, many endpoints may be undocumented or removed from current documentation but still functional. By querying the Common Crawl Index (CDX) API of the Wayback Machine, attackers can retrieve a list of historical URLs, revealing attack surfaces. This is particularly useful for blind vulnerabilities where direct discovery is challenging. Prerequisites include internet access and basic knowledge of URL patterns.

## Requirements

1. Public internet access to web.archive.org
2. Target domain knowledge (e.g., app.pullrequest.com)
3. Command-line tool like curl for API queries

## Defense

Defensive measures and detection strategies:

- Monitor for unusual traffic to archival services from internal networks
- Implement web application firewalls (WAF) to detect reconnaissance patterns
- Regularly audit and document all endpoints to reduce hidden surfaces

## Objectives

1. Identify archived URLs matching target patterns
2. Expand reconnaissance on web applications
3. Locate potential vulnerability entry points

## Instructions

### Step 1: Query CDX API

**Context**: Use the CDX search to fetch archived URLs for the target domain.

**Command** ([[commands/wayback-machine-cdx-query]]):
```bash
http://web.archive.org/cdx/search/cdx?url=app.pullrequest.com/*&output=text&fl=original&collapse=urlkey
```

> This command queries the Wayback Machine for all archived pages under app.pullrequest.com, outputting original URLs in text format, collapsed by unique keys to avoid duplicates. Expected output is a list of URLs, e.g., https://app.pullrequest.com/reviews/ratings/{uuid}.

### Step 2: Analyze Results

**Context**: Parse the output to identify relevant endpoints.

No specific command; manually grep for patterns like "/reviews/" in the results.

> Review for functional endpoints that accept user input.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Websites

### Sub-Techniques


## Commands Used

- [[commands/wayback-machine-cdx-query]]

## Tools Used

- [[tools/Wayback-Machine]]

## Tags

- [[Reconnaissance]]
- [[web-archive]]
