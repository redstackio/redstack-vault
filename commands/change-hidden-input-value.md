---
id: ffba3a64-d385-47f6-b969-e2ae3a8ec835
name: change-hidden-input-value
type: command
executor: bash
data: 'curl -X POST -d "page=4" http://target.com/rpo-endpoint'
output: null
created_at: '2023-04-06T03:56:43.833053+00:00'
updated_at: '2023-04-06T03:56:43.857346+00:00'
platforms:
  - Web
tags:
  - rpo
  - manipulation
verified: true
validated: true
---

# change-hidden-input-value

## Command

```bash
curl -X POST -d "page=4" http://target.com/rpo-endpoint
```

## Description

Modifies a hidden input field in a POST request to alter application flow for RPO exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -d "page=4" | Value to set for hidden field | Yes |
| http://target.com/rpo-endpoint | Target URL | Yes |

## Examples

### Basic Usage

```bash
curl -X POST -d "page=4" http://target.com/rpo-endpoint
```

## Expected Output

Response with modified page state, enabling path overwrite.

## Related

- [[procedures/Exploit-RPO-for-Stored-XSS-via-CSS-Injection-in-IE]]
