---
tags:
  - information-disclosure
  - api
  - shopify
  - privacy
type: attack_chain
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-shopify-page-query]]'
verified: false
platforms:
  - Web
submitted: true
complexity: low
procedures:
  - '[[procedures/Query-Shopify-Public-API-for-Author-Disclosure]]'
step_count: 1
techniques:
  - '[[Gather Victim Identity Information]]'
description: >-
  Attack chain demonstrating the disclosure of Shopify store admin names via
  public API queries.
skill_level: beginner
impact_level: medium
id: 45535a56-bdb8-4a7b-9eb8-2ebb1b4f2a84
created_at: '2025-12-14T17:28:44.653Z'
updated_at: '2025-12-14T17:28:44.653Z'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Identity Information]]'
---
# Shopify API Author Name Disclosure

Multi-stage attack chain demonstrating a complete attack workflow.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 1 |
| Execution Time | ~1 minutes |
| Skill Level | Beginner |
| Complexity | Low |
| Impact Level | Medium |

## Attack Flow Visualization

```mermaid
graph LR
    A[Query Public API] --> B[Extract Admin Names]

    style A fill:#e74c3c
    style B fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- None (uses standard HTTP client like curl)

### Target Environment

- Web platform
- Shopify store with public API access
- No authentication required for vulnerable endpoints

### Initial Access Requirements

- Public internet access
- Knowledge of target Shopify store domain (e.g., store.myshopify.com)
- No prior credentials or access needed

## Detailed Attack Procedures

### Step 1: Query API for Page Data
procedure: [[procedures/Query-Shopify-Public-API-for-Author-Disclosure]]

**Objective**: Retrieve page data from the Shopify public API to expose author names of store admins.

**Instructions**: Identify a Shopify store and query its public API endpoint for pages. Use [[commands/curl-shopify-page-query]] to fetch the response:

```bash
curl -s "https://target-store.myshopify.com/admin/api/pages.json" | jq '.pages[] | {title: .title, author: .author}'
```

Parse the JSON response to extract the 'author' field containing first and last names.

**Expected Output**: JSON array of pages with author details, e.g., {"first_name": "John", "last_name": "Doe"}.

**Success Indicators**:
- API response includes 'author' field with personal names
- Names correspond to store admin identities

## Attack Chain Summary

### Key Achievements

1. Successful query of public API without authentication
2. Extraction of sensitive admin personal information
3. Demonstration of privacy disclosure across any Shopify store

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Gather Victim Identity Information]]

### MITRE ATT&CK Tactics

- [[Reconnaissance]]

---
*Last updated: 2023-10-01T00:00:00Z*
