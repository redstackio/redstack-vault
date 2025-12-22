---
type: code
language: bash
verified: true
created_at: '2023-05-24T22:34:09.705389+00:00'
updated_at: '2024-01-01T00:00:00Z'
platforms:
  - Cloud
tags:
  - azure
  - storage
  - sas
validated: true
---

# Azure-CLI-Generate-Azure-Blob-SAS-Full

## Code

```bash
az login
token=$(az storage container generate-sas --name mycontainer --account-name mystorageaccount --permissions rwdl --expiry 2023-12-31T23:59Z --https-only --output tsv)
$url = "https://mystorageaccount.blob.core.windows.net/mycontainer?$token"
```

## Description

This script uses Azure CLI to log in, generate a SAS token for a Blob container with rwdl permissions expiring on a specified date, and construct the full URL. Note: The variable assignment uses shell syntax, but the final $url line mixes PowerShell-style; adapt for pure bash by using url=... . It provides a cross-platform alternative to PowerShell for SAS creation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| mycontainer | Blob container name | uploads |
| mystorageaccount | Storage account name | sa-storage |
| rwdl | Permissions string | rw (read/write only) |
| 2023-12-31T23:59Z | Expiry in ISO 8601 format | 2024-01-02T12:00Z |

## Usage

Execute in a bash terminal (or PowerShell with az extension). Substitute parameters and run to output $url. Test with curl $url to list blobs. Useful in Linux-based attack infrastructures for cloud pivoting.

## Detection

- Azure CLI usage in sign-in logs or command-line audit events
- Frequent SAS generations from non-approved IPs in storage logs
- HTTPS-only enforcement bypassed attempts in network proxies
- Shell process spawning az commands in endpoint detection tools

## Related

- [[procedures/Generate-Azure-Blob-Storage-SAS-URLs]]
- [[tools/Azure-CLI]]
