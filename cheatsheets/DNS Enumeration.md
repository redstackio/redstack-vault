---
id: 07d9d940-14db-4e8d-b77c-341838800668
name: DNS Enumeration
type: cheatsheet
verified: true
created_at: '2019-09-18T22:07:52.707234+00:00'
updated_at: '2023-05-30T20:09:23.425289+00:00'
---

# DNS Enumeration

**Status**: ✓ Verified

# Description

Active DNS enumeration, subdomain brute forcing, and zone transfers.



## host





**Command** ([[host Query a DNS Server for A, AAAA, and MX Records]]):

```bash
host $_TARGET_HOST
```







**Command** ([[host Query a DNS Server for Name Servers]]):

```bash
host -t ns $_TARGET_HOST
```







**Command** ([[host Query a DNS Server for Mail Servers]]):

```bash
host -t mx $_TARGET_HOST
```







**Command** ([[host Attempt a DNS Zone Transfer]]):

```bash
host -l $_DOMAIN_NAME $_TARGET_HOST
```







**Command** ([[host Attempt a DNS Zone Transfer and List All Records]]):

```bash
host -a -l $_DOMAIN_NAME $_TARGET_HOST
```





## DNSRecon





**Command** ([[DNSRecon DNS Zone Transfer]]):

```bash
dnsrecon -d $_TARGET_DOMAIN -t axfr
```







**Command** ([[DNSRecon Brute Force DNS Subdomains]]):

```bash
dnsrecon -d $_TARGET_DOMAIN -t brt -D $_FULL_PATH_TO_DICTIONARY
```





## dnsenum





**Command** ([[dnsenum Query a DNS Server and Attempt a Zone Transfer]]):

```bash
dnsenum $_TARGET_DOMAIN
```







**Command** ([[dnsenum Brute Force DNS Subdomains]]):

```bash
dnsenum -r $_TARGET_DOMAIN -f $_DICTIONARY
```






