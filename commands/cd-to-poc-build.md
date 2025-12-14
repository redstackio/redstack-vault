---
id: cmd-uuid-2
data: 'cd c:\CVE-2019-0604\ConsoleApplication1\ConsoleApplication1\bin\Debug\'
tags:
  - navigation
  - windows
type: command
output: null
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.027Z'
verified: false
validated: true
submitted: true
---
# cd-to-poc-build

## Command

```cmd
cd c:\CVE-2019-0604\ConsoleApplication1\ConsoleApplication1\bin\Debug\
```

## Description

Changes the current directory in Windows Command Prompt to the build output path of the PoC encoder executable.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| path | Full path to Debug folder | Yes |

## Examples

### Basic Usage

```cmd
cd c:\CVE-2019-0604\ConsoleApplication1\ConsoleApplication1\bin\Debug\
```

## Expected Output

C:\CVE-2019-0604\ConsoleApplication1\ConsoleApplication1\bin\Debug> (prompt updates to new directory).

## Related

- [[procedures/Generate-Encoded-XAML-Payload]]
