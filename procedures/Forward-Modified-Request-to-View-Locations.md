---
id: proc-forward-request-view-001
tags:
  - data-exfiltration
  - web
  - privacy
  - yelp
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
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:23.153Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Forward-Modified-Request-to-View-Locations

## Summary

This procedure forwards the tampered Yelp edit request through Burp Suite to trigger the server response, resulting in the unauthorized display of another user's saved profile locations.

## Description

After modifying the locid, forwarding the request to the /profile_location/add_or_edit endpoint causes the server to return the targeted user's location data without validation. This collects sensitive information like addresses, potentially logged in server access logs (e.g., Apache). The procedure assumes a proxied, authenticated session on the web platform and highlights privacy risks from IDOR flaws.

## Requirements

1. Modified request ready in Burp Suite
2. Valid session cookies intact
3. Target endpoint accessible via HTTPS

## Defense

Defensive measures and detection strategies:

- Sanitize and anonymize location data in responses if not user-owned
- Implement logging of all parameter accesses with user correlation for forensic analysis
- Use data loss prevention (DLP) tools to scan for sensitive location patterns in responses

## Objectives

1. Execute the modified request to retrieve unauthorized data
2. Observe and collect disclosed location information
3. Validate the IDOR exploitation success

## Instructions

### Step 1: Review Modified Request

**Context**: Double-check the tampered locid before sending.

No specific command; in Burp, inspect the full request headers, query parameters, and body.

> Confirm locid change and session cookies are present.

### Step 2: Forward and Observe Response

**Context**: Release the request to the server and capture the output.

No specific command; click 'Forward' in Burp's proxy interceptor.

> The response renders the edit form populated with the target user's location data, confirming disclosure.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- data-exfiltration
- web
- privacy
- yelp
