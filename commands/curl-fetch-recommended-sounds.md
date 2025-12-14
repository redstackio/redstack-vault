---
id: cmd-curl-fetch-recommended
data: >-
  curl -i -s -k -X 'POST' -H 'Host: gateway-production.dubsmash.com' -H 'X-Dmac:
  a252a66f19e030696d2b70ae2cff527b32e9add33475af6ab192595017f6b4ea' -H
  'X-Remote-Config-Values: []' -H 'X-Time: 1613160805' -H 'User-Agent:
  Dopesmash/5.20.0 (com.mobilemotion.dubsmash; build:45431; iOS 14.0.1)
  Alamofire/5.4.0' -H 'X-Accept-Content-Language: en_IN' -H 'X-Device-Timezone:
  19800' -H 'X-Device-Language: en' -H 'X-Device-Country: IN' -H
  'X-Build-Number: 45431' -H 'Content-Length: 1065' -H 'X-App-Version: 5.20.0'
  -H 'X-Platform: ios' -H 'Connection: close' -H 'Authorization: Bearer
  xxxxxxxxx' -H 'X-Dubsmash-Device-Id: 0675382B-668E-4EB7-8313-ED96BC132DC9' -H
  'Accept-Language: en-IN;q=1.0, hi-IN;q=0.9' -H 'Accept: application/json' -H
  'Content-Type: application/json' -H 'X-Dmac-Version: 2' -H 'If-None-Match:
  W/\"7d-SQTt6RA1iQk+sK3Hcqc774a67/I\"' -b
  '__cfduid=d42d0391d8f2c2d8bf5107a6ceda7c2f61610738889' --data-binary
  '{"variables":{"next":null},"query":"query RecommendedRichSounds($next:
  String) {\n recommendations(next: $next, type: SOUND) {\n __typename\n next\n
  results {\n __typename\n recommendation_identifier\n score\n updated_at\n
  object {\n __typename\n ... on Sound {\n ...RichSoundFragment\n }\n }\n }\n
  }\n}\nfragment RichSoundFragment on Sound {\n __typename\n uuid\n created_at\n
  sound\n name\n waveform_raw_data\n liked\n soundStatus: status\n creator {\n
  __typename\n ...ContentCreatorFragment\n }\n share_link\n num_likes\n
  num_videos\n top_videos {\n __typename\n ...TopVideoFragment\n }\n}\nfragment
  ContentCreatorFragment on User {\n __typename\n username\n uuid\n
  date_joined\n followed\n has_invite_badge\n badges\n
  profile_picture\n}\nfragment TopVideoFragment on Video {\n __typename\n uuid\n
  video_data {\n __typename\n mobile {\n __typename\n thumbnail\n }\n }\n
  creator {\n __typename\n uuid\n username\n }\n}"}'
  'https://gateway-production.dubsmash.com/graphql?build_number=45431&platform=ios'
tags:
  - graphql
  - recon
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.282Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-recommended-sounds

## Command

```bash
curl -i -s -k -X 'POST' -H 'Host: gateway-production.dubsmash.com' -H 'X-Dmac: a252a66f19e030696d2b70ae2cff527b32e9add33475af6ab192595017f6b4ea' -H 'X-Remote-Config-Values: []' -H 'X-Time: 1613160805' -H 'User-Agent: Dopesmash/5.20.0 (com.mobilemotion.dubsmash; build:45431; iOS 14.0.1) Alamofire/5.4.0' -H 'X-Accept-Content-Language: en_IN' -H 'X-Device-Timezone: 19800' -H 'X-Device-Language: en' -H 'X-Device-Country: IN' -H 'X-Build-Number: 45431' -H 'Content-Length: 1065' -H 'X-App-Version: 5.20.0' -H 'X-Platform: ios' -H 'Connection: close' -H 'Authorization: Bearer xxxxxxxxx' -H 'X-Dubsmash-Device-Id: 0675382B-668E-4EB7-8313-ED96BC132DC9' -H 'Accept-Language: en-IN;q=1.0, hi-IN;q=0.9' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'X-Dmac-Version: 2' -H 'If-None-Match: W/\"7d-SQTt6RA1iQk+sK3Hcqc774a67/I\"' -b '__cfduid=d42d0391d8f2c2d8bf5107a6ceda7c2f61610738889' --data-binary '{"variables":{"next":null},"query":"query RecommendedRichSounds($next: String) {\n recommendations(next: $next, type: SOUND) {\n __typename\n next\n results {\n __typename\n recommendation_identifier\n score\n updated_at\n object {\n __typename\n ... on Sound {\n ...RichSoundFragment\n }\n }\n }\n }\n}\nfragment RichSoundFragment on Sound {\n __typename\n uuid\n created_at\n sound\n name\n waveform_raw_data\n liked\n soundStatus: status\n creator {\n __typename\n ...ContentCreatorFragment\n }\n share_link\n num_likes\n num_videos\n top_videos {\n __typename\n ...TopVideoFragment\n }\n}\nfragment ContentCreatorFragment on User {\n __typename\n username\n uuid\n date_joined\n followed\n has_invite_badge\n badges\n profile_picture\n}\nfragment TopVideoFragment on Video {\n __typename\n uuid\n video_data {\n __typename\n mobile {\n __typename\n thumbnail\n }\n }\n creator {\n __typename\n uuid\n username\n }\n}"}' 'https://gateway-production.dubsmash.com/graphql?build_number=45431&platform=ios'
```

## Description

This command sends a GraphQL POST request to fetch recommended rich sounds from Dubsmash's API, mimicking an iOS client to retrieve public sound details including UUIDs for reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H 'Authorization: Bearer xxxxxxxxx'` | Bearer token for authentication (replace xxxxxxxxx) | Yes |
| `--data-binary` | GraphQL query JSON with variables.next=null | Yes |
| `build_number=45431&platform=ios` | Query params mimicking app version | Yes |

## Examples

### Basic Usage

```bash
# As above, with your token
```

### Advanced Usage

```bash
# Pipe to jq for UUID extraction
curl ... | jq '.data.recommendations.results[].object.uuid'
```

## Expected Output

HTTP 200 response with JSON: {"data":{"recommendations":{"results":[{"object":{"uuid":"a687eb61ad814a09a8a85cedef7837f3","name":"original","creator":{"username":"victim"}}}]}}}

## Related

- [[commands/curl-update-sound-title]]
- [[procedures/Fetch-Public-Sound-UUIDs-via-RecommendedRichSounds]]
