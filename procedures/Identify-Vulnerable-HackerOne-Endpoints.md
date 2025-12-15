---
id: proc-uuid-001
tags:
  - reconnaissance
  - endpoint-discovery
type: procedure
tools:
  - '[[tools/Browser-Console]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T17:27:50.110Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Identify-Vulnerable-HackerOne-Endpoints

## Summary

This procedure identifies JSON API endpoints on HackerOne that lack CSRF protection and exhibit timing variations based on query results, setting the foundation for side-channel inference attacks.

## Description

In a web environment targeting HackerOne's platform, manually inspect public-facing JSON endpoints for CSRF vulnerabilities. Test GET requests to confirm unauthenticated access and measure response sizes for consistent (e.g., empty queries) versus variable (e.g., user-specific data) cases. Endpoints like `/bugs.json` return ~750 bytes for no results but grow with record counts (~185 bytes per record post-gzip), enabling timing-based leaks when loaded cross-origin.

## Requirements

1. Access to a modern browser for testing requests
2. Knowledge of HackerOne's API parameters (e.g., `text_query`, `substates[]`)
3. No special credentials; endpoints are public

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing or sensitive endpoints
- Add CORS restrictions to block cross-origin resource loads
- Monitor for anomalous request patterns from third-party domains

## Objectives

1. Locate unprotected endpoints for timing exploitation
2. Confirm response size variability for inference potential
3. Map parameters like `sort_type=pg_search_rank` that influence processing time

## Instructions

### Step 1: Test Endpoint Accessibility

**Context**: Verify endpoints accept unauthenticated GET requests without CSRF.

**Command** (Manual Browser Test):
Open browser console and navigate to `https://hackerone.com/bugs.json?text_query=999999&subject=&sort_type=pg_search_rank&substates%5B%5D=triaged`.

> This loads a consistent ~750-byte response for empty results. Repeat for `/programs/search.json?query=IBB` (~9200 bytes fixed).

### Step 2: Analyze Response Variations

**Context**: Probe with variable queries to observe size differences.

**Command** (Browser Fetch):
Use console: `fetch('https://hackerone.com/bugs.json?text_query=3480&substates%5B%5D=new').then(r => r.text()).then(t => console.log(t.length));`

> Expected varying lengths based on logged-in user's data; compare to baseline.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Scanning IP Blocks

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Console]]

## Tags

- [[Reconnaissance]]
- [[web-api]]
