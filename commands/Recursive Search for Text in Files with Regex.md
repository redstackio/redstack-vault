---
id: 15868e77-662d-46de-8d30-65445744bd4a
name: Recursive Search for Text in Files with Regex
type: command
executor: ''
data: grep -RE $_REGEX $_PATH
output: 'root@a7ffb5e7e757:/# grep -RE ''^root'' /etc/shadow

  root:*:18291:0:99999:7:::'
created_at: '2020-03-10T07:20:54.638165+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[grep]]'
---

# Recursive Search for Text in Files with Regex

```bash
grep -RE $_REGEX $_PATH
```

## Expected Output

```
root@a7ffb5e7e757:/# grep -RE '^root' /etc/shadow
root:*:18291:0:99999:7:::
```


