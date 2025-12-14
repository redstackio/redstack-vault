---
tags:
  - idor
  - graphql
  - recon
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Account Discovery]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 8086c94a-2e57-4a29-ab8a-a934c156e86c
created_at: '2025-12-14T17:25:33.491Z'
updated_at: '2025-12-14T17:25:33.491Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Login-and-Capture-GraphQL-Visibility-Request

## Summary

This procedure authenticates a user to HackerOne and captures the GraphQL POST request sent when updating personal team visibility settings, revealing the structure for IDOR exploitation.

## Description

In the context of HackerOne's web application, team members can change their profile's team visibility (Revealed/Concealed) via settings. This triggers a GraphQL mutation to /graphql. By intercepting this with a proxy, attackers can inspect the base64-encoded team_member_id parameter, which is directly referenceable. Prerequisites include a valid HackerOne account with team access and Burp Suite configured as a proxy.

## Requirements

1. Authenticated HackerOne session
2. Burp Suite proxy intercept enabled (browser traffic routed through 127.0.0.1:8080)
3. Access to https://hackerone.com/settings/teams

## Defense

Defensive measures and detection strategies:

- Implement proper authorization checks in GraphQL resolvers to validate team_member_id ownership
- Monitor GraphQL logs for anomalous mutation patterns (e.g., non-self ID updates)
- Use rate limiting on visibility mutations

## Objectives

1. Capture the exact request payload for replication
2. Identify the team_member_id encoding
3. Establish baseline for request modification

## Instructions

### Step 1: Authenticate and Navigate to Settings

**Context**: Log in and access the team visibility section to prepare for request capture.

Navigate to https://hackerone.com/settings/teams and select the Visibility section.

### Step 2: Trigger and Intercept Request

**Context**: Change visibility to generate the GraphQL mutation and capture it.

Click on 'Concealed' or 'Revealed' to toggle the setting. With Burp Suite intercepting, capture the POST to /graphql.

The request includes:

```json
{
  "query": "mutation Update_team_member_visibility_mutation(...)",
  "variables": {
    "input_0": {
      "team_member_id": "Z2lkOi8vaGFja2Vyb25lL1RlYW1NZW1iZXIvNDM3OTQ=",
      "concealed": true,
      "clientMutationId": "..."
    }
  }
}
```

> This captures the mutation; inspect for the base64 team_member_id.

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

- [[idor]]
- [[graphql]]
- [[recon]]
