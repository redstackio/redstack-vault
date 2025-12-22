---
data: 'javascript:alert(1)'
tags:
  - recon
  - validation-test
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:38.276Z'
id: 6842d102-60e9-4b50-a3bb-f4d3ce684087
verified: false
validated: true
submitted: true
---
# test-url-scheme

## Command

```javascript
javascript:alert(1)
```

## Description

Simple JavaScript URI to test if URL inputs accept and execute dangerous schemes, confirming XSS potential.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| alert(1) | Basic JS to trigger popup | Yes |

## Examples

### Basic Usage

```javascript
javascript:alert(1)
```

### Advanced Usage

```javascript
javascript:console.log('Test')
```

## Expected Output

Alert dialog or console log if executed on render.

## Related

- [[procedures/Identify-Lack-of-URL-Validation-in-SocialIcon-Link]]
