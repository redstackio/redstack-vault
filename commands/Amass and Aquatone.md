---
id: 68012c3f-082c-4c00-9fd3-9d2b76ff6681
name: Amass and Aquatone
type: command
executor: bash
data: './Amass/amass -active -brute -o /tmp/hosts.txt -d $1

  cat /tmp/hosts.txt | ./Aquatone/aquatone -ports large -out /tmp/aquatone$1'
output: null
created_at: '2023-04-06T03:56:25.630797+00:00'
updated_at: '2023-04-10T20:25:37.405281+00:00'
---

# Amass and Aquatone

```bash
./Amass/amass -active -brute -o /tmp/hosts.txt -d $1
cat /tmp/hosts.txt | ./Aquatone/aquatone -ports large -out /tmp/aquatone$1
```


