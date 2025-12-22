---
id: cmd-invokelink-001
data: >-
  invokeLink = () => { this.element.innerHTML = this.props.options ==
  defaultOptions ? Autolinker.link(this.props.text) :
  Autolinker.link(this.props.text, this.props.options) }
tags:
  - xss
  - innerhtml
type: command
output: innerHTML set; scripts execute if present.
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:16:02.617Z'
verified: false
validated: true
submitted: true
---
# observe-invokelink-execution

## Command

```javascript
invokeLink = () => {
  this.element.innerHTML = this.props.options == defaultOptions
    ? Autolinker.link(this.props.text)
    : Autolinker.link(this.props.text, this.props.options)
}
```

## Description

Method in AutolinkerWrapper that sets innerHTML to linked text, vulnerable to XSS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| this.props.text | User text | Yes |
| this.props.options | Linking config | No |

## Examples

### Basic Usage

```javascript
invokeLink();
```

## Expected Output

Element updated with HTML; executes embedded scripts.

## Related

- [[commands/inject-malicious-xss-payload]]
