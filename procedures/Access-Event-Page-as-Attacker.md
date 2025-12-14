---
tags:
  - unauthorized-access
  - event-view
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:27.149Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 09dbe5c0-0687-489e-8c96-f45799b8e262
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access-Event-Page-as-Attacker

## Summary

This procedure simulates an unauthorized user viewing a FetLife event page without RSVPing, triggering the API call that leaks location data.

## Description

The attacker navigates to the event URL directly, which fetches details via API. Even with privacy set, the response includes coordinates. This step relies on the public-facing nature of event pages, assuming no bans or restrictions.

## Requirements

1. Attacker account logged in
2. Known event ID from victim setup
3. Proxied browser to capture the request

## Defense

Defensive measures and detection strategies:

- Restrict event page access to invited users only
- Implement authorization checks on API endpoints for sensitive data
- Rate-limit page views and monitor for scraping patterns

## Objectives

1. Trigger the vulnerable API request without authentication escalation
2. Ensure the response is captured for analysis
3. Confirm no frontend blocks prevent access

## Instructions

### Step 1: Log In as Attacker

**Context**: Switch to attacker persona.

Log out of victim, log in as 'Ezzra1'.

> Expected: Successful login to dashboard.

### Step 2: Navigate to Event

**Context**: Load the target event page.

Enter https://fetlife.com/events/{event-id} in address bar.

> Expected: Page loads, showing event details without exact address.

### Step 3: Observe Traffic

**Context**: Verify API call in proxy.

Check Burp HTTP history for the GET /events/{event-id}.

> Expected: Request logged, response ready for inspection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[unauthorized-access]]
- [[event-view]]
