---
id: 452b655f-0991-46cf-ae03-245000c0002b
name: Show last system boot time
type: command
executor: bash
data: 'Get-WmiObject win32_operatingsystem | select csname, @{LABEL=''LastBootUpTime'';
  EXPRESSION={$_.ConverttoDateTime($_.lastbootuptime)}}

  '
output: null
created_at: '2020-07-14T18:21:10.753392+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Show last system boot time

```bash
Get-WmiObject win32_operatingsystem | select csname, @{LABEL='LastBootUpTime'; EXPRESSION={$_.ConverttoDateTime($_.lastbootuptime)}}

```
