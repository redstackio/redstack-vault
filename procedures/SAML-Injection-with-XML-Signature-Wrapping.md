---
id: 27751b2c-a45f-4aa6-9f7e-c3f3e22e0618
name: SAML-Injection-with-XML-Signature-Wrapping
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.167694+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Privilege Escalation|TA0004 - Privilege Escalation]]'
techniques:
  - '[[techniques/Access Token Manipulation|T1134 - Access Token Manipulation]]'
  - '[[techniques/Forge Web Credentials|T1606 - Forge Web Credentials]]'
sub_techniques:
  - '[[sub-techniques/Parent PID Spoofing|T1134.004 - Parent PID Spoofing]]'
tags:
  - '[[tags/Authentication Bypass]]'
  - '[[tags/SAML Injection]]'
  - '[[tags/XML Signature Wrapping Attacks]]'
commands:
  - '[[commands/curl-post-modified-saml-response]]'
tools:
  - '[[tools/Burp-Suite]]'
platforms:
  - Web
validated: true
---

# SAML-Injection-with-XML-Signature-Wrapping

## Summary

This procedure demonstrates how to perform a SAML Injection attack combined with XML Signature Wrapping (XSW) to bypass authentication in SAML-based single sign-on (SSO) systems. By manipulating the SAML response XML to include an unauthorized assertion alongside a legitimate one, an attacker can trick the service provider (SP) into authenticating the attacker's identity while the signature validates against the legitimate portion.

## Description

SAML (Security Assertion Markup Language) is used for SSO in web applications, where an identity provider (IdP) sends an XML response to the SP containing authentication assertions. XML Signature Wrapping exploits flaws in XML parsers or SAML implementations that validate signatures but fail to check for extraneous elements. The attacker intercepts the legitimate SAML response, injects a new assertion (e.g., for their own user), and ensures the signature covers only the legitimate part, allowing the injected assertion to be processed. This technique is effective against vulnerable SAML libraries like older versions of OpenSAML or custom implementations. It requires man-in-the-middle access to the SAML exchange, typically via a proxy, and targets web applications in enterprise or cloud environments.

## Requirements

1. Network access to intercept SAML traffic between IdP and SP (e.g., via proxy or compromised network).
2. Tools: [[tools/Burp-Suite]] or similar proxy for intercepting and modifying HTTP requests.
3. Knowledge of the target's SAML flow, including assertion IDs and user attributes.
4. Base64 encoding/decoding capability (built into most tools).
5. Valid session or ability to trigger a SAML authentication flow.

## Defense

- Implement strict XML validation: Parse and validate the entire SAML response, checking for multiple assertions and ensuring the signature covers all processed elements.
- Use canonicalization and exclusive XML signatures to prevent wrapping attacks.
- Monitor for anomalous SAML responses, such as multiple assertions or unexpected user attributes.
- Regularly update SAML libraries (e.g., to latest OpenSAML) and enable logging for signature validation failures.

## Objectives

1. Bypass SAML authentication to impersonate a legitimate user.
2. Gain unauthorized access to the protected web application.
3. Escalate privileges if the injected assertion includes higher-level attributes.

## Instructions

### Step 1: Intercept the Legitimate SAML Response

**Context**: Trigger a SAML authentication flow from a legitimate user session to capture the base64-encoded SAMLResponse. This provides the structure needed for wrapping.

Use [[tools/Burp-Suite]] to intercept the POST request to the SP's assertion consumer service (ACS) endpoint (typically /saml/acs).

**Expected Output**: HTTP POST request with SAMLResponse parameter containing base64-encoded XML.

### Step 2: Decode and Modify the SAML XML

**Context**: Decode the SAMLResponse, inject an additional assertion for the attacker, and wrap it so the signature validates on the legitimate assertion while the parser processes the injected one. Use the example payload from [[codes/SAML-XML-Signature-Wrapping-Payload]] as a template, replacing placeholders with target-specific values.

1. Decode the base64 SAMLResponse using a tool like base64 -d.
2. Insert the injected <FA> element before the legitimate <LA> assertion, ensuring the signature reference points only to <LA>.
3. Re-encode the modified XML to base64.

**Code** ([[codes/SAML-XML-Signature-Wrapping-Payload]]):

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

> This XML injects an 'evil' assertion (FA) for the attacker while preserving the legitimate assertion (LA). The signature on LA validates, but the SP may process FA if validation is incomplete.

**Expected Output**: Modified base64-encoded SAMLResponse ready for replay.

### Step 3: Replay the Modified SAML Response

**Context**: Forward the tampered SAMLResponse to the SP to complete authentication as the injected user.

Execute [[commands/curl-post-modified-saml-response]] to send the POST request, replacing placeholders with the target's ACS URL and modified SAMLResponse.

**Command** ([[commands/curl-post-modified-saml-response]]):
```bash
curl -X POST -d "SAMLResponse=$_MODIFIED_SAML_BASE64&RelayState=$_RELAY_STATE" $_ACS_URL
```

> This replays the wrapped SAML response. If successful, the SP authenticates the attacker.

**Expected Output**: HTTP 302 redirect to the protected resource or session cookie indicating successful login.

### Step 4: Verify Access

**Context**: Confirm the bypass by accessing protected endpoints as the impersonated user.

Navigate to the application's dashboard or API endpoints to check user context (e.g., via browser dev tools or curl HEAD).

**Expected Output**: Access granted with attacker attributes from the injected assertion.

### Step 5: Clean Up

**Context**: Avoid detection by clearing proxy history and monitoring for alerts.

If decision point: If multi-factor is enabled post-SAML, this may fail—abort and pivot to another vector.

**Success Indicators**:
- Authentication succeeds without valid credentials.
- User profile shows injected attributes (e.g., Attacker subject).
