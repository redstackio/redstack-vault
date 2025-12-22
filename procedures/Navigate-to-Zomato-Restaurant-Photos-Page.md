---
tags:
  - navigation
  - endpoint-access
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:14.410Z'
sub_techniques: []
id: dc960c2d-7cd8-49ae-acfd-f20bb28d682c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate-to-Zomato-Restaurant-Photos-Page

## Summary

This procedure directs the browser to a specific restaurant's photos page on Zomato's mobile site, where the vulnerable category parameter is used for filtering content.

## Description

The /photos endpoint on Zomato's mobile site reflects user input from the category parameter directly into a script tag without proper escaping. Navigating to a sample page like a Manila restaurant's photos sets up the environment for payload injection. This targets mobile users, where the impact includes client-side attacks like cookie theft.

## Requirements

1. Active mobile user agent simulation
2. Access to zomato.com
3. A valid restaurant URL (e.g., from search)

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected parameters in HTML/JS contexts
- Implement parameter whitelisting for category values
- Log and monitor access to sensitive endpoints like /photos

## Objectives

1. Load the vulnerable page with a benign category parameter
2. Verify reflection in page source
3. Position for parameter manipulation

## Instructions

### Step 1: Search for a Restaurant

**Context**: Identify a target restaurant to access its photos.

In the mobile-simulated browser, search for a restaurant on Zomato, such as "Artsy Cafe Diliman" in Manila.

### Step 2: Access Photos Endpoint

**Context**: Navigate to the photos page with an initial category.

Enter the URL: https://www.zomato.com/manila/artsy-cafe-diliman-quezon-city/photos?category=ambience

Inspect the page source to confirm the category value is reflected in a <script> tag.

**Expected Output**: Photos load, and source shows category="ambience" inside script without escaping.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[navigation]]
- [[endpoint-access]]
