---
id: 650475bd-c92f-4d7d-a718-1b41c22f7544
name: Find domains by cidr (amass)
type: procedure
verified: false
submitted: false
created_at: '2020-06-29T16:32:10.923635+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
commands:
- '[[amass enumerate domains from cidr ip range]]'
---

# Find domains by cidr (amass)

## Summary

description Enumerating domain names from a CIDR IP Range can prove useful when dealing with organizations hosting with Managed Service Providers or in their own Data Centers. This won't be as useful with cloud hosting environments because the elastic IP's provisioned will not belong to a single IP

## Description

description

Enumerating domain names from a CIDR IP Range can prove useful when dealing with organizations hosting with Managed Service Providers or in their own Data Centers.



This won't be as useful with cloud hosting environments because the elastic IP's provisioned will not belong to a single IP Range or Organization ASN, they will belong to the Cloud Hosting Provider







**Command** ([[amass enumerate domains from cidr ip range]]):

```bash
amass intel -ip -cidr 13.224.8.0/21
```





## Commands Used

- [[amass enumerate domains from cidr ip range]]


