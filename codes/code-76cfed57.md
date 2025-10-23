---
id: 76cfed57-3558-4d85-8b62-3931f763bae8
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:57.446837+00:00'
updated_at: '2023-04-06T03:55:57.457187+00:00'
---

# Code Snippet 76cfed57

**Language**: Powershell

```powershell
swissky@crashlab:~$ time if [ $(whoami|cut -c 1) == s ]; then sleep 5; fi
real    0m5.007s
user    0m0.000s
sys 0m0.000s

swissky@crashlab:~$ time if [ $(whoami|cut -c 1) == a ]; then sleep 5; fi
real    0m0.002s
user    0m0.000s
sys 0m0.000s
```


