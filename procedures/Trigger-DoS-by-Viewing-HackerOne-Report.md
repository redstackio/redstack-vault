---
id: proc-hackerone-trigger-view-dos
tags:
  - dos
  - web
  - hackerone
  - uncontrolled-resource-consumption
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:30.794Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Trigger-DoS-by-Viewing-HackerOne-Report

## Summary

This procedure triggers the denial of service by attempting to view a spam-filled HackerOne report, causing the AJAX controller to load all comments without limits, resulting in server overload and 524 timeout errors.

## Description

Targeting the report view functionality, this step exploits the absence of pagination or chunking in comment loading. The AJAX endpoint fetches every comment (manual/system-generated) at once, leading to resource exhaustion. Applicable to both sandboxed and non-sandboxed teams, with impacts including blocked access for users and amplified requests via high-entropy data. Scenario assumes prior spamming; outcomes are timeouts after 60 seconds and increased server load.

## Requirements

1. A HackerOne report overloaded with comments from previous procedures.
2. Web browser with network inspection tools (e.g., dev console).
3. Access to view the report (any authenticated user).

## Defense

Defensive measures and detection strategies:

- Add pagination or lazy loading to comment fetches.
- Implement timeouts and resource quotas on AJAX requests; monitor for large comment loads.

## Objectives

1. Force server to process unlimited comments, causing DoS.
2. Prevent legitimate access to report content.
3. Amplify impact with incompressible data.

## Instructions

### Step 1: Navigate to Report View

**Context**: Initiate the load of the bloated report.

Open the report URL (e.g., https://hackerone.com/reports/137508) in a browser. The view functionality automatically triggers comment loading.

### Step 2: Monitor AJAX Request

**Context**: Observe the overload in action.

Use browser dev tools (Network tab) to watch the AJAX call to load comments (e.g., GET /reports/{id}/comments). The request will hang, leading to timeout.

**Expected Output**: 524 Origin Time-Out error after 60 seconds; report content inaccessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Endpoint Denial of Service]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[dos]]
- [[web]]
- [[hackerone]]
- [[uncontrolled-resource-consumption]]
