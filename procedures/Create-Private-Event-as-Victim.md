---
tags:
  - event-creation
  - privacy-settings
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:27.152Z'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: 609f0fd6-1a79-45ea-8b81-78b77b5fd705
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Private-Event-as-Victim

## Summary

This procedure details creating an event on FetLife with privacy settings enabled to hide the exact address, setting up the conditions for testing information disclosure in the API.

## Description

As the victim account, users create events via the web interface, specifying a venue with coordinates. Privacy options allow hiding details from non-RSVP users, but the API still exposes coordinates. This step simulates a real user protecting location privacy, highlighting the vulnerability when bypassed.

## Requirements

1. Logged-in victim account with event creation permissions
2. Specific venue address for testing (e.g., one with known coordinates)
3. Browser access to FetLife events section

## Defense

Defensive measures and detection strategies:

- Enforce privacy settings at the API level, filtering sensitive fields based on user permissions
- Log event creation and access attempts for anomaly detection
- Use geofencing or approximate location display instead of exact coords

## Objectives

1. Generate an event ID for subsequent access testing
2. Apply privacy controls to obscure address from unauthorized viewers
3. Verify settings hide details on the frontend while testing backend leakage

## Instructions

### Step 1: Log In and Navigate to Events

**Context**: Access the event creation interface.

Log in as victim, go to https://fetlife.com/events/new.

> Expected: Event creation form loads.

### Step 2: Fill Event Details

**Context**: Input event info including exact address.

Enter title, date, description, and venue address (e.g., a location in Darwin, Australia at -12.496252, 131.04425).

> Save draft. Expected: Address parsed to coordinates internally.

### Step 3: Set Privacy and Save

**Context**: Enable hiding of location from non-RSVP users.

In privacy settings, check 'Address & Name of Location', click 'Update Event Privacy'.

> Publish event. Expected: URL with {event-id}, page shows hidden address.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[event-creation]]
- [[privacy-settings]]
