---
tags:
  - data-extraction
  - coordinates
  - disclosure
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:30:27.134Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques:
  - '[[T1005.001]]'
id: 28c3b040-eeb2-4d63-89ba-b672fdd4d722
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Extract-Location-Coordinates-from-Response

## Summary

This procedure searches the API response in Burp Suite to extract reversed location coordinates, correcting them to reveal the exact event venue despite privacy settings.

## Description

The FetLife API returns JSON with a 'location' field containing lat/long swapped (e.g., long first). Searching for 'location' uncovers this, allowing mapping on external tools like Google Maps. This bypasses frontend privacy, exposing physical locations and risking user safety.

## Requirements

1. Selected API response in Burp
2. Knowledge of coordinate format (lat/long vs long/lat)
3. Access to mapping service like Google Maps

## Defense

Defensive measures and detection strategies:

- Remove or encrypt coordinates in API responses for unauthorized users
- Validate privacy settings server-side before including data
- Audit API responses for PII leakage in security reviews

## Objectives

1. Identify and parse the leaked location data
2. Correct formatting errors to obtain usable coordinates
3. Demonstrate impact by geolocating the venue

## Instructions

### Step 1: Open Response Tab

**Context**: Access the full API payload.

In Burp Inspector, switch to Response tab.

> Expected: Raw JSON or HTML with embedded data.

### Step 2: Search for Location

**Context**: Locate the sensitive field.

Use Ctrl+F to search 'location' in the response body.

> Expected: Snippet like "location": [131.04425, -12.496252].

### Step 3: Extract and Correct

**Context**: Interpret and validate coordinates.

Note values, swap to [-12.496252, 131.04425] (lat, long), search on Google Maps.

> Expected: Pin drops on exact address, confirming disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System

### Sub-Techniques

- [[T1005.001]] Web Browser Data (adapted for API)

## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[data-extraction]]
- [[coordinates]]
- [[disclosure]]
