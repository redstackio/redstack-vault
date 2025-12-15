---
id: p4d5e6f7-g8h9-0123-defg-4567890123
tags:
  - dos
  - graphql
  - browser-crash
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Impact]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:56.789Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques:
  - '[[OS Exhaustion Flood]]'
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Observe-DoS-Effects-on-Pages

## Summary

This procedure loads pages that query user profile data via GraphQL to demonstrate the DoS impact from oversized filenames, observing delays, timeouts, and crashes caused by massive JSON responses.

## Description

After the payload is in place, GraphQL endpoints fetching profile information (e.g., for reports or programs) include the full 3MB filename in responses. This leads to client-side resource exhaustion, affecting pages like user profiles, report lists, program directories, and thank-you pages. Burp Suite can be used to inspect the bloated responses.

## Requirements

1. Access to the affected report or profile pages
2. Burp Suite for optional response inspection
3. Modern browser to test crash conditions

## Defense

Defensive measures and detection strategies:

- Paginate or truncate large fields in API responses
- Implement client-side size checks for JSON parsing
- Monitor for anomalous response times and log oversized queries
- Use CDN or caching to mitigate repeated large fetches

## Objectives

1. Trigger GraphQL queries including the oversized data
2. Measure and verify DoS symptoms
3. Confirm impact across multiple page types

## Instructions

### Step 1: Load Affected Pages

**Context**: Access endpoints that fetch participant or profile data.

Navigate to the report participants page (https://hackerone.com/reports/<report-id>/participants/), user profile, program page, or thank-you page involving the affected account.

### Step 2: Intercept and Inspect Responses

**Context**: Use Burp to capture GraphQL traffic and analyze size.

With Burp proxy enabled, reload the pages. In the Repeater or Inspector, examine the GraphQL POST responses for the inclusion of the 3MB filename in the JSON payload.

**Expected Output**: Pages hang or timeout; responses exceed several MB in size, causing browser instability.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques

- [[OS Exhaustion Flood]] OS Exhaustion Floods

## Commands Used

- None

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- dos
- graphql-query
- response-bloat
