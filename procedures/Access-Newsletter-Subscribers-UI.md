---
tags:
  - ui-interaction
  - api-trigger
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:30:47.237Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: e6e892fe-ed52-4833-947d-7e686621dff9
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Access-Newsletter-Subscribers-UI

## Summary

Interact with the LinkedIn newsletter UI to trigger the vulnerable API endpoint for viewing subscribers, enabling request capture.

## Description

Navigate to the created newsletter and click the 'Subscribers' button, which sends a GET request to the vulnerable endpoint. This step is crucial for observing the legitimate request format before modification. Target environment is LinkedIn's web platform; outcomes include API request details for replay.

## Requirements

1. Existing newsletter
2. Proxy tool like Burp Suite configured
3. Authenticated session

## Defense

Defensive measures and detection strategies:

- Log UI interactions with API calls
- Validate user ownership in frontend

## Objectives

1. Trigger legitimate API request
2. Capture request for analysis
3. Identify vulnerable parameters

## Instructions

### Step 1: Open Newsletter Page

**Context**: Load the newsletter dashboard.

Use browser to navigate to your newsletter URL.

> Expected: Dashboard with 'Subscribers' option visible.

### Step 2: Click Subscribers Button

**Context**: Initiate API call.

Click 'Subscribers' to send GET request.

> Intercepted in Burp: Request to /voyager/api/voyagerPublishingDashSeriesSubscribers.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ui-interaction]]
- [[api-trigger]]
