---
id: proc-observe-geo-fetch
tags:
  - information-disclosure
  - geolocation
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T17:28:12.378Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Observe-Geolocation-Data-Fetch-in-Iframe

## Summary

This procedure tests and observes the geolocation data returned by the embedded GeoAPI iframe, confirming the vulnerability allows unauthorized access to IP and location details.

## Description

Loading the clickjacking HTML triggers a GET request to https://geoapi.acronis.com/?q=admin/views/ajax/autocomplete/user/a, which responds with unauthenticated JSON based on the requester's IP. The response includes sensitive details like latitude/longitude (with accuracy radius), city, region, country, timezone, and IP. This step validates the data exposure before integrating capture mechanisms. Target environment is any browser; no server-side access needed.

## Requirements

1. Local HTML file from previous procedure
2. Web browser with DevTools (e.g., Chrome)
3. Internet access to reach geoapi.acronis.com

## Defense

Defensive measures and detection strategies:

- Require authentication for geolocation APIs
- Rate-limit requests by IP to prevent abuse
- Log and alert on high-volume geo queries

## Objectives

1. Confirm JSON response contains victim-specific geo data
2. Identify key fields for exfiltration (IP, coordinates)
3. Ensure fetch occurs without user consent

## Instructions

### Step 1: Load HTML in Browser

**Context**: Open the file to initiate the iframe request.

No command; double-click Clickjacking.html or use file:// URL.

> Browser loads the page, iframe requests data silently.

### Step 2: Inspect Network Response

**Context**: Use DevTools to view the fetched JSON.

Open DevTools (F12), go to Network tab, reload page, and filter for geoapi.acronis.com.

**Expected Output**: JSON like {"city":"Abu Kabir","country":{"name":"Egypt","code":"EG"},"location":{"accuracy_radius":1000,"latitude":30.7251,"longitude":31.6715,"time_zone":"Africa\/Cairo"},"region":{"name":"Sharqia","code":"SHR"},"ip":"154.237.109.156"}

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Hardware]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[information-disclosure]]
- [[geolocation]]
