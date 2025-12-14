---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - recon
  - web
  - url-parsing
type: procedure
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:27:23.324Z'
skill_level: beginner
impact_level: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Extract-Photo-ID-from-Zomato-URL

## Summary

This procedure involves inspecting Zomato photo URLs to extract the unique photo ID, which is essential for crafting targeted CSRF payloads to manipulate photo interactions.

## Description

In the context of exploiting Zomato's CSRF vulnerability, the attacker first identifies a target photo by browsing the site. The photo URL contains an encoded ID in the path, typically after `pv-res-[restaurant_id]-`, in a format like `r_[base64_string]`. This ID is used in POST requests to the photoViewerActionsHandler.php endpoint. Prerequisites include access to a web browser and the target Zomato site. Expected outcomes: A usable photo_id for subsequent exploitation steps.

## Requirements

1. Web browser with developer tools
2. Access to Zomato website
3. Basic URL parsing knowledge

## Defense

Defensive measures and detection strategies:

- Implement URL parameter logging to detect anomalous photo ID extractions
- Use client-side monitoring to flag scripted URL inspections

## Objectives

1. Obtain the exact photo_id from a Zomato photo URL
2. Prepare data for CSRF form construction
3. Enable targeted manipulation of specific photos

## Instructions

### Step 1: Navigate to Target Photo

**Context**: Locate the photo you wish to target on Zomato's site.

Browse to a restaurant's photo gallery and click on the desired photo. The URL updates to include the photo details.

**Expected Output**: URL like `https://www.zomato.com/es/photos/pv-res-18342981-r_2MzMzNTg1NzIwO`.

### Step 2: Parse the Photo ID

**Context**: Extract the ID from the URL path.

Inspect the URL and copy the segment after `pv-res-[number]-`, e.g., `r_2MzMzNTg1NzIwO` as the photo_id.

**Expected Output**: Isolated photo_id string ready for use.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[recon]]
- [[web]]
