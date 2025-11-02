---
id: ab82b5cd-9eb5-4bb5-a803-94dd712198a4
name: MSBuild Build Package from XML
type: command
executor: bash
data: C:\windows\Microsoft.net\Framework\$_VERSION\MSBuild.exe $_FILENAME.xml
output: 'PS C:\Windows\Tasks> C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe
  msbuild_nps.xml

  Microsoft (R) Build Engine version 4.7.2053.0

  [Microsoft .NET Framework, version 4.0.30319.42000]

  Copyright (C) Microsoft Corporation. All rights reserved.


  Build started 14/11/2019 22:22:37.'
created_at: '2019-11-14T23:38:41.534280+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[MSBuild]]'
- '[[ps]]'
---

# MSBuild Build Package from XML

```bash
C:\windows\Microsoft.net\Framework\$_VERSION\MSBuild.exe $_FILENAME.xml
```

## Expected Output

```
PS C:\Windows\Tasks> C:\Windows\Microsoft.NET\Framework\v4.0.30319\MSBuild.exe msbuild_nps.xml
Microsoft (R) Build Engine version 4.7.2053.0
[Microsoft .NET Framework, version 4.0.30319.42000]
Copyright (C) Microsoft Corporation. All rights reserved.

Build started 14/11/2019 22:22:37.
```


