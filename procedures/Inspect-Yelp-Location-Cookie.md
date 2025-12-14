---
id: proc-inspect-yelp-cookie-001
tags:
  - recon
  - cookie
  - web
type: procedure
tools:
  - '[[tools/Chrome-Developer-Tools]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:16:30.984Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Inspect-Yelp-Location-Cookie

## Summary

This procedure involves using browser developer tools to inspect the Yelp location cookie, revealing its URL-encoded JSON structure containing user location data like city, state, and country, which can be targeted for tampering in self-XSS attacks.

## Description

In the context of testing Yelp's web application, inspect the 'location' cookie set during user authentication or location-based interactions. The cookie stores location details in JSON format, URL-encoded for transmission. This step is prerequisite for identifying injectable fields like 'city' without server-side validation. Expected outcome is understanding the cookie's parseable structure for subsequent modifications.

## Requirements

1. Authenticated session on yelp.com
2. Browser with developer tools (e.g., Chrome)
3. Network access to yelp.com

## Defense

Defensive measures and detection strategies:

- Implement cookie prefixing (e.g., __Host-) to prevent client-side modification
- Server-side validation of cookie contents before use
- Monitor for anomalous cookie values in logs

## Objectives

1. Reveal cookie structure for vulnerability assessment
2. Identify user-controlled fields like 'city'
3. Prepare for payload injection

## Instructions

### Step 1: Open Developer Tools

**Context**: Access the browser's inspection capabilities to view site cookies.

Use [[tools/Chrome-Developer-Tools]] to open the Application tab (or Storage in Firefox) and expand Cookies under yelp.com.

### Step 2: Locate and Decode Cookie

**Context**: Find the specific location cookie and decode its value to view the JSON.

Select the 'location' cookie and copy its value, then use a URL decoder (built-in or online) to reveal the JSON payload.

**Expected Output**: JSON object such as {"city": "San Francisco", "zip": "", "country": "US", "address2": "", "address3": "", "state": "CA", "address1": "", "unformatted": "San Francisco, CA"}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chrome-Developer-Tools]]

## Tags

- recon
- cookie
- web
