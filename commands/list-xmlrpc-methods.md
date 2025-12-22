---
data: >-
  curl -X POST https://nordvpn.com/xmlrpc.php -H "Content-Type: text/xml" -d
  '<?xml version="1.0"
  encoding="utf-8"?><methodCall><methodName>system.listMethods</methodName><params></params></methodCall>'
  -v
tags:
  - recon
  - xmlrpc
type: command
output: null
executor: bash
platforms:
  - Linux
  - Web
created_at: '2024-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:56.549Z'
id: 9d06d3df-03f8-4921-88be-5aa25faa0bf0
verified: false
validated: true
submitted: true
---
# list-xmlrpc-methods

## Command

```bash
curl -X POST https://nordvpn.com/xmlrpc.php \
  -H "Content-Type: text/xml" \
  -d '<?xml version="1.0" encoding="utf-8"?><methodCall><methodName>system.listMethods</methodName><params></params></methodCall>' -v
```

## Description

Sends an XML-RPC request to list all available methods on the xmlrpc.php endpoint, confirming if it's enabled on a WordPress site. Use this for initial reconnaissance to identify exploitable functions.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: text/xml"` | Sets XML content type | Yes |
| `-d '...' ` | XML payload with system.listMethods | Yes |
| `-v` | Verbose output for HTTP details | No |
| Target URL | Replace https://nordvpn.com with target domain | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://example.com/xmlrpc.php -H "Content-Type: text/xml" -d '<?xml version="1.0"?><methodCall><methodName>system.listMethods</methodName></methodCall>'
```

### Advanced Usage

```bash
curl -X POST https://nordvpn.com/xmlrpc.php -H "Content-Type: text/xml" -H "User-Agent: Mozilla/5.0" -d '<?xml version="1.0" encoding="utf-8"?><methodCall><methodName>system.listMethods</methodName><params></params></methodCall>' --cookie "__cfduid=example"
```

## Expected Output

XML response like: <?xml version="1.0"?><methodResponse><params><param><value><array><data><value><string>pingback.ping</string></value>...</data></array></value></param></params></methodResponse>. Lists methods if successful; faults if disabled.

## Related

- [[Related Procedure|procedures/Verify-XML-RPC-Endpoint-Accessibility]]
