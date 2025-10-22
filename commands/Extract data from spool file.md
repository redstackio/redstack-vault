---
id: 873ea4a7-ec53-47dd-8df5-008c9c8ada2b
name: Extract data from spool file
type: command
executor: bash
data: "SPOOL spoolfile.txt; \nSELECT * FROM employees; \nSPOOL OFF;"
output: null
created_at: '2023-04-06T03:56:07.618745+00:00'
updated_at: '2023-04-10T20:36:05.391024+00:00'
---

# Extract data from spool file

```bash
SPOOL spoolfile.txt; 
SELECT * FROM employees; 
SPOOL OFF;
```
