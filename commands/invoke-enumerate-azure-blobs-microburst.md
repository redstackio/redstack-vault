---
id: 9dd803e9-7865-470b-901f-6fe4abd16210
type: command
executor: powershell
data: Invoke-EnumerateAzureBlobs -Base $_SHORT_DOMAIN -OutputFile $_OUTPUT_FILE
output: >-
  PS > Invoke-EnumerateAzureBlobs -Base <SHORT DOMAIN> -OutputFile
  azureblobs.txt


  Found Storage Account -  testsecure.blob.core.windows.net

  Found Storage Account -  securetest.blob.core.windows.net

  Found Storage Account -  securedata.blob.core.windows.net

  Found Storage Account -  securefiles.blob.core.windows.net
created_at: '2023-05-24T22:11:13.024040+00:00'
updated_at: '2023-05-24T22:11:13.198951+00:00'
platforms:
  - Cloud
tags:
  - azure
  - microburst
  - blob-enumeration
verified: true
validated: true
---

# invoke-enumerate-azure-blobs-microburst

## Command

```powershell
Invoke-EnumerateAzureBlobs -Base $_SHORT_DOMAIN -OutputFile $_OUTPUT_FILE
```

## Description

This command uses the Microburst toolkit to enumerate Azure storage accounts and their blobs by querying endpoints based on a base domain, saving results to a file for analysis.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Base | Short domain or tenant identifier for brute-forcing storage account names (e.g., contoso) | Yes |
| -OutputFile | Path to the output file for saving discovered blobs and accounts | Yes |

## Examples

### Basic Usage

```powershell
Invoke-EnumerateAzureBlobs -Base contoso -OutputFile azureblobs.txt
```

### Advanced Usage

Run after loading the script and configuring Azure credentials.

## Expected Output

```
PS > Invoke-EnumerateAzureBlobs -Base <SHORT DOMAIN> -OutputFile azureblobs.txt

Found Storage Account -  testsecure.blob.core.windows.net
Found Storage Account -  securetest.blob.core.windows.net
Found Storage Account -  securedata.blob.core.windows.net
Found Storage Account -  securefiles.blob.core.windows.net
```
Lists discovered storage accounts; detailed blob info is appended to the output file.

## Related

- [[procedures/Azure-Storage-Blob-Enumeration]]
- [[tools/Microburst]]
