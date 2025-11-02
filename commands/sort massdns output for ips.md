---
id: 67677097-dd4e-4ee2-8135-2b502ffb25f3
name: sort massdns output for ips
type: command
executor: ''
data: cat $_MASSDNS_OUTPUT | awk '{print $3}' | sort -u | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b"
  > $_OUTPUT_FILE
output: 'root@hacker:~# cat massdns.out | awk ''{print $3}'' | sort -u | grep -oE
  "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" > ips-online.txt

  104.22.26.77

  104.22.27.77

  172.67.10.39'
created_at: '2020-06-30T05:03:09.607678+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[CAT]]'
- '[[grep]]'
- '[[massdns]]'
---

# sort massdns output for ips

```bash
cat $_MASSDNS_OUTPUT | awk '{print $3}' | sort -u | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" > $_OUTPUT_FILE
```

## Expected Output

```
root@hacker:~# cat massdns.out | awk '{print $3}' | sort -u | grep -oE "\b([0-9]{1,3}\.){3}[0-9]{1,3}\b" > ips-online.txt
104.22.26.77
104.22.27.77
172.67.10.39
```


