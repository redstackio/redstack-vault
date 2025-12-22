---
type: code
language: xml
verified: true
tags:
  - saml
  - injection
  - xml
platforms:
  - Web
validated: true
---

# SAML-NameID-Comment-Injection-Example

## Code

```xml
<SAMLResponse>
    <Issuer>https://idp.com/</Issuer>
    <Assertion ID="_id1234">
        <Subject>
            <NameID>user@user.com<!--XMLCOMMENT-->.evil.com</NameID>
        </Subject>
    </Assertion>
</SAMLResponse>
```

## Description

This XML snippet demonstrates a SAML assertion injection using an XML comment within the <NameID> element. The comment (<!--XMLCOMMENT-->) is ignored by parsers, but the adjacent text nodes concatenate to form "user@user.com.evil.com", potentially bypassing domain validation or enabling impersonation if the SP mishandles comment parsing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| user@user.com | Original/target username email | admin@target.com |
| XMLCOMMENT | Placeholder for injected comment content | INJECTED-PAYLOAD |
| .evil.com | Attacker-controlled domain suffix | .attacker.net |

## Usage

Insert this pattern into a decoded SAML response during an intercepted SSO flow. Modify the NameID for impersonation (e.g., set to a privileged user) or enumeration (test multiple values). Re-encode and replay to the SP. Used in procedures like [[procedures/SAML-Injection-for-Authentication-Bypass-and-User-Enumeration]] for auth bypass via proxy interception.

## Detection

- Log unsigned or tampered SAML responses with anomalous NameID formats (e.g., unexpected domains or comment remnants).
- Enable XML parsing logs to detect concatenated text nodes or injection attempts.
- Monitor for rapid SSO attempts with varying NameIDs from the same source IP.

## Related

- [[procedures/SAML-Injection-for-Authentication-Bypass-and-User-Enumeration]]
- [[tools/Burp Suite]]
