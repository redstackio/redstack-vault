---
id: 6a094c2e-607c-447f-ad19-de7daf39f07c
name: amass visualize assets using d3 from a previous scan
type: command
executor: bash
data: amass viz -d3 -dir $_OUTPUT_DIRECTORY
output: 'root@kali in ~# ls owasp.org/

  amass_d3.html  amass.json  amass.log  amass.txt  indexes.bolt'
created_at: '2020-06-29T18:05:44.400879+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# amass visualize assets using d3 from a previous scan

```bash
amass viz -d3 -dir $_OUTPUT_DIRECTORY
```

## Expected Output

```
root@kali in ~# ls owasp.org/
amass_d3.html  amass.json  amass.log  amass.txt  indexes.bolt
```


