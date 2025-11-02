---
id: 51bbc53b-14be-4359-aa15-b845a0155bd5
name: sort massdns output for online hosts
type: command
executor: ''
data: cat $_MASSDNS_OUTPUT | awk '{print $1}' | sed 's/.$//' | sort -u > $_OUTPUT_FILE
output: 'root@hacker:~# cat massdns.out | awk ''{print $1}'' | sed ''s/.$//'' | sort
  -u > hosts-online.txt

  austin.owasp.org

  calendar.owasp.org

  contact.owasp.org

  dev.owasp.org

  docs.owasp.org

  gapps.owasp.org

  groups.owasp.org

  kerala.owasp.org

  lists.owasp.org

  mail.owasp.org

  sl.owasp.org

  videos.owasp.org

  wiki.owasp.org

  www2.owasp.org

  www.owasp.org'
created_at: '2020-06-30T05:00:10.524170+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[CAT]]'
- '[[massdns]]'
---

# sort massdns output for online hosts

```bash
cat $_MASSDNS_OUTPUT | awk '{print $1}' | sed 's/.$//' | sort -u > $_OUTPUT_FILE
```

## Expected Output

```
root@hacker:~# cat massdns.out | awk '{print $1}' | sed 's/.$//' | sort -u > hosts-online.txt
austin.owasp.org
calendar.owasp.org
contact.owasp.org
dev.owasp.org
docs.owasp.org
gapps.owasp.org
groups.owasp.org
kerala.owasp.org
lists.owasp.org
mail.owasp.org
sl.owasp.org
videos.owasp.org
wiki.owasp.org
www2.owasp.org
www.owasp.org
```


