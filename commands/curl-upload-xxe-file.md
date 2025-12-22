---
data: 'curl -X POST -F "file=@malicious.xml" https://target.com/upload'
tags:
  - xxe
  - upload
type: command
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
id: f50b9858-907c-43be-b07e-dded9f48ac6b
created_at: '2025-12-13T09:00:27.818Z'
updated_at: '2025-12-13T09:00:27.818Z'
verified: false
validated: true
submitted: true
---
# Curl Upload XXE File

## Command

```bash
curl -X POST -F "file=@malicious.xml" https://target.com/upload
```

## Description

This command uses curl to upload a malicious XML file via a POST request to exploit XXE in file upload features. It simulates form-based file submission.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-F "file=@malicious.xml"` | Form field for file upload | Yes |
| `https://target.com/upload` | Target upload URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -F "file=@malicious.xml" https://target.com/upload
```

### Advanced Usage

```bash
curl -X POST -F "file=@malicious.xml" -H "Authorization: Bearer token" https://target.com/upload
```

## Expected Output

Server response potentially containing exfiltrated data from the XXE exploit, or an error if upload fails.

## Related

- [[procedures/Prepare-XXE-Payload]]
- [[commands/craft-xxe-xml-payload]]
