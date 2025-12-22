---
tags:
  - interception
  - burp-suite
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
id: 9957bc26-c538-4d74-98aa-44247ed4b8ac
created_at: '2025-12-13T09:01:26.370Z'
updated_at: '2025-12-13T09:01:26.370Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept GraphQL Request with Burp Suite

## Summary

This procedure uses Burp Suite to intercept and review HTTP traffic from the Trint application to identify the GraphQL request for Zendesk token.

## Description

After registration, interacting with the app generates requests that can be captured. Burp Suite's proxy history reveals the POST to graphql2.trint.com, which is crucial for replicating the token query.

## Requirements

1. Burp Suite installed and configured as proxy
2. Registered Trint account
3. Browser configured to use Burp proxy

## Defense

Defensive measures and detection strategies:

- Rate limit API requests
- Monitor for anomalous GraphQL queries

## Objectives

1. Capture relevant HTTP requests
2. Identify GraphQL endpoint
3. Extract request structure

## Instructions

### Step 1: Configure Proxy

**Context**: Set up Burp to intercept traffic.

Launch Burp Suite and configure your browser to proxy through 127.0.0.1:8080.

> This captures all requests from the app.

### Step 2: Review History

**Context**: Browse app and check captured requests.

Interact with app.trint.com, then in Burp, filter history for POST to graphql2.trint.com.

> Locate the GraphQL query request.

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

- [[interception]]
- [[tools/Burp-Suite]]
