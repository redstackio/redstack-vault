---
tags:
  - graphql
  - traffic-capture
  - information-disclosure
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/ruby-redact-pii]]'
platforms:
  - Web
techniques:
  - '[[Data from Information Repositories]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 76bbfdb0-1c6d-4649-8a29-45bf837e8938
created_at: '2025-12-11T06:10:15.675Z'
updated_at: '2025-12-11T06:10:15.675Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1213]]'
---
# Capture GraphQL Traffic for Email Disclosure

## Summary

This procedure captures GraphQL request traffic during collaborator editing on HackerOne to disclose private emails from the SaveCollaboratorsMutation payload.

## Description

By intercepting the POST request to /graphql, attackers can view email details in the payload without the invitation being accepted. This exploits poor access controls in the mutation.

## Requirements

1. Pending invitation in a report.
2. Traffic interception tool like [[tools/Burp-Suite]].
3. Ability to edit collaborators.

## Defense

Defensive measures and detection strategies:

- Redact sensitive data in API payloads.
- Implement strict access controls on GraphQL operations.

## Objectives

1. Intercept and inspect GraphQL requests.
2. Extract leaked email addresses.
3. Achieve information disclosure goal.

## Instructions

### Step 1: Set Up Traffic Proxy

**Context**: Configure a proxy to capture requests.

Launch [[tools/Burp-Suite]] and set your browser to proxy through it.

> Ensure all traffic to hackerone.com is intercepted.

### Step 2: Trigger and Capture Request

**Context**: Edit collaborators to generate the request.

Click the pen icon for collaborators, then capture the /graphql POST with SaveCollaboratorsMutation.

> Inspect the payload for email fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Data from Information Repositories]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[graphql]]
- [[traffic-capture]]
- [[information-disclosure]]
