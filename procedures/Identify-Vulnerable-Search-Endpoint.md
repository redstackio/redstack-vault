---
id: proc-identify-search-endpoint
tags:
  - recon
  - web
  - sqli
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-basic-get]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:28:28.625Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Vulnerable Search Endpoint

## Summary

This procedure involves locating and analyzing the search functionality of a web application to identify potential SQL injection entry points in the query input parameter.

## Description

In web applications, search features often directly query backend SQL databases without adequate input validation. By inspecting the search form or URL parameters, attackers can pinpoint vulnerable endpoints. This step is crucial for confirming the attack surface in unauthenticated areas, leading to potential data exposure as seen in the exploitation of unpublished posts.

## Requirements

1. Access to a web browser or command-line tool like curl
2. Publicly accessible target website with search functionality
3. Basic knowledge of HTTP requests and URL parameters

## Defense

Defensive measures and detection strategies:

- Implement web application firewalls (WAF) to monitor search inputs
- Use parameterized queries in backend code to prevent injection
- Log and alert on anomalous search queries with special characters

## Objectives

1. Locate the search query parameter (e.g., ?q=)
2. Verify database interaction via response analysis
3. Prepare for payload testing

## Instructions

### Step 1: Locate Search Page

**Context**: Navigate to the target's search interface to understand the input mechanism.

**Command** ([[commands/curl-basic-get]]):
```bash
curl "https://target.com/search" -v
```

> This fetches the search page HTML. Inspect the form action and input name (e.g., <input name="q">) to identify the parameter.

### Step 2: Perform Normal Search

**Context**: Submit a benign query to observe normal behavior and network requests.

**Command** ([[commands/curl-basic-get]]):
```bash
curl "https://target.com/search?q=test" -v
```

> Check response for reflected input or database hints (e.g., result counts). Use browser dev tools for deeper inspection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/curl-basic-get]]

## Tools Used


## Tags

- recon
- web
