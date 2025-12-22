---
type: procedure
description: >-
  Manipulate SAML responses using XXE injection to impersonate users and bypass
  authentication.
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.249118+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Command and Control|TA0011]]'
  - '[[tactics/Defense Evasion|TA0005]]'
  - '[[tactics/Lateral Movement|TA0008]]'
techniques:
  - '[[techniques/Encrypted Channel|T1573]]'
  - '[[techniques/Use Alternate Authentication Material|T1550]]'
sub_techniques:
  - '[[sub-techniques/Web Session Cookie|T1550.004]]'
tags:
  - '[[tags/Authentication Bypass]]'
  - '[[tags/SAML Injection]]'
  - '[[tags/XML External Entity]]'
commands:
  - '[[commands/curl-post-saml-response]]'
tools:
  - '[[tools/Burp-Suite]]'
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
validated: true
---

# SAML-Injection-for-Authentication-Bypass

## Summary

SAML Injection is a technique to bypass authentication by manipulating SAML responses, often exploiting XML External Entity (XXE) vulnerabilities to alter assertions and impersonate legitimate users. This procedure outlines intercepting, modifying, and replaying a SAML response to gain unauthorized access to a service provider application.

## Description

SAML (Security Assertion Markup Language) is used for single sign-on (SSO) between identity providers (IdP) and service providers (SP). An attacker with the ability to intercept or influence the SAML response can inject malicious XML content, leveraging XXE to read sensitive files or embed arbitrary data into the assertion. This allows forging authentication claims, such as user identity or attributes, to bypass login mechanisms. The attack targets web applications relying on SAML 2.0 for authentication, typically in enterprise environments. Success grants the attacker a valid session as the impersonated user, potentially leading to data access or privilege escalation. This procedure assumes the application lacks proper XML parsing security (e.g., no entity resolution disabled) and signature validation.

## Requirements

1. Network access to the target application and IdP traffic (e.g., man-in-the-middle position or proxy setup).
2. Knowledge of SAML protocol structure, including response elements like assertions, attributes, and signatures.
3. Tools for intercepting and modifying HTTP requests/responses, such as a proxy (e.g., [[tools/Burp-Suite]]).
4. Ability to craft or modify XML payloads, potentially requiring a text editor or XML-aware tool.
5. Valid session or initial access to trigger a legitimate SAML flow for interception.

## Defense

- Implement strict XML parsing by disabling external entity resolution in the SAML library (e.g., use secure parsers like libxml2 with XXE protections).
- Enforce SAML response signature verification using public keys from trusted IdPs to detect tampering.
- Validate all SAML attributes and assertions against expected schemas, rejecting unsigned or malformed responses.
- Use HTTP-only, secure cookies and short session timeouts to limit replay attack windows.
- Regularly audit SAML configurations and monitor for anomalous authentication patterns, such as logins from unexpected IPs.

## Objectives

1. Intercept a legitimate SAML response during the authentication flow.
2. Inject malicious XML entities to manipulate user attributes or assertions.
3. Replay the modified response to achieve unauthorized authentication as a target user.
4. Gain access to protected resources on the service provider.

## Instructions

### Step 1: Intercept Legitimate SAML Response

**Context**: Establish a proxy to capture the SAML response sent from the IdP to the SP during a normal login attempt. This provides the base structure for modification.

Use [[tools/Burp-Suite]] to configure your browser proxy and trigger a login to the target application.

**Expected Output**: A captured HTTP POST request containing the SAMLResponse parameter in Base64-encoded XML.

### Step 2: Decode and Modify SAML Response

**Context**: Decode the SAMLResponse, then inject XXE entities into the XML to alter attributes (e.g., user ID or roles). Reference the example payload in [[codes/SAML-Response-XXE-Injection-Example]] to define entities that can exfiltrate data or forge values.

1. Decode the Base64 SAMLResponse using a tool like base64decode.org or command-line.
2. Edit the XML: Insert DOCTYPE with entities (e.g., <!ENTITY xxe SYSTEM "file:///etc/passwd">) and reference them in an attribute value (e.g., &xxe;).
3. Re-encode the modified XML to Base64.
4. Ensure the modification targets authentication-relevant elements like <saml:AttributeStatement> or <saml:Subject>.

**Expected Output**: Modified Base64-encoded SAMLResponse that, when parsed, includes injected data or forged assertions.

### Step 3: Replay Modified Response

**Context**: Send the tampered SAMLResponse to the SP's assertion consumer service (ACS) endpoint to complete the authentication flow as the impersonated user.

**Command** ([[commands/curl-post-saml-response]]):
```bash
curl -X POST $_ACS_URL \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "SAMLResponse=$ENCODED_SAML&RelayState=$RELAY_STATE"
```

> This command submits the modified SAML response. Replace placeholders with captured values from Step 1. If successful, the SP will process the assertion and issue a session cookie.

**Expected Output**: HTTP 302 redirect to the protected application dashboard, along with a Set-Cookie header for the session.
