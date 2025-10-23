---
id: 22f18687-1ac3-4faf-82be-6b3116d9ea4f
name: 'sort and tail # of results'
type: command
executor: ''
data: cat $_FILE | sort | tail -n 25
output: 'root@kali ~# cat resolvers.txt | sort | tail -n 10

  94.94.89.38

  95.109.18.6

  95.109.30.117

  95.142.162.240

  95.154.58.46

  95.155.206.55

  95.163.86.6

  95.172.66.6

  95.174.99.142

  95.174.99.179

  '
created_at: '2020-06-30T02:54:42.363161+00:00'
updated_at: '2023-03-13T19:50:21.945040+00:00'
---

# sort and tail # of results

```bash
cat $_FILE | sort | tail -n 25
```

## Expected Output

```
root@kali ~# cat resolvers.txt | sort | tail -n 10
94.94.89.38
95.109.18.6
95.109.30.117
95.142.162.240
95.154.58.46
95.155.206.55
95.163.86.6
95.172.66.6
95.174.99.142
95.174.99.179

```


