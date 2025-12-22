---
id: c23552a2-635c-4037-8041-da5b593eff98
type: command
executor: powershell
data: . $_SCRIPT_PATH
output: null
created_at: '2023-05-24T22:11:13.022732+00:00'
updated_at: '2023-05-24T22:11:13.198951+00:00'
platforms:
  - Cloud
tags:
  - azure
  - microburst
  - script-load
verified: true
validated: true
---

# load-microburst-enumerate-azure-blobs-script

## Command

```powershell
. $_SCRIPT_PATH
```

## Description

This command loads the Invoke-EnumerateAzureBlobs PowerShell script from the Microburst toolkit into the current session, enabling blob enumeration functions for Azure storage discovery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SCRIPT_PATH | Full path to the InvokeEnumerateAzureBlobs.ps1 script file | Yes |

## Examples

### Basic Usage

```powershell
. C:\Tools\MicroBurst\Misc\InvokeEnumerateAzureBlobs.ps1
```

### Advanced Usage

If the script is in a different location, adjust the path accordingly.

## Expected Output

No output if successful; the function Invoke-EnumerateAzureBlobs becomes available in the session. Errors indicate path issues or permission problems.

## Related

- [[procedures/Azure-Storage-Blob-Enumeration]]
- [[tools/Microburst]]
