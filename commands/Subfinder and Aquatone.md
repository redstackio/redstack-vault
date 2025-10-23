---
id: 00563379-0fd3-408f-8074-94a362358d41
name: Subfinder and Aquatone
type: command
executor: bash
data: './Subfinder/subfinder -d $1 -r 8.8.8.8,1.1.1.1 -nW -o /tmp/subresult$1

  cat /tmp/subresult$1 | ./Aquatone/aquatone -ports large -out /tmp/aquatone$1'
output: null
created_at: '2023-04-06T03:56:25.630730+00:00'
updated_at: '2023-04-10T20:25:37.405281+00:00'
---

# Subfinder and Aquatone

```bash
./Subfinder/subfinder -d $1 -r 8.8.8.8,1.1.1.1 -nW -o /tmp/subresult$1
cat /tmp/subresult$1 | ./Aquatone/aquatone -ports large -out /tmp/aquatone$1
```


