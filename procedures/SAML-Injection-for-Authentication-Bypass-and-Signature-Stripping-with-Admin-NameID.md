---
type: procedure
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
sub_techniques: []
tags:
  - authentication-bypass
  - saml-injection
  - signature-stripping
commands:
  - '[[commands/sed-modify-saml-response-for-injection]]'
tools:
  - '[[tools/Burp-Suite]]'
platforms:
  - Web
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# SAML-Injection-for-Authentication-Bypass-and-Signature-Stripping-with-Admin-NameID

## Summary

This procedure demonstrates how to perform SAML injection by intercepting and modifying a SAML authentication response to change the NameID to an administrative user and strip the digital signature, allowing an attacker to bypass authentication and gain elevated privileges on a web application relying on SAML for single sign-on (SSO).

## Description

SAML (Security Assertion Markup Language) is an XML-based standard for exchanging authentication and authorization data between an identity provider (IdP) and a service provider (SP). In this attack, the attacker exploits improper validation in the SAML implementation by intercepting the SAML response during the authentication flow, modifying the XML to set the NameID element to a known admin username, and removing the Signature element to evade signature verification checks. This enables the attacker to impersonate an admin user without valid credentials. The technique targets web applications with vulnerable SAML configurations, such as those not enforcing signature validation or allowing unsigned assertions. Success grants unauthorized access to admin functions, potentially leading to data exfiltration, configuration changes, or further lateral movement. This procedure assumes the attacker has network access to intercept traffic, such as via a man-in-the-middle position or compromised endpoint.

## Requirements

1. Network access to intercept SAML authentication traffic (e.g., via proxy or MITM setup).
2. Knowledge of the target application's SAML flow and a valid admin username (e.g., obtained via reconnaissance).
3. Tools for traffic interception and XML manipulation, such as Burp Suite and sed or xmlstarlet.
4. A SAML response XML file or live interception capability.

## Defense

- Enforce strict signature validation on all SAML assertions and reject unsigned or tampered responses.
- Implement XML schema validation and canonicalization checks to prevent injection attacks.
- Use certificate pinning for IdP signatures and monitor for anomalous authentication events, such as unexpected admin logins.
- Apply web application firewalls (WAFs) to detect XML modifications in SAML payloads.

## Objectives

1. Intercept and modify the SAML response to impersonate an admin user via NameID injection.
2. Strip the signature to bypass verification and achieve authentication bypass.
3. Gain unauthorized admin access to the target application for further exploitation.

## Instructions

### Step 1: Intercept the SAML Authentication Response

**Context**: Position yourself to capture the SAML response sent from the IdP to the SP during login. This requires acting as a proxy between the victim/user and the application.

Use Burp Suite to intercept the HTTP POST request containing the SAMLResponse parameter.

> Set up Burp Suite as a proxy and configure the browser to route traffic through it. Trigger a login attempt to capture the response. The SAMLResponse is typically base64-encoded XML in the POST body to the assertion consumer service (ACS) endpoint.

**Expected Output**: A captured request with the SAMLResponse parameter visible in the Repeater or Proxy history.

### Step 2: Decode and Modify the SAML XML

**Context**: Decode the base64 SAMLResponse, edit the XML to change the NameID to 'admin' (or known admin value), and remove the entire <Signature> element to strip verification. This step exploits lax validation to forge admin credentials.

**Command** ([[commands/sed-modify-saml-response-for-injection]]):
```bash
sed -i 's|<NameID>.*</NameID>|<NameID>admin</NameID>|g; /<ds:Signature>/,/</ds:Signature>/d' saml_response.xml
echo "$(base64 -w 0 saml_response.xml)" > modified_samlresponse
```

> This command uses sed to replace the NameID content with 'admin' and delete the signature block (assuming ds namespace for signatures). Save the original decoded XML as 'saml_response.xml', run the command, then re-encode to base64 for replay. If the XML structure varies, adjust the sed patterns accordingly. Verify the modification with xmllint --format saml_response.xml.

**Expected Output**: Modified XML file with NameID set to 'admin' and no <Signature> element; base64-encoded output ready for injection.

### Step 3: Replay the Modified Response

**Context**: Forward the tampered SAMLResponse back to the SP to complete authentication as the admin user. This bypasses the IdP entirely if validation is weak.

Paste the modified base64 SAMLResponse into the POST body using Burp Repeater and submit to the ACS URL.

> Ensure session cookies from the initial request are preserved. If the application uses additional checks, you may need to adjust other attributes like SessionIndex.

**Expected Output**: Successful authentication redirect to the application dashboard, logged in as the admin user.

### Step 4: Verify Admin Access

**Context**: Confirm elevated privileges by accessing admin-only features, such as user management or sensitive data views.

Navigate to protected admin endpoints and check for access grants.

> Look for indicators like admin dashboard elements or API responses confirming role='admin'.

**Expected Output**: Access to admin functions without credential prompts.
