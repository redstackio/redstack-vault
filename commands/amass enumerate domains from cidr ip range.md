---
id: 09185716-0859-446e-86fb-9cbcc5657a80
name: amass enumerate domains from cidr ip range
type: command
executor: ''
data: amass intel -ip -cidr 13.224.8.0/21
output: 'root@kali ~# amass intel -ip -cidr 13.224.8.0/21

  r.cloudfront.net 13.224.13.184'
created_at: '2020-06-29T16:32:10.894203+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# amass enumerate domains from cidr ip range

```bash
amass intel -ip -cidr 13.224.8.0/21
```

## Expected Output

```
root@kali ~# amass intel -ip -cidr 13.224.8.0/21
r.cloudfront.net 13.224.13.184
```
