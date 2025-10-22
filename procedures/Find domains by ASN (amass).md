---
id: 65aaca1d-d39a-49d9-ae18-f590e05a7609
name: Find domains by ASN (amass)
type: procedure
verified: false
submitted: false
created_at: '2020-06-29T16:38:40.350331+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
commands:
- '[[amass enumerate domains and ip by ASN]]'
- '[[amass enumerate domains by ASN]]'
---

# Find domains by ASN (amass)

## Summary

The Autonomous System Number is uniquely allocated to organizations and directly tied to public IP Ranges provided to these organizations. Using the 'amass' tool we can lookup domains / subdomains by using the ASN number 

## Description

## Description

The Autonomous System Number is uniquely allocated to organizations and directly tied to public IP Ranges provided to these organizations.

Using the 'amass' tool we can lookup domains / subdomains by using the ASN number

**Command** ([[amass enumerate domains by ASN]]):

```bash
amass intel -asn $_ASN
```

Secondary command to retrieve the IP also

**Command** ([[amass enumerate domains and ip by ASN]]):

```bash
amass intel -active -asn $_ASN -ip
```

## Commands Used

- [[amass enumerate domains and ip by ASN]]
- [[amass enumerate domains by ASN]]
