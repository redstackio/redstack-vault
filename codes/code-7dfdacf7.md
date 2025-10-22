---
id: 7dfdacf7-1b72-4a02-8073-cacfd760092c
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:56:25.630655+00:00'
updated_at: '2023-04-10T20:25:37.406217+00:00'
---

# Code Snippet 7dfdacf7

**Language**: Powershell

```powershell
# Subfinder version
./Subfinder/subfinder -d $1 -r 8.8.8.8,1.1.1.1 -nW -o /tmp/subresult$1
cat /tmp/subresult$1 | ./Aquatone/aquatone -ports large -out /tmp/aquatone$1

# Amass version
./Amass/amass -active -brute -o /tmp/hosts.txt -d $1
cat /tmp/hosts.txt | ./Aquatone/aquatone -ports large -out /tmp/aquatone$1
```
