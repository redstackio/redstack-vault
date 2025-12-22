---
id: cmd-002
data: >-
  type
  d:\\TrustHX\\STBKSERM101\\www_app\\concurrent_test\\new_application_concurrent_test__svc.cs
tags:
  - collection
  - file-read
type: command
output: >-
  Source code content starting with using System; ... class
  new_application_concurrent_test : IHXPageXmlService { ... }, wrapped in HTML
  textarea
executor: cmd
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:22.935Z'
verified: false
validated: true
submitted: true
---
# type-source-code-disclosure

## Command

```cmd
type d:\\TrustHX\\STBKSERM101\\www_app\\concurrent_test\\new_application_concurrent_test__svc.cs
```

## Description

This Windows command displays the contents of a text file, used via webshell to exfiltrate C# source code from the server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| d:\\TrustHX\\STBKSERM101\\www_app\\concurrent_test\\new_application_concurrent_test__svc.cs | Full path to target file | Yes |

## Examples

### Basic Usage

```cmd
type d:\\path\\to\\file.cs
```

### Advanced Usage

For multiple files: for %f in (*.cs) do type %f

## Expected Output

Full file contents, e.g., C# class definitions, in HTML textarea via webshell.

## Related

- [[commands/dir-directory-listing]]
