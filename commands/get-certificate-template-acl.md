---
type: command
executor: bash
data: >-
  python3 modifyCertTemplate.py $_DOMAIN/$_USERNAME -k -no-pass -template
  $_TEMPLATE_NAME -dc-ip $_DC_IP -get-acl
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - ad-cs
  - recon
verified: true
validated: true
---

# get-certificate-template-acl

## Command

```bash
python3 modifyCertTemplate.py $_DOMAIN/$_USERNAME -k -no-pass -template $_TEMPLATE_NAME -dc-ip $_DC_IP -get-acl
```

## Description

Retrieves the access control list (ACL) for a specified certificate template in AD CS via LDAP query, helping identify if the current user can modify the template for exploitation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | Target domain (e.g., domain.local) | Yes |
| $_USERNAME | Username for authentication (e.g., user) | Yes |
| -k | Use Kerberos authentication with current ticket | Yes |
| -no-pass | No password prompt (uses ticket) | Yes |
| -template $_TEMPLATE_NAME | Name of the certificate template (e.g., User) | Yes |
| -dc-ip $_DC_IP | IP address of the domain controller (e.g., 10.10.10.10) | Yes |
| -get-acl | Flag to retrieve ACL details | Yes |

## Examples

### Basic Usage

```bash
python3 modifyCertTemplate.py domain.local/user -k -no-pass -template User -dc-ip 10.10.10.10 -get-acl
```

### Advanced Usage

Use with a specific user in a subdomain if applicable.

## Expected Output

Outputs a list of ACL entries, such as:

```
Access Control Entries:
- Principal: Everyone
  Rights: WriteProperty (Full Control on msPKI-Certificate-Name-Flag)
```

Look for 'WriteProperty' or 'GenericAll' granted to low-priv groups.

## Related

- [[procedures/Active-Directory-Certificate-Services-Access-Control-Vulnerabilities]]
- [[tools/certipy]]
