---
id: dff5ff91-4ff9-4913-ba62-b7dd585f2e88
name: SNMPWALK
type: command
executor: bash
data: 'snmpwalk -v 1 -c public $ip

  snmpbulkwalk -v 2 -c public $ip

  '
output: null
created_at: '2020-07-14T18:14:33.565123+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# SNMPWALK

```bash
snmpwalk -v 1 -c public $ip
snmpbulkwalk -v 2 -c public $ip

```
