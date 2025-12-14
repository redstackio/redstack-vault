---
id: cmd-react-schema
data: '{ "type": "object", "required": [ "comments" ] }'
tags:
  - xss
  - json
type: command
output: Triggers evaluation of the condition in the form
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:08.424Z'
verified: false
validated: true
submitted: true
---
# react-schema-form-schema

## Command

```json
{ "type": "object", "required": [ "comments" ] }
```

## Description

Complementary JSON schema for react-schema-form that requires the 'comments' field, forcing evaluation of the malicious condition for XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| required | Array of required fields | Yes |
| type | Schema type (object) | Yes |

## Examples

### Basic Usage

Input into schema editor alongside form.

### Advanced Usage

Add more required fields to chain conditions.

## Expected Output

Triggers evaluation of the condition in the form

## Related

- [[procedures/Trigger-XSS-with-Malicious-Form-Schema]]
