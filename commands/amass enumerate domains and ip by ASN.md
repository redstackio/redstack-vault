---
id: 68062206-f4ac-46ca-ac49-d31ff24adef7
name: amass enumerate domains and ip by ASN
type: command
executor: ''
data: amass intel -active -asn $_ASN -ip
output: 'root@kali ~# amass intel -active -asn 41264 -ip

  corp.google.com 104.132.31.80'
created_at: '2020-06-29T16:54:21.625706+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# amass enumerate domains and ip by ASN

```bash
amass intel -active -asn $_ASN -ip
```

## Expected Output

```
root@kali ~# amass intel -active -asn 41264 -ip
corp.google.com 104.132.31.80
```
