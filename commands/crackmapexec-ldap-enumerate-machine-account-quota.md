---
id: 96e2ff64-5939-4035-959f-34c2e91a378a
name: crackmapexec-ldap-enumerate-machine-account-quota
type: command
executor: bash
data: >-
  crackmapexec ldap $_DC_IP -u $_USERNAME -p '$_PASSWORD' -d '$_DOMAIN'
  --kdcHost $_DC_IP -M MAQ
output: null
created_at: '2023-04-06T03:56:03.034601+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - enumeration
  - active-directory
verified: true
validated: true
---

# crackmapexec-ldap-enumerate-machine-account-quota

## Command

```bash
crackmapexec ldap $_DC_IP -u $_USERNAME -p '$_PASSWORD' -d '$_DOMAIN' --kdcHost $_DC_IP -M MAQ
```

## Description

This command uses CrackMapExec to perform an LDAP query against an Active Directory domain controller, executing the MAQ module to enumerate the machine account quota attribute. It is used during domain reconnaissance to discover policy limits on machine account creation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DC_IP | IP address of the domain controller | Yes |
| $_USERNAME | Domain username for authentication | Yes |
| $_PASSWORD | Password for the username | Yes |
| $_DOMAIN | Fully qualified domain name (e.g., domain.local) | Yes |
| --kdcHost | Specifies the KDC host IP (same as DC usually) | Yes |
| -M MAQ | Runs the Machine Account Quota module | Yes |

## Examples

### Basic Usage

```bash
crackmapexec ldap 10.10.10.10 -u username -p 'Password123' -d 'domain.local' --kdcHost 10.10.10.10 -M MAQ
```

### Advanced Usage

```bash
crackmapexec ldap 10.10.10.10 -u username -p 'Password123' -d 'domain.local' --kdcHost 10.10.10.10 -M MAQ -v
```

## Expected Output

Successful execution shows authentication success and quota details:

LDAP 10.10.10.10:445 BUILTIN\username Pwn3d! (Pwn3d!)
Machine Account Quota: 10

If failed: LDAP 10.10.10.10:445 BUILTIN\username FAILED (Incorrect password)

## Related

- [[procedures/Active-Directory-Machine-Account-Enumeration-using-CrackMapExec]]
- [[tools/CrackMapExec]]
