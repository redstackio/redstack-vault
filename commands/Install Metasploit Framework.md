---
id: 92aaf94b-8acc-4490-a9d8-4b1ca8f8d995
name: Install Metasploit Framework
type: command
executor: bash
data: curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb
  > msfinstall && chmod 755 msfinstall && ./msfinstall
output: null
created_at: '2023-04-06T03:56:21.178025+00:00'
updated_at: '2023-04-10T20:24:59.324258+00:00'
---

# Install Metasploit Framework

```bash
curl https://raw.githubusercontent.com/rapid7/metasploit-omnibus/master/config/templates/metasploit-framework-wrappers/msfupdate.erb > msfinstall && chmod 755 msfinstall && ./msfinstall
```
