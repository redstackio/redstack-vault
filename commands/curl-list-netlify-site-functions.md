---
id: cmd-002
data: >-
  curl -X GET
  https://api.netlify.com/api/v1/sites/5a05c659-aa54-4184-bdbe-7faa4dd497b5/functions
  -H "Authorization: Bearer ████" -s | jq
tags:
  - api
  - functions
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:52.726Z'
verified: false
validated: true
submitted: true
---
# curl-list-netlify-site-functions

## Command

```bash
curl -X GET https://api.netlify.com/api/v1/sites/5a05c659-aa54-4184-bdbe-7faa4dd497b5/functions -H "Authorization: Bearer ████" -s | jq
```

## Description

This command lists deployed functions for a specific Netlify site, helping assess deployment capabilities and RCE potential via AWS Lambda.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP GET method | Yes |
| `-H "Authorization: Bearer ████"` | Adds Bearer token for authentication | Yes |
| `-s` | Silent mode | No |
| `| jq` | Formats JSON output | No |
| `https://api.netlify.com/api/v1/sites/5a05c659-aa54-4184-bdbe-7faa4dd497b5/functions` | Endpoint for site functions (site ID specific) | Yes |

## Examples

### Basic Usage

```bash
curl -X GET https://api.netlify.com/api/v1/sites/your-site-id/functions -H "Authorization: Bearer token" -s | jq
```

### Advanced Usage

```bash
curl -X GET https://api.netlify.com/api/v1/sites/5a05c659-aa54-4184-bdbe-7faa4dd497b5/functions -H "Authorization: Bearer ████" -s | jq '.[] | {name, runtime}'
```

## Expected Output

JSON array of functions: {"name": "ping-details", "provider": "aws_lambda", "runtime": "nodejs18.x", "region": "us-east-2"}.

## Related

- [[Related Procedure: Explore-Account-Access-and-RCE-Potential]]
