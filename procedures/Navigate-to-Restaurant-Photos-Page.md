---
id: proc-navigate-photos-page-230119
tags:
  - web-navigation
  - endpoint-discovery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-11-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:39.992Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Navigate-to-Restaurant-Photos-Page

## Summary

This procedure involves accessing a specific restaurant's photos page on Zomato's mobile site, which processes the 'category' parameter and sets the stage for XSS injection.

## Description

To exploit the reflected XSS, the attacker must first reach the vulnerable endpoint: the photos section of a restaurant page. Using a legitimate URL with a valid category (e.g., 'ambience') loads the page without suspicion. This step identifies the injection point where user input is reflected into a script context without proper escaping. Prerequisites include mobile user agent simulation; outcomes confirm the parameter is accepted and reflected.

## Requirements

1. Mobile-simulated browser session
2. Knowledge of a target restaurant URL on Zomato
3. Direct internet access

## Defense

Defensive measures and detection strategies:

- Rate-limit access to dynamic endpoints like /photos
- Log and monitor URL parameter manipulations
- Enforce HTTPS and validate referral headers

## Objectives

1. Load the photos endpoint with a benign category
2. Confirm 'category' parameter reflection in page source
3. Prepare for parameter tampering

## Instructions

### Step 1: Identify Target Restaurant

**Context**: Select a publicly listed restaurant to avoid access issues.

Search for a restaurant like 'Artsy Cafe' in Manila on Zomato and note its URL structure.

### Step 2: Construct and Visit Base URL

**Context**: Append the photos endpoint with a valid category to load the page.

Enter `https://www.zomato.com/manila/artsy-cafe-diliman-quezon-city/photos?category=ambience` in the address bar and press Enter.

> This displays photos filtered by ambience, with the parameter visible in the URL.

### Step 3: Inspect Page for Reflection

**Context**: Verify the parameter is processed and potentially vulnerable.

View page source (Ctrl+U) and search for 'category' to see if it's echoed into HTML or scripts.

**Expected Output**: Photos load, and source shows parameter usage.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web-navigation]]
- [[endpoint-discovery]]
