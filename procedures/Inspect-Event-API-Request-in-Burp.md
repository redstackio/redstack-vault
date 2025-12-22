---
tags:
  - api-inspection
  - http-history
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:30:27.146Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: b15626ff-44cb-404c-abf8-cfdb57473b34
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Inspect-Event-API-Request-in-Burp

## Summary

This procedure uses Burp Suite to locate and examine the HTTP GET request to FetLife's event API endpoint in the proxy history.

## Description

After accessing the event page, the API response contains JSON with event data. Burp's HTTP history allows filtering and viewing without active interception. This reveals the vulnerability where privacy settings are not enforced at the backend.

## Requirements

1. Active Burp proxy session with traffic captured
2. Event page accessed to generate the request
3. Basic familiarity with Burp's interface

## Defense

Defensive measures and detection strategies:

- Strip sensitive fields from API responses based on user roles
- Use HTTPS and monitor for proxy artifacts in logs
- Implement API gateway with authorization enforcement

## Objectives

1. Isolate the specific API request for the event
2. Access the full response payload
3. Prepare for searching hidden data

## Instructions

### Step 1: Open HTTP History

**Context**: Review captured traffic post-page load.

In Burp, go to Proxy > HTTP History.

> Expected: List of requests including FetLife domains.

### Step 2: Filter for Event Request

**Context**: Narrow down to the relevant endpoint.

Filter by URL containing '/events/' or GET method to {event-id}.

> Expected: Single or few matching entries; select the primary GET.

### Step 3: View Request Details

**Context**: Examine headers and body if any.

Click the request to open Inspector.

> Expected: Standard GET with auth cookies, no payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[api-inspection]]
- [[http-history]]
