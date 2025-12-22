---
id: j0k1l2m3-n4o5-6789-jklm-012345678901
name: set-required-schema
type: command
executor: json
data: '{"type": "object","required": ["comments"]}'
output: Validates form for XSS trigger
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:24.324Z'
platforms:
  - Web
tags:
  - xss
  - validation
verified: false
validated: true
submitted: true
---

# set-required-schema

## Command

```json
{"type": "object","required": ["comments"]}
```

## Description

JSON schema object requiring the 'comments' field, enabling form submission and payload execution in react-schema-form.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| required | Array specifying 'comments' field | Yes |

## Examples

### Basic Usage

Enter into schema editor alongside form JSON.

### Advanced Usage

Add more required fields: {"type": "object","required": ["comments", "other"]}

## Expected Output

Schema validates the form, allowing submission to trigger XSS.

## Related

- [[commands/configure-malicious-form-json]]
- [[procedures/Exploit-XSS-in-react-schema-form]]
