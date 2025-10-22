---
id: 4818b02d-f61f-40a8-9184-e1a5bfd562bf
name: Find Company ASN (amass)
type: procedure
verified: false
submitted: false
created_at: '2020-06-29T16:27:45.213356+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
commands:
- '[[amass enumerate company properties]]'
---

# Find Company ASN (amass)

## Summary

This is useful for finding additional information on a company, perhaps a subdivision or part of a merger and acquisition. Using amass to enumerate company information, this can return ASN id's assigned to the target. ASN id's can be used to enumerate IP Range information, Organization's,  even sub

## Description

## Description

This is useful for finding additional information on a company, perhaps a subdivision or part of a merger and acquisition.

Using amass to enumerate company information, this can return ASN id's assigned to the target.

ASN id's can be used to enumerate IP Range information, Organization's,  even sub domains.

**Command** ([[amass enumerate company properties]]):

```bash
amass intel -org $_COMPANY_NAME
```

## Commands Used

- [[amass enumerate company properties]]
