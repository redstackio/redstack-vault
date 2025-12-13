---
tags:
  - xxe
  - ssrf
  - saml
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
commands:
  - '[[commands/curl-post-saml-xxe]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 2c7f5c5c-4d28-470e-be8d-8225cf3aa03f
created_at: '2025-12-13T09:01:26.347Z'
updated_at: '2025-12-13T09:01:26.347Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send Malicious SAMLResponse to SSO Endpoint

## Summary

This procedure sends a crafted malicious SAMLResponse via HTTP POST to the vulnerable SSO endpoint, exploiting the XXE vulnerability to cause the server to perform SSRF by fetching an external resource.

## Description

Targeting the /sso endpoint of a web application using SAML, this procedure involves sending a POST request with a base64-encoded XML payload containing an XXE entity. Upon parsing, the server resolves the entity, leading to SSRF. Expected outcomes include confirmation of exploitation via traffic to the attacker's server and potential internal data disclosure.

## Requirements

1. Crafted base64-encoded XXE payload
2. Network access to the target endpoint
3. Tool for sending HTTP requests (e.g., curl)

## Defense

Defensive measures and detection strategies:

- Validate and sanitize SAML inputs
- Monitor server logs for XML parsing errors or unusual outbound traffic

## Objectives

1. Deliver the payload to trigger XXE
2. Induce SSRF for internal access
3. Verify impact through callback

## Instructions

### Step 1: Prepare the Request

**Context**: Set up the HTTP POST request with appropriate headers and body.

Ensure headers include Host and Content-Type.

> This mimics a legitimate SAML authentication request.

### Step 2: Execute the Request

**Context**: Send the request to exploit the vulnerability.

Execute [[commands/curl-post-saml-xxe]] to send the payload:

```bash
curl -X POST 'https://rev-app.informatica.com/sso' \
  -H 'Host: rev-app.informatica.com' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  --data 'SAMLResponse=<base64-encoded-XML>&RelayState='
```

> The server will parse the XML and fetch the external entity.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-post-saml-xxe]]

## Tools Used

- [[tools/curl]]

## Tags

- [[xxe]]
- [[ssrf]]
- [[saml]]
