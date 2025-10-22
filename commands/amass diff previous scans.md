---
id: 8fc6e5a0-bc2d-4a64-8dff-2d05f181e603
name: amass diff previous scans
type: command
executor: bash
data: amass track -dir $_OUTPUT_DIRECTORY -d $_TARGET_DOMAIN -last 2
output: "root@kali ~# amass track -dir owasp.org/ -d owasp.org -last 2\n--------------------------------------------------------------------------------\n\
  Between\t06/29 13:49:56 2020 EDT -> 06/29 13:51:11 2020 EDT\nand\t06/29 13:44:43\
  \ 2020 EDT -> 06/29 13:47:18 2020 EDT\n--------------------------------------------------------------------------------\n\
  No differences discovered"
created_at: '2020-06-29T18:05:44.398305+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# amass diff previous scans

```bash
amass track -dir $_OUTPUT_DIRECTORY -d $_TARGET_DOMAIN -last 2
```

## Expected Output

```
root@kali ~# amass track -dir owasp.org/ -d owasp.org -last 2
--------------------------------------------------------------------------------
Between	06/29 13:49:56 2020 EDT -> 06/29 13:51:11 2020 EDT
and	06/29 13:44:43 2020 EDT -> 06/29 13:47:18 2020 EDT
--------------------------------------------------------------------------------
No differences discovered
```
