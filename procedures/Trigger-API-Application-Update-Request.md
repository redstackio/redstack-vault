---
id: proc-pressable-trigger-update
tags:
  - api
  - update
  - pressable
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
updated_at: '2025-12-14T17:33:24.399Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger API Application Update Request

## Summary

This procedure initiates a POST request to update the API application in Pressable, allowing interception of the full request payload including the application ID and authenticity token.

## Description

By clicking the update button on the application details page, a POST to /api/applications is sent. With a proxy in place, this request can be captured for modification. This step builds on the view interception and targets the Ruby on Rails endpoint.

## Requirements

1. Proxy actively intercepting traffic
2. Access to the application details page
3. Valid authenticity_token from session

## Defense

Defensive measures and detection strategies:

- Validate all update requests with proper authorization checks
- Rate limit POST requests to API endpoints

## Objectives

1. Generate interceptable POST request
2. Capture application[id] parameter
3. Include authenticity_token for bypassing CSRF

## Instructions

### Step 1: Submit Update Action

**Context**: Trigger the update to send the POST request.

No specific command; perform via web interface with proxy:

- On the application details page, click 'Update'
- Proxy intercepts the POST to /api/applications

> Request body includes application[id]=your_id&authenticity_token=token&other_params. Do not forward yet.

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

- [[api]]
- [[update]]
- [[pressable]]
