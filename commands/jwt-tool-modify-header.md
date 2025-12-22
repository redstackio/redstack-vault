---
type: command
executor: bash
data: python3 jwt_tool.py $_JWT_TOKEN -I -hc $_HEADER_CLAIM -hv $_HEADER_VALUE
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - jwt
  - manipulation
verified: true
validated: true
---

# jwt-tool-modify-header

## Command

```bash
python3 jwt_tool.py $_JWT_TOKEN -I -hc $_HEADER_CLAIM -hv $_HEADER_VALUE
```

## Description

This command uses the jwt_tool.py script to modify specific claims in the header of a JWT token. It is useful for testing algorithm confusion attacks by changing the 'alg' field or adding custom headers to exploit validation weaknesses.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_JWT_TOKEN | The base64-encoded JWT string to modify | Yes |
| -I | Inspect and modify mode | Yes |
| -hc $_HEADER_CLAIM | Header claim to change (e.g., alg, typ) | Yes |
| -hv $_HEADER_VALUE | New value for the header claim (e.g., HS256) | Yes |

## Examples

### Basic Usage

Change the algorithm to HS256:

```bash
python3 jwt_tool.py eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9... -I -hc alg -hv HS256
```

### Advanced Usage

Modify multiple headers:

```bash
python3 jwt_tool.py $_JWT_TOKEN -I -hc alg -hv HS256 -hc kid -hv malicious
```

## Expected Output

The modified JWT token as a string, e.g.:

eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyIn0.signature

No errors if successful; use the output token for testing.

## Related

- [[procedures/JWT-Header-Manipulation-for-Algorithm-Confusion]]
- [[tools/jwt-tool]]
