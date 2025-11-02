---
id: 02d93c9a-75ed-404a-89b7-b5271449024a
name: Brute Force SNMP Community String
type: command
executor: bash
data: onesixtyone -c $_WORDLIST $_TARGET_IP
output: 'root@kali:~/Documents# onesixtyone -c wordlist.txt 10.10.10.10

  Scanning 1 hosts, 4603 communities

  10.10.10.20 [public] Linux Host 4.4.0-75-generic #96~14.04.1-Ubuntu SMP Thu Apr
  20 11:06:56 UTC 2017 i686'
created_at: '2019-09-17T00:51:23.939596+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[host]]'
- '[[onesixtyone]]'
---

# Brute Force SNMP Community String

```bash
onesixtyone -c $_WORDLIST $_TARGET_IP
```

## Expected Output

```
root@kali:~/Documents# onesixtyone -c wordlist.txt 10.10.10.10
Scanning 1 hosts, 4603 communities
10.10.10.20 [public] Linux Host 4.4.0-75-generic #96~14.04.1-Ubuntu SMP Thu Apr 20 11:06:56 UTC 2017 i686
```


