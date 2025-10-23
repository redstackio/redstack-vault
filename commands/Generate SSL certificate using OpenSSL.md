---
id: 89c73a99-5700-4058-b92c-868883111c66
name: Generate SSL certificate using OpenSSL
type: command
executor: bash
data: openssl req -subj '/CN=[domain.of.server.to.mitm]' -batch -new -x509 -days 365
  -nodes -out server.pem -keyout server.pem
output: null
created_at: '2023-04-06T03:56:22.335940+00:00'
updated_at: '2023-04-10T20:25:09.843906+00:00'
---

# Generate SSL certificate using OpenSSL

```bash
openssl req -subj '/CN=[domain.of.server.to.mitm]' -batch -new -x509 -days 365 -nodes -out server.pem -keyout server.pem
```


