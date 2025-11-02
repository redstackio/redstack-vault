---
id: 5a4a21ec-34c4-4cea-b5c2-827e9951615b
name: Set the KRBCCNAME Value to a Local File
type: command
executor: bash
data: export KRB5CCNAME="$(pwd)/Administrator.ccache"
output: root@kali:~# export KRB5CCNAME="$(pwd)/Administrator.ccache"
created_at: '2020-06-24T05:08:26.192345+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[SET]]'
---

# Set the KRBCCNAME Value to a Local File

```bash
export KRB5CCNAME="$(pwd)/Administrator.ccache"
```

## Expected Output

```
root@kali:~# export KRB5CCNAME="$(pwd)/Administrator.ccache"
```


