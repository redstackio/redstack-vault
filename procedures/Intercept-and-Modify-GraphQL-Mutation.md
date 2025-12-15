---
id: p5q6r7s8-t9u0-1234-fghi-jk5678901234
tags:
  - interception
  - modification
  - graphql
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:53.508Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-and-Modify-GraphQL-Mutation

## Summary

This core procedure intercepts the UpdateInvitationPreferencesMutation GraphQL request triggered by the UI slider, modifies the min_bounty variable to an arbitrary high value (e.g., 7000), and replays it to bypass server-side validation absence.

## Description

The vulnerability stems from client-side only enforcement of the min_bounty limit based on average payouts. Using Burp, the JSON payload in the POST to /graphql is edited. Target: HackerOne web app. Outcome: Preferences updated beyond UI constraints, affecting invitation eligibility.

## Requirements

1. Burp Suite proxy active
2. Bounty slider visible and interacted with
3. Knowledge of JSON structure

## Defense

Defensive measures and detection strategies:

- Implement server-side validation against user averages
- Rate-limit GraphQL mutations
- Log and anomaly-detect payload changes

## Objectives

1. Capture the mutation request
2. Tamper with min_bounty
3. Achieve successful update

## Instructions

### Step 1: Trigger and Intercept Request

**Context**: Generate the GraphQL mutation via UI.

Adjust the min bounty slider to a low value; enable interception in Burp > Proxy > Intercept.

> Request to https://hackerone.com/graphql intercepted, containing UpdateInvitationPreferencesMutation with variables like min_bounty.

### Step 2: Modify Payload

**Context**: Edit to bypass limit.

In Burp Repeater or Intercept tab, change "min_bounty": 1000 to "min_bounty": 7000 in the JSON variables.

> Payload updated; ensure syntax valid.

### Step 3: Forward Request

**Context**: Submit the tampered mutation.

Click Forward or Send in Repeater.

> Server returns 200 OK with {"data":{"updateInvitationPreferences":{"wasSuccessful":true}}}.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- tampering
- mutation
