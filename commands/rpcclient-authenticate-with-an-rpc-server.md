---
id: 33ff043a-6e43-4561-ab56-91233e200a36
type: command
executor: bash
data: rpcclient -U "$_USERNAME%$_PASSWORD" $_TARGET_IP
output: rpcclient -U "bob%secretpass" 10.10.10.10
created_at: '2019-09-18T23:26:06.918339+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - rpc
  - smb
verified: true
validated: true
---

# rpcclient-authenticate-with-an-rpc-server

## Command

```bash
rpcclient -U "$_USERNAME%$_PASSWORD" $_TARGET_IP
```

## Description

This command establishes a connection to a Windows SMB/RPC server using rpcclient, opening an interactive shell for further RPC-based enumeration. It can use null authentication for anonymous access (limited info) or valid credentials for comprehensive domain discovery. Ideal for initial connection in Active Directory reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_USERNAME | Domain username (e.g., bob); use empty string "" for null session | No |
| $_PASSWORD | Password for the username; use empty string "" for null session | No |
| $_TARGET_IP | IP address of the target SMB/RPC server (e.g., 10.10.10.10) | Yes |
| -U | Specifies the username and password in "user%pass" format | Built-in |

## Examples

### Basic Usage (Null Session)

```bash
rpcclient -U "" 10.10.10.10
```

Connects anonymously if the server allows null sessions.

### Advanced Usage (Authenticated)

```bash
rpcclient -U "DOMAIN\\bob%secretpass" 10.10.10.10
```

Uses domain credentials for authenticated access.

## Expected Output

Successful connection drops into an interactive rpcclient shell:

```
rpcclient $
```

From here, you can run commands like `enumdomusers` or `srvinfo`. Failure shows errors like:

```
NT_STATUS_LOGON_FAILURE: Logon failure
```

For null sessions, success without credentials indicates anonymous RPC access is enabled.

## Related

- [[procedures/List-Domain-Users-and-Groups-with-MS-RPC-SMB-Service]]
- [[tools/rpcclient]]
