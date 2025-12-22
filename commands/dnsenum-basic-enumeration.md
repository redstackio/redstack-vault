---
type: command
executor: bash
data: dnsenum $_TARGET_DOMAIN
tags:
  - enumeration
  - dns
platforms:
  - Linux
verified: true
validated: true
---

# dnsenum-basic-enumeration

## Command

```bash
dnsenum $_TARGET_DOMAIN
```

## Description

This command performs basic DNS enumeration on a target domain, retrieving host addresses, name servers, and attempting zone transfers to discover additional DNS records.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_DOMAIN | The domain name to enumerate (e.g., example.com) | Yes |

## Examples

### Basic Usage

```bash
dnsenum example.com
```

### Advanced Usage

For more advanced enumeration with brute-forcing, use additional options like `--enum` or specify a wordlist, but this command focuses on the basic invocation.

```bash
dnsenum --enum example.com
```

## Expected Output

```
root@kali:~# dnsenum testsite.com
dnsenum VERSION:1.2.4

-----   testsite.com   -----


Host's addresses:
__________________

testsite.com.                         7199     IN    A      203.22.87.231 


Name Servers:
______________

nsztm2.testsite.com.                     10799    IN    A        203.22.87.231
nsztm1.testsite.com.                     10799    IN    A        203.22.88.232


Trying Zone Transfers and getting Bind Versions:
_________________________________________________


Trying Zone Transfer for testsite.com on nsztm2.testsite.com ...
testsite.com.                         7200     IN    SOA               (
testsite.com.                         300      IN    HINFO        "Casio
testsite.com.                         301      IN    TXT               (
testsite.com.                         7200     IN    MX                0
testsite.com.                         7200     IN    MX               10

brute force file not specified, bay.
```

## Related

- [[tools/dnsenum]]
- [[procedures/DNS-Enumeration-for-Reconnaissance]]
