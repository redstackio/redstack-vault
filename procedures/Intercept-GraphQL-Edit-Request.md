---
id: 56b982ec-d1c9-4ebf-be80-00be8297bc72
name: Intercept GraphQL Edit Request
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:47.721Z'
updated_at: '2025-12-11T03:47:47.721Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - intercept
  - proxy
  - graphql
commands: []
platforms:
  - Web
tools:
  - '[[tools/Burp-Proxy]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
validated: true
mitre_tactics:
  - '[[TA0007]]'
mitre_techniques:
  - '[[T1087]]'
---

# Intercept GraphQL Edit Request

## Summary

This procedure intercepts the GraphQL request for editing certifications using a proxy tool to enable parameter modification.

## Description

Initiate an edit on a certification and use [[tools/Burp-Proxy]] to capture the CreateOrUpdateHackerCertification query. This allows inspection and alteration of parameters like ID for IDOR testing. Targets web applications with GraphQL endpoints.

## Requirements

1. Configured [[tools/Burp-Proxy]] with browser integration.
2. Authenticated HackerOne session.
3. Existing certification to edit.

## Defense

Defensive measures and detection strategies:

- Use HTTPS and certificate pinning to hinder interception.
- Detect proxy usage via request anomalies or headers.

## Objectives

1. Capture editable GraphQL query.
2. Prepare for ID modification.
3. Identify lack of authorization checks.

## Instructions

### Step 1: Configure Burp Proxy

**Context**: Set up proxy for traffic interception.

Configure your browser to route traffic through [[tools/Burp-Proxy]] at 127.0.0.1:8080.

> Install Burp CA certificate if needed.

### Step 2: Initiate Edit and Intercept

**Context**: Trigger the request.

Edit a certification in the profile and intercept the outgoing GraphQL request in Burp.

> Look for the CreateOrUpdateHackerCertification query in the request body.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Proxy]]

## Tags

- intercept
- proxy
- graphql
