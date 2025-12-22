---
id: de298a69-33f9-4eea-8255-fff7758a5867
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:32.270838+00:00'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Credential Access|TA0006 - Credential Access]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Forge Web Credentials|T1606 - Forge Web Credentials]]'
  - '[[techniques/XSL Script Processing|T1220 - XSL Script Processing]]'
sub_techniques: []
tags:
  - '[[tags/Authentication Bypass]]'
  - '[[tags/Extensible Stylesheet Language Transformation]]'
  - '[[tags/SAML Injection]]'
commands:
  - '[[commands/xsltproc-apply-stylesheet]]'
  - '[[commands/curl-send-modified-saml-response]]'
platforms:
  - Web
tools:
  - '[[tools/Burp-Suite]]'
skill_level: advanced
impact_level: high
detection_risk: high
validated: true
---

# SAML-Injection-Authentication-Bypass

## Summary

SAML Injection Authentication Bypass exploits vulnerabilities in SAML-enabled applications by injecting malicious XML code, specifically an XSLT stylesheet, into the SAML response. This allows the stylesheet to be processed by the application during parsing, enabling arbitrary code execution, data exfiltration, or authentication bypass to gain unauthorized access to protected resources.

## Description

This procedure targets applications using SAML for single sign-on (SSO) where the SAML response is not properly sanitized for XML external entities or XSLT processing. Attackers intercept the SAML response (typically a base64-encoded XML assertion sent via POST to the Assertion Consumer Service or ACS endpoint) and modify it to embed a malicious XSLT stylesheet within the XML digital signature's <ds:Transforms> element. When the application processes the response, it applies the XSLT, which can read local files (e.g., /etc/passwd), encode them, and exfiltrate data to an attacker-controlled server. This bypasses authentication by forging valid-looking credentials or executing post-auth actions. The target environment is typically a web application on a Linux server acting as the identity provider (IdP) or service provider (SP). Success grants attacker access equivalent to an authenticated user, potentially leading to data theft or lateral movement. Prerequisites include network access to the login flow and ability to intercept HTTPS traffic.

## Requirements

1. Network access to the SAML-enabled application's authentication endpoint (e.g., via browser or proxy).
2. A proxy tool like [[tools/Burp-Suite]] configured to intercept and modify HTTP/HTTPS traffic.
3. A legitimate SAML response captured from a test authentication attempt (requires user credentials or public access to initiate SSO).
4. Attacker-controlled server to receive exfiltrated data (e.g., a web server at http://attacker.com).
5. Basic knowledge of SAML XML structure and XSLT syntax.

## Defense

- Implement strict XML parsing with disabling external entity processing and XSLT execution in the SAML library (e.g., use secure parsers like those in Spring Security or Shibboleth with XXE protection).
- Monitor SAML responses for anomalies such as unexpected <xsl:stylesheet> elements or network outbound connections from the application server to unknown domains.
- Enforce multi-factor authentication (MFA) on SAML flows to add layers beyond the bypassed credential check.
- Use Web Application Firewalls (WAFs) tuned to detect XML injections and block suspicious XSLT patterns.
- Regularly audit SAML configurations for processing of signatures and transforms.

## Objectives

1. Intercept and modify a SAML response to inject a malicious XSLT stylesheet.
2. Cause the application to process the XSLT, leading to data exfiltration or authentication bypass.
3. Gain unauthorized access to the application's resources as an authenticated user.

## Instructions

### Step 1: Test Malicious XSLT Stylesheet Locally

**Context**: Before injection, validate the XSLT payload works by applying it to a sample SAML XML file on your local machine. This step confirms the stylesheet can read and exfiltrate file contents without errors. Use [[commands/xsltproc-apply-stylesheet]] to transform a test SAML document.

**Command** ([[commands/xsltproc-apply-stylesheet]]):
```bash
xsltproc $_STYLESHEET $_INPUT_XML -o $_OUTPUT_XML
```

> This applies the malicious XSLT to a sample SAML XML, simulating the target's processing. Replace $_STYLESHEET with the path to your XSLT file containing the payload from [[codes/SAML-XSLT-Exfiltration-Payload]], $_INPUT_XML with a base SAML response, and $_OUTPUT_XML with the desired output file. Expected output is a transformed XML that includes exfiltrated data (e.g., contents of /etc/passwd encoded and appended).

### Step 2: Intercept Legitimate SAML Response

**Context**: Initiate an authentication flow to capture a valid SAML response. Configure [[tools/Burp-Suite]] as a proxy in your browser, then navigate to the application's login page and trigger SAML SSO (e.g., via IdP like Okta or Azure AD). Intercept the POST request to the ACS endpoint containing the SAMLResponse parameter.

**Instructions**: In Burp, set breakpoints on the ACS URL (typically /login or /saml/acs). Submit the login form and drop the request when the SAML POST is sent. Decode the base64 SAMLResponse to view the XML.

**Expected Output**: A base64-encoded SAML XML assertion in the POST body, including <samlp:Response> with assertions and optional <ds:Signature>.

### Step 3: Modify SAML Response with Malicious XSLT

**Context**: Edit the intercepted SAML XML to inject the malicious XSLT into the <ds:Transforms> section of the signature. This exploits T1220 by embedding the stylesheet where the parser expects transforms. Reference [[codes/SAML-XSLT-Exfiltration-Payload]] for the exact snippet to insert.

**Instructions**: In Burp Repeater, paste the decoded SAML XML into the SAMLResponse field. Locate the <ds:Signature> element and insert the payload within <ds:Transforms><ds:Transform>. Update the attackerUrl variable in the XSLT to your controlled domain. Re-encode the modified XML as base64.

**Expected Output**: Modified base64 SAMLResponse that, when processed, triggers XSLT execution to read /etc/passwd and send to http://attacker.com.

### Step 4: Replay Modified SAML Response

**Context**: Forward the tampered response to the ACS endpoint to bypass authentication. This step verifies the injection succeeds, allowing access or triggering exfiltration.

**Command** ([[commands/curl-send-modified-saml-response]]):
```bash
curl -X POST -k $_ACS_URL -H "Content-Type: application/x-www-form-urlencoded" -d "SAMLResponse=$_MODIFIED_BASE64_RESPONSE&RelayState=$_RELAY_STATE"
```

> This sends the modified SAML response to the application's ACS. Use -k to ignore SSL if self-signed certs are in play. $_ACS_URL is the POST endpoint (e.g., https://target.com/saml/acs), $_MODIFIED_BASE64_RESPONSE is the base64 of the tampered XML, and $_RELAY_STATE is the original relay state if present. Expected output is a 302 redirect to the protected resource or a successful login page, indicating bypass.

**Success Indicators**:
- Application processes the response without XML parsing errors.
- Attacker server receives exfiltrated data (e.g., GET request with encoded /etc/passwd contents).
- Access granted to post-auth pages without valid credentials.
