---
tags:
  - recon
  - id-gathering
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
  - Mobile API
techniques:
  - '[[Account Discovery]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 2f6be29c-898f-41ea-89f2-a04c55fa890e
created_at: '2025-12-14T17:25:29.761Z'
updated_at: '2025-12-14T17:25:29.761Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Reconnaissance to Obtain Restaurant IDs

## Summary

This procedure focuses on researching Zomato's application structure over time to identify and obtain critical IDs like user_id and res_id, targeting a safe test restaurant to prepare for IDOR exploitation.

## Description

Extended reconnaissance reveals the API's ID usage patterns. By exploring the app, attackers map out restaurant IDs and select non-production targets like Zomato-owned test restaurants (res_id=XXXXXX). This avoids real impact while confirming exploit feasibility. Requires weeks of observation but no special tools.

## Requirements

1. Persistent access to Zomato app
2. Ability to browse restaurant listings and extract IDs from URLs or responses
3. Ethical targeting (e.g., test environments)

## Defense

Defensive measures and detection strategies:

- Rate-limit API reconnaissance endpoints
- Monitor for repeated ID queries from single sessions
- Use CAPTCHA or behavioral analysis for suspicious browsing

## Objectives

1. Identify valid res_id for target restaurants
2. Extract user_id from authenticated requests
3. Ensure target is low-impact (e.g., internal test)

## Instructions

### Step 1: Explore App Structure

**Context**: Browse Zomato to understand ID flows and identify test restaurants.

> Search for restaurants and note res_id in URLs (e.g., /restaurant/XXXXXX). Research for weeks to find Zomato-owned tests.

### Step 2: Extract User ID

**Context**: From session data, pull user_id.

> Inspect network requests in dev tools for user_id in headers or payloads.

**Expected Output**: res_id=XXXXXX and user_id=XXXX.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[id-gathering]]
