---
id: cmd-get-customerprofile-guid
data: >-
  curl -k -H "Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz" -H
  "Device-Token: 337658ef1bf61f5c"
  https://crmproxy.protel.com.tr/api/v1/customerprofile/ae533ce1-0613-e611-80bf-00155d5b2b02
tags:
  - profile-access
  - sensitive-data
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.521Z'
verified: false
validated: true
submitted: true
---
# get-customerprofile-guid

## Command

```bash
curl -k -H "Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz" -H "Device-Token: 337658ef1bf61f5c" https://crmproxy.protel.com.tr/api/v1/customerprofile/ae533ce1-0613-e611-80bf-00155d5b2b02
```

## Description

This command fetches detailed customer profile data by GUID, including transactions and masked credit cards, using the static token for unauthorized access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Ignore SSL errors | Yes |
| `-H "Authorization: ..."` | Static auth token | Yes |
| `-H "Device-Token: ..."` | Optional device identifier | No |
| `/customerprofile/{guid}` | Path with specific customer GUID | Yes |

## Examples

### Basic Usage

```bash
curl -k -H "Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz" https://crmproxy.protel.com.tr/api/v1/customerprofile/ae533ce1-0613-e611-80bf-00155d5b2b02
```

### Advanced Usage

```bash
curl -k -H "Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz" -H "User-Agent: Mozilla/5.0" https://crmproxy.protel.com.tr/api/v1/customerprofile/ae533ce1-0613-e611-80bf-00155d5b2b02
```

## Expected Output

JSON profile data or HTTP 409 "No such contact exists" if GUID invalid.

## Related

- [[commands/get-customerprofiles]]
- [[procedures/Access-API-Documentation-and-Sensitive-Endpoints]]
