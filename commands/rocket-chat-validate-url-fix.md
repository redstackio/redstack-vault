---
data: >-
  const validateUrl=(url, presentTokens)=>{try{new
  URL(url);return!(presentTokens && presentTokens.length >0 && new
  RegExp(presentTokens.join("|")).test(url));}catch(e){return false;}};
tags:
  - mitigation
  - fix
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.225Z'
id: 5287af66-f73d-4b3f-8cd2-d8612fd2ac78
verified: false
validated: true
submitted: true
---
# rocket-chat-validate-url-fix

## Command

```javascript
const validateUrl=(url, presentTokens)=>{try{new URL(url);return!(presentTokens && presentTokens.length >0 && new RegExp(presentTokens.join("|")).test(url));}catch(e){return false;}};
```

## Description

Proposed fix function to validate URLs against Markdown tokens.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| url | URL to check | Yes |
| presentTokens | Array of tokens like ['[', ']'] | Yes |

## Examples

### Basic Usage

```javascript
validateUrl('https://a?p=[ ]', ['[', ']']); // false
```

## Expected Output

Boolean: true if valid URL without tokens.

## Related

- [[procedures/Craft-and-Send-Malicious-XSS-Payload]]
