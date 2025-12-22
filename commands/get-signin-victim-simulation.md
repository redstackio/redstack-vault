---
data: >+
  GET /signin HTTP/1.1

  Host: launchpad.37signals.com

  Connection: close

  Upgrade-Insecure-Requests: 1

  User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36
  (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36

  Accept:
  text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

  Accept-Encoding: gzip, deflate

  Accept-Language: en-US,en;q=0.9,la;q=0.8

  Cookie:
  _launchpad_session=uViarUZn10afBS9AD4AgD9lF4iEk6%2FIfinxiAVgiEQNq2xMTKY86i9r%2FZEQ%2BENl183aEL845OspHItodYdrC0OIEWMzEjswGng%2F%2BXwE5nsYBhY7ep%2B%2FmrDB1ZXa%2B1NaAji52own5luVsggkP98GrqNjnWHxGdIfffZjMFwz3Q3fNxV0NilS1DmNiY0P72x9CDsrQfzc0HbGfnL%2BEvs9%2BODfbfJYnexsrxX2P78RaQ8wf--0zL8fFbFTz6maAwm--XxtVi%2BPuHcoHD8hjqSkxkQ%3D%3D

tags:
  - http
  - simulation
type: command
executor: bash
platforms:
  - Web
id: ab38bf7d-2667-43ad-9808-3b117134d64b
created_at: '2025-12-13T09:01:21.706Z'
updated_at: '2025-12-13T09:01:21.706Z'
verified: false
validated: true
submitted: true
---
# get-signin-victim-simulation

## Command

```bash
GET /signin HTTP/1.1
Host: launchpad.37signals.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,la;q=0.8
Cookie: _launchpad_session=uViarUZn10afBS9AD4AgD9lF4iEk6%2FIfinxiAVgiEQNq2xMTKY86i9r%2FZEQ%2BENl183aEL845OspHItodYdrC0OIEWMzEjswGng%2F%2BXwE5nsYBhY7ep%2B%2FmrDB1ZXa%2B1NaAji52own5luVsggkP98GrqNjnWHxGdIfffZjMFwz3Q3fNxV0NilS1DmNiY0P72x9CDsrQfzc0HbGfnL%2BEvs9%2BODfbfJYnexsrxX2P78RaQ8wf--0zL8fFbFTz6maAwm--XxtVi%2BPuHcoHD8hjqSkxkQ%3D%3D

```

## Description

Simulates a normal visitor request to /signin to observe the impact of the smuggled request.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `Cookie` | Includes session cookie | Yes |
| `Connection` | close to terminate the connection | Yes |
| `User-Agent` | Mimics a browser user agent | Yes |

## Examples

### Basic Usage

```bash
GET /signin HTTP/1.1
Host: launchpad.37signals.com
Connection: close
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.129 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Accept-Encoding: gzip, deflate
Accept-Language: en-US,en;q=0.9,la;q=0.8
Cookie: _launchpad_session=uViarUZn10afBS9AD4AgD9lF4iEk6%2FIfinxiAVgiEQNq2xMTKY86i9r%2FZEQ%2BENl183aEL845OspHItodYdrC0OIEWMzEjswGng%2F%2BXwE5nsYBhY7ep%2B%2FmrDB1ZXa%2B1NaAji52own5luVsggkP98GrqNjnWHxGdIfffZjMFwz3Q3fNxV0NilS1DmNiY0P72x9CDsrQfzc0HbGfnL%2BEvs9%2BODfbfJYnexsrxX2P78RaQ8wf--0zL8fFbFTz6maAwm--XxtVi%2BPuHcoHD8hjqSkxkQ%3D%3D

```

## Expected Output

Normal response unless poisoned, in which case redirection occurs.

## Related

- [[procedures/Simulate-Victim-Requests-to-Observe-Poisoning]]
