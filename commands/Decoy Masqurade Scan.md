---
id: d17c0c02-4a52-4aab-814d-9533a23cd6ff
name: Decoy Masqurade Scan
type: command
executor: bash
data: 'nmap -sS -sV -D $ip2,$ip3,$ip4,$ip5 -f --mtu=24 --data-length=1337 -T2 $ip

  nmap -Pn -T2 -sV --randomize-hosts $ip,$ip2

  '
output: null
created_at: '2020-07-14T18:15:19.609602+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Decoy Masqurade Scan

```bash
nmap -sS -sV -D $ip2,$ip3,$ip4,$ip5 -f --mtu=24 --data-length=1337 -T2 $ip
nmap -Pn -T2 -sV --randomize-hosts $ip,$ip2

```


