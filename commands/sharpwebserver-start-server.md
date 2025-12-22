---
id: fc74e7d5-e92c-4772-a307-7269a6d41be7
type: command
executor: cmd
data: SharpWebServer.exe port=%PORT% dir=%DIRECTORY% verbose=true
output: null
created_at: '2023-04-06T03:56:02.931186+00:00'
updated_at: '2023-04-10T20:25:52.370784+00:00'
platforms:
  - Windows
tags:
  - webdav
  - hosting
  - printnightmare
verified: true
validated: true
---

# sharpwebserver-start-server

## Command

```cmd
SharpWebServer.exe port=%PORT% dir=%DIRECTORY% verbose=true
```

## Description

Starts SharpWebServer, a .NET tool for hosting files over HTTP/WebDAV, commonly used in PrintNightmare attacks to serve malicious DLLs via UNC paths.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| port=%PORT% | Listening port (e.g., 8888) | Yes |
| dir=%DIRECTORY% | Directory to serve files from (e.g., c:\\users\\public) | Yes |
| verbose=true | Enable verbose logging | No |

## Examples

### Basic Usage

```cmd
SharpWebServer.exe port=8888 dir=c:\\users\\public verbose=true
```

### Advanced Usage

```cmd
SharpWebServer.exe port=8080 dir=c:\\temp\\payloads
```

## Expected Output

Server listening on http://0.0.0.0:8888
Serving files from: c:\users\public
[Verbose logs on requests]

## Related

- [[procedures/PrintNightmare-WebDAV-Attack]]
- [[tools/SharpWebServer]]
