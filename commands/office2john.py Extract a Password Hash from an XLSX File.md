---
id: 56531108-238d-46f1-9cd1-64b961db8dc7
name: office2john.py Extract a Password Hash from an XLSX File
type: command
executor: bash
data: office2john.py $_TARGET_FILE.xslx
output: "root@kali:/usr/share/john# ./office2john.py /tmp/ccinfo.xlsx \nccinfo.xlsx:$office$*2013*100000*256*16*7a8978075d68abb1546e84564ba4e6f7*80c87564a5f646a2e6f8d2e74653e225*08dd6485a452b6c8456c5468321aa10cb548a5aee64264cc68456b68d6826a5d"
created_at: '2020-06-25T21:07:47.240186+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# office2john.py Extract a Password Hash from an XLSX File

```bash
office2john.py $_TARGET_FILE.xslx
```

## Expected Output

```
root@kali:/usr/share/john# ./office2john.py /tmp/ccinfo.xlsx 
ccinfo.xlsx:$office$*2013*100000*256*16*7a8978075d68abb1546e84564ba4e6f7*80c87564a5f646a2e6f8d2e74653e225*08dd6485a452b6c8456c5468321aa10cb548a5aee64264cc68456b68d6826a5d
```


