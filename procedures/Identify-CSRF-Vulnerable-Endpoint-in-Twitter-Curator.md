---
tags:
  - csrf
  - recon
  - twitter
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:27:35.878Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 10c8c312-b96a-460e-ba1e-6de40e257d2c
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Identify-CSRF-Vulnerable-Endpoint-in-Twitter-Curator

## Summary

This procedure involves reconnaissance to identify the Twitter curator API endpoint vulnerable to CSRF by inspecting network requests and testing for missing token validation, enabling subsequent exploit development.

## Description

In the context of Twitter's collections feature, attackers perform manual testing using browser tools to capture legitimate POST requests for adding tweets. The endpoint https://curator.twitter.com/api/collections/STREAM/content is targeted, as it processes parameters like tweet_ids[], collections[], and model[id] without requiring a CSRF token. This lack of protection allows forged requests from external sites. Prerequisites include access to a Twitter account with curator permissions and basic web debugging skills. Expected outcome is confirmation of vulnerability for crafting exploits.

## Requirements

1. Twitter account with access to collections feature
2. Browser with developer tools (e.g., Chrome DevTools)
3. Knowledge of victim's collection ID (publicly discoverable)

## Defense

Defensive measures and detection strategies:

- Implement CSRF tokens on all state-changing endpoints
- Monitor for anomalous additions to collections via logging
- Educate users on phishing risks and link verification

## Objectives

1. Locate and document the vulnerable API endpoint
2. Verify absence of CSRF protections
3. Gather parameters for exploit replication

## Instructions

### Step 1: Inspect Legitimate Request

**Context**: Log into Twitter, navigate to the curator, and attempt to add a tweet to a collection to capture the network request.

Open browser developer tools (Network tab), perform the action, and examine the POST request to https://curator.twitter.com/api/collections/STREAM/content. Note parameters: tweet_ids[] (array of tweet IDs), collections[] (collection ID), model[id] ('STREAM').

**Expected Output**: Request details showing no CSRF token in headers or body.

### Step 2: Test for CSRF Vulnerability

**Context**: Simulate an external request to confirm exploitability.

Use a simple HTML form from a local file or external host to POST the same parameters without authentication. If the request succeeds when loaded by an authenticated user, the vulnerability is confirmed.

**Expected Output**: Successful addition without token, indicating CSRF risk.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[csrf]]
- [[recon]]
- [[twitter]]
