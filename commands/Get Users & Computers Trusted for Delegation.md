---
id: 14a9755c-674c-40c1-a880-927b7e2a1711
name: Get Users & Computers Trusted for Delegation
type: command
executor: bash
data: 'Get-DomainUser -TrustedtoAuth -Properties distinguisedname,useraccountcontrol,msds-allowedtodelegateto|fl
  Get-DomainComputer -TrustedtoAuth -Properties distinguisedname,useraccountcontrol,msds-allowedtodelegateto|fl

  '
output: null
created_at: '2020-07-14T18:21:07.167468+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Get Users & Computers Trusted for Delegation

```bash
Get-DomainUser -TrustedtoAuth -Properties distinguisedname,useraccountcontrol,msds-allowedtodelegateto|fl Get-DomainComputer -TrustedtoAuth -Properties distinguisedname,useraccountcontrol,msds-allowedtodelegateto|fl

```


