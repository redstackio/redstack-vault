---
id: fa9e2f53-5837-425d-b627-8fab6436b183
type: command
executor: bash
data: >-
  export KRB5CCNAME=$_KERBEROS_CCACHE; crackmapexec smb $_TARGET_IP -u
  $_USERNAME --use-kcache
output: null
created_at: '2023-04-06T03:56:30.722082+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - credential-testing
  - smb
  - kerberos
verified: true
validated: true
---

# crackmapexec-smb-with-kerberos

## Command

```bash
export KRB5CCNAME=$_KERBEROS_CCACHE; crackmapexec smb $_TARGET_IP -u $_USERNAME --use-kcache
```

## Description

Uses a Kerberos ticket cache for SMB authentication, ideal for overpass-the-hash or ticket delegation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_KERBEROS_CCACHE | Path to Kerberos ticket cache (e.g., /tmp/krb5cc) | Yes |
| $_TARGET_IP | Target IP | Yes |
| -u $_USERNAME | Username associated with ticket | Yes |
| --use-kcache | Flag to use Kerberos cache | Yes |
| smb | SMB protocol | Built-in |

## Examples

### Basic Usage

```bash
export KRB5CCNAME=/tmp/kerberos/admin.ccache; crackmapexec smb 192.168.1.100 -u admin --use-kcache
```

## Expected Output

Success:

SMB                 192.168.1.100:445     100       admin:<KRB5CCACHE>                              [+] (corp\admin)

Failure:

SMB                 192.168.1.100:445     100       admin:<KRB5CCACHE>                              [-] KRB5CCNAME not found or invalid

## Related

- [[procedures/Test-Credentials-Against-Multiple-Protocols-with-CrackMapExec]]
