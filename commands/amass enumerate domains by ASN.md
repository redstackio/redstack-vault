---
id: ed440e9d-f373-4cee-abfd-dbb36948de91
name: amass enumerate domains by ASN
type: command
executor: bash
data: amass intel -asn $_ASN
output: 'root@kali ~# amass intel -asn 41264

  corp.google.com

  '
created_at: '2020-06-29T16:38:40.327469+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[amass]]'
---

# amass enumerate domains by ASN

```bash
amass intel -asn $_ASN
```

## Expected Output

```
root@kali ~# amass intel -asn 41264
corp.google.com

```


