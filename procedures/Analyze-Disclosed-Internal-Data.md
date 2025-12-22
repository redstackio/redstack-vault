---
tags:
  - analysis
  - social-engineering
  - information-disclosure
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Data from Information Repositories]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 83f499aa-d341-4831-96ec-6344c7ae4e53
created_at: '2025-12-14T17:25:59.608Z'
updated_at: '2025-12-14T17:25:59.608Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Information Repositories]]'
---
# Analyze Disclosed Internal Data

## Summary

This procedure reviews GraphQL response data to extract insights from office locations and beer inventories, identifying preferences for social engineering opportunities.

## Description

Post-exploitation, manual or scripted analysis of JSON reveals patterns like popular beers (e.g., low-remaining Witbier) tied to contacts. Targets internal culture data; no tools required beyond text editors or jq. Outcomes: Actionable intel for phishing or event interactions.

## Requirements

1. JSON responses from prior queries
2. jq or similar for parsing (optional)
3. Domain knowledge of target (e.g., Shopify offices)
4. Note-taking for insights

## Defense

Defensive measures and detection strategies:

- Minimize exposed internal data in APIs
- Anonymize or pseudonymize contacts
- Train on social engineering risks from leaks
- Regularly audit API disclosures

## Objectives

1. Identify beer preferences per location
2. Map contacts to insights
3. Plan social engineering vectors

## Instructions

### Step 1: Review Location Data

**Context**: Examine addresses and contacts for targeting.

**Command** (Manual or jq):
```bash
ej jq '.data.allLocations[] | {code, contact}' locations.json
```

> Lists codes and contacts. Expected output: "OTT150, 8th Floor" -> "Alana Plomp (@alana.plomp)".

### Step 2: Correlate Beer Data

**Context**: Link low-remaining beers to preferences.

**Command** (jq filter low %):
```bash
ej jq '.data.location.taps.edges[] | select(.node.percentRemaining < 10) | .node.beer' beer.json
```

> Finds popular items. Expected output: Witbier details indicating preference.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- analysis
- social-engineering
- information-disclosure
