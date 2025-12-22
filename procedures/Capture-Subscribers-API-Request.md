---
tags:
  - request-capture
  - interception
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
updated_at: '2025-12-14T17:30:47.235Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: e0941613-ca75-4832-9a39-b33c36e1d0ff
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Capture-Subscribers-API-Request

## Summary

Intercept the HTTP GET request triggered by the subscribers UI to analyze the vulnerable API endpoint structure.

## Description

Using a proxy tool, capture the request sent to /voyager/api/voyagerPublishingDashSeriesSubscribers. This reveals parameters like seriesUrn, which is key to the IDOR. Scenario involves legitimate access; outcome is full request details for modification.

## Requirements

1. Burp Suite or similar proxy
2. Traffic routed through proxy
3. Newsletter access

## Defense

Defensive measures and detection strategies:

- Monitor for proxy-intercepted traffic
- Encrypt API communications

## Objectives

1. Extract request parameters
2. Identify seriesUrn format
3. Prepare for tampering

## Instructions

### Step 1: Configure Proxy

**Context**: Set up interception.

In Burp, configure browser proxy to 127.0.0.1:8080.

> Expected: All traffic proxied.

### Step 2: Trigger and Capture

**Context**: Perform UI action to capture.

Click 'Subscribers'; intercept in Burp Repeater.

> Request: GET with seriesUrn=urn%3Ali%3Afsd_contentSeries%3A<yourId>, headers including CSRF tokens.

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

- [[request-capture]]
- [[interception]]
