---
id: 3203a852-a53c-4391-961c-9b1b0cef4997
name: gather snmp v1 information with standard community strings
type: command
executor: bash
data: 'snmpwalk -v1 -c public target-ip

  snmpwalk -v1 -c private target-ip

  snmpwalk -v1 -c manager target-ip

  '
output: null
created_at: '2020-07-14T18:14:48.538455+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# gather snmp v1 information with standard community strings

```bash
snmpwalk -v1 -c public target-ip
snmpwalk -v1 -c private target-ip
snmpwalk -v1 -c manager target-ip

```
