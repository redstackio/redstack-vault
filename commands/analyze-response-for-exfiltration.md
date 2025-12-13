---
data: >-
  curl -X POST -H "Content-Type: application/xml" --data "[xxe payload]"
  https://target/endpoint | grep "sensitive"
tags:
  - xxe
  - analysis
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: f60882a5-a6d0-40b5-a889-b3fe3f966be9
created_at: '2025-12-13T09:00:27.316Z'
updated_at: '2025-12-13T09:00:27.316Z'
verified: false
validated: true
submitted: true
---
# Analyze Response for Exfiltration

## Command

```bash
curl -X POST -H "Content-Type: application/xml" --data "[xxe payload]" https://target/endpoint | grep "sensitive"
```

## Description

This command captures the response from an XXE exploit and filters for signs of exfiltrated sensitive data.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `curl [options]` | Sends the request | Yes |
| `| grep "sensitive"` | Filters output | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Content-Type: application/xml" --data "[xxe payload]" https://subdomain.informatica.com/endpoint | grep "root:"
```

### Advanced Usage

```bash
curl -X POST -H "Content-Type: application/xml" --data "[xxe payload]" https://subdomain.informatica.com/endpoint > response.txt && grep "confidential" response.txt
```

## Expected Output

Lines from the response matching the grep pattern, indicating leaked data.

## Related
- [[procedures/Verify-Data-Exfiltration]]
- [[procedures/Craft-and-Send-XXE-Payload]]
