---
tags:
  - information-disclosure
  - api
  - shopify
  - privacy
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/curl-shopify-page-query]]'
verified: false
platforms:
  - Web
submitted: true
techniques:
  - '[[Gather Victim Identity Information]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 7cfe2481-ebee-465c-bf2b-f1018c42550a
created_at: '2025-12-14T17:28:44.649Z'
updated_at: '2025-12-14T17:28:44.649Z'
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Identity Information]]'
---
# Query-Shopify-Public-API-for-Author-Disclosure

## Summary

This procedure outlines querying the Shopify public API to retrieve page data, which inadvertently exposes the first and last names of store admin authors. It targets the lack of access controls on the author field in API responses, allowing unauthorized disclosure of personal information for any Shopify store.

## Description

In the vulnerable Shopify setup, the public API endpoints for page data included author metadata without proper authentication or authorization checks. By sending a simple GET request to the pages endpoint, attackers could enumerate admin names across stores. This privacy issue affected all stores using the API and was mitigated by Shopify removing the author field from public responses. The procedure assumes a target store domain and uses HTTP requests to fetch and parse the data, highlighting reconnaissance via exposed APIs.

## Requirements

1. Internet access to reach the target Shopify store
2. Basic knowledge of HTTP requests and JSON parsing (e.g., using jq)
3. Target Shopify store URL (e.g., target-store.myshopify.com)

## Defense

Defensive measures and detection strategies:

- Remove sensitive fields like author names from public API responses
- Implement API authentication (e.g., API keys or OAuth) for all endpoints
- Monitor API logs for unusual query patterns to the pages endpoint
- Use rate limiting on public APIs to prevent enumeration

## Objectives

1. Gather personal identity information of store admins
2. Demonstrate privacy disclosure without authentication
3. Validate the vulnerability on target stores

## Instructions

### Step 1: Identify Target Store and Query API

**Context**: Locate a Shopify store and send an HTTP GET request to the public pages API endpoint to retrieve page data including author details.

**Command** ([[commands/curl-shopify-page-query]]):
```bash
curl -s "https://target-store.myshopify.com/admin/api/pages.json" | jq '.pages[] | {title: .title, author: {first_name: .author.first_name, last_name: .author.last_name}}'
```

> This command fetches the JSON response from the pages endpoint and uses jq to filter and display page titles along with author first and last names. Successful output reveals admin identities, such as {"title": "About Us", "author": {"first_name": "Jane", "last_name": "Smith"}}. If the author field is present, the disclosure is confirmed.

### Step 2: Parse and Validate Disclosure

**Context**: Review the response to confirm exposure of personal information and enumerate multiple pages if needed.

**Command** ([[commands/curl-shopify-page-query]]):
```bash
curl -s "https://target-store.myshopify.com/admin/api/pages.json" | jq '.["pages"][].author'
```

> This extracts only the author objects from the response. Expected output is an array of admin details. Cross-reference names with public store info to validate impact.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Gather Victim Identity Information]]

### Sub-Techniques


## Commands Used

- [[commands/curl-shopify-page-query]]

## Tools Used


## Tags

- [[information-disclosure]]
- [[api]]
- [[shopify]]
- [[privacy]]
