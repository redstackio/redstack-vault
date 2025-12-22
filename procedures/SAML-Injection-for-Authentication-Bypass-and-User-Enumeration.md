---
type: procedure
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
techniques:
  - '[[techniques/Valid Accounts|T1078 - Valid Accounts]]'
sub_techniques:
  - '[[techniques/Valid Accounts/.004| T1078.004 - Cloud Accounts]]'
tags:
  - '[[tags/Authentication Bypass]]'
  - '[[tags/SAML Injection]]'
  - '[[tags/XML Comment Handling]]'
commands:
  - '[[commands/base64-decode-saml]]'
  - '[[commands/base64-encode-saml]]'
  - '[[commands/curl-post-modified-saml]]'
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

# SAML-Injection-for-Authentication-Bypass-and-User-Enumeration

## Summary

This procedure outlines how to perform SAML injection by manipulating XML elements in SAML responses to bypass authentication controls and impersonate users, as well as enumerate valid usernames by observing application responses to injected payloads. It exploits improper XML parsing, such as mishandling of comments, to alter the effective NameID attribute without breaking the overall XML structure.

## Description

SAML (Security Assertion Markup Language) is an XML-based standard for exchanging authentication and authorization data between an identity provider (IdP) and a service provider (SP). SAML injection vulnerabilities arise when the SP fails to properly validate or sanitize SAML responses, allowing attackers to inject malicious XML content. A common vector is intercepting the base64-encoded SAMLResponse during the authentication flow (e.g., via a proxy) and modifying elements like the <NameID> to impersonate a different user or test for valid accounts. For example, inserting an XML comment within the NameID text can alter the concatenated value if the parser ignores comments but joins adjacent text nodes, potentially bypassing domain checks or enabling enumeration through differential error responses (e.g., "user not found" vs. successful login). This technique is particularly effective against web applications using SAML for single sign-on (SSO), such as those integrated with Okta, Azure AD, or custom IdPs. The target environment typically involves a browser-based login flow where the attacker has network proximity or can use a proxy like Burp Suite. Expected outcomes include unauthorized access to the SP as the targeted user or confirmation of valid usernames for further attacks like phishing or brute-forcing.

## Requirements

1. Network access to the target's SAML-enabled login endpoint (e.g., ability to intercept traffic via MITM or proxy).
2. A proxy tool like [[tools/Burp-Suite]] configured to intercept HTTPS traffic (requires valid CA certificate installed in the browser).
3. Knowledge of the target's SAML flow, including the ACS URL and any expected Issuer.
4. Basic XML editing skills and a text editor (e.g., vim or VS Code).
5. Optional: A controlled domain (e.g., evil.com) for testing modified NameIDs.

## Defense

- Implement strict SAML response validation, including signature verification using the IdP's public key and checking the ACS URL.
- Sanitize and parse XML inputs using secure libraries that handle comments and entities properly (e.g., avoid custom parsers).
- Monitor authentication logs for anomalies like unexpected NameID values, multiple failed SSO attempts from the same IP, or unsigned responses.
- Enforce least privilege on SSO endpoints and use short-lived assertions with audience restrictions.

## Objectives

1. Bypass SAML authentication by altering the NameID to impersonate a legitimate user.
2. Enumerate valid usernames by injecting test values and analyzing response differences (e.g., success vs. error codes).
3. Gain unauthorized access to protected resources on the service provider.

## Instructions

### Step 1: Intercept and Decode the SAML Response

**Context**: Begin the authentication flow to capture a legitimate SAMLResponse, then decode it for modification. This step requires proxying the traffic to access the base64-encoded SAML assertion sent from the IdP to the SP.

Configure [[tools/Burp-Suite]] as a proxy in your browser and navigate to the target's login page. Initiate a login attempt with any credentials to trigger the SAML response. Intercept the POST request to the ACS endpoint (typically containing the SAMLResponse parameter).

**Command** ([[commands/base64-decode-saml]]):
```bash
echo "$_SAML_RESPONSE" | base64 -d > saml.xml
```

> This decodes the base64 SAMLResponse into an editable XML file. Replace $_SAML_RESPONSE with the captured value from the proxy. Expected output: A valid XML file starting with <samlp:Response> or similar, viewable with cat saml.xml.

### Step 2: Modify the SAML XML for Injection

**Context**: Edit the decoded XML to inject a comment within the <NameID> element. This exploits XML comment handling flaws where the parser ignores the comment but concatenates text nodes, potentially altering the effective username (e.g., appending a domain to bypass validation). Use the provided code snippet for the injection pattern.

Open saml.xml in a text editor and locate the <NameID> element within the <Subject>. Insert an XML comment to modify the value, for example, changing "victim@target.com" to "victim@target.com<!--INJECTED-->@evil.com" so the concatenated text becomes "victim@target.com@evil.com" (assuming the parser joins nodes post-comment ignore). Save the file.

Reference the injection payload: [[codes/SAML-NameID-Comment-Injection-Example]]

> This step's purpose is to test if the SP accepts the modified NameID as valid, enabling bypass if domain checks are weak. If enumeration is the goal, iterate with guessed usernames (e.g., admin@target.com) and note response behaviors.

### Step 3: Re-encode and Replay the Modified SAML Response

**Context**: Encode the tampered XML back to base64 and replay it to the SP to complete the authentication. This verifies the injection success by attempting to log in as the modified/impersonated user.

**Command** ([[commands/base64-encode-saml]]):
```bash
base64 saml.xml > encoded_saml.txt
```

> Encodes the modified XML. Expected output: A base64 string in encoded_saml.txt, which you copy as the new SAMLResponse value.

Then, in your proxy, modify the intercepted POST request's SAMLResponse parameter with the new base64 value and forward it.

**Command** ([[commands/curl-post-modified-saml]]):
```bash
curl -X POST "$_ACS_URL" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "SAMLResponse=$(cat encoded_saml.txt)"
```

> Replays the modified response directly if proxy replay isn't used. Replace $_ACS_URL with the SP's assertion consumer service URL (e.g., https://target.com/saml/acs). Expected output: A 302 redirect to the protected resource or a successful login page, indicating bypass success. For enumeration, vary the NameID and check for differences like HTTP 200 vs. 403.

### Step 4: Validate and Enumerate

**Context**: Confirm access and enumerate users by repeating the injection with a list of potential usernames. Success is indicated by dashboard access or personalized content; failures may reveal valid users via timing or error leaks.

Replay with variations (e.g., test@target.com, admin@target.com). Log responses for patterns.

> If the injection allows impersonation, you've bypassed auth. For enumeration, compile a list of usernames that trigger non-generic errors.
