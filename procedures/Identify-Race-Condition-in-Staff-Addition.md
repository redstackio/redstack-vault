---
id: p-shopify-identify-race
tags:
  - race-condition
  - identification
  - shopify
  - web
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:24:18.917Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify Race Condition in Staff Addition

## Summary

This procedure involves analyzing Shopify's staff member addition process to identify a race condition vulnerability that allows concurrent requests to bypass quota limits on subscription plans.

## Description

In Shopify's team management features, adding staff members involves an API call that checks the plan's quota before creation. However, the lack of synchronization (e.g., no database locks or atomic operations) enables multiple requests to pass the check simultaneously before the count updates. This procedure details inspecting the process using browser tools to confirm the flaw, targeting the staff addition endpoint in authenticated merchant sessions. Expected outcomes include mapping the request flow and verifying sequential additions respect limits, setting up for exploitation.

## Requirements

1. Authenticated access to a Shopify admin dashboard with team management permissions
2. Browser with developer tools (e.g., Chrome DevTools) for network inspection
3. Basic understanding of HTTP requests and API interactions

## Defense

Defensive measures and detection strategies:

- Implement database-level locking (e.g., row-level locks) during quota checks and creations
- Use atomic transactions to ensure check-and-act operations are indivisible
- Monitor for unusual spikes in concurrent staff addition requests via API logs

## Objectives

1. Confirm the absence of synchronization in the staff addition workflow
2. Document the exact endpoint and parameters for quota bypass potential
3. Validate that the vulnerability enables exceeding plan limits

## Instructions

### Step 1: Access Team Management

**Context**: Log in and navigate to the staff addition interface to observe normal behavior.

Open the Shopify admin dashboard, go to Settings > Users and permissions, and attempt to add a single staff member with a test email. Note the UI feedback on quota limits.

### Step 2: Inspect Network Requests

**Context**: Use developer tools to trace the addition process and identify check points.

In browser DevTools, open the Network tab, add a staff member, and filter for POST requests to endpoints like /admin/team_members.json. Examine request payloads (e.g., email, role) and responses for quota checks. Repeat sequentially to confirm limits are enforced after each addition.

### Step 3: Test for Concurrency

**Context**: Probe for race potential by simulating rapid additions.

Manually attempt quick successive additions or use a simple script to send requests with minimal delay. Observe if any exceed the quota before enforcement, confirming the race window.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- race-condition
- shopify
- reconnaissance
