---
id: ee21a1e4-4c9c-410f-8236-1ac9ae8abf1f
name: Copy PrtToCertmaster.zip to destination and extract it
type: command
executor: bash
data: 'Copy-Item -ToSession $jumpvm -Path C:\Tools\PrtToCertmaster.zip -Destination
  C:\Users\Username\Documents\username –Verbose

  Expand-Archive -Path C:\Users\Username\Documents\username\PrtToCert-master.zip -DestinationPath
  C:\Users\Username\Documents\username\PrtToCert'
output: null
created_at: '2023-04-06T03:56:15.747822+00:00'
updated_at: '2023-05-25T18:35:34.917738+00:00'
---

# Copy PrtToCertmaster.zip to destination and extract it

```bash
Copy-Item -ToSession $jumpvm -Path C:\Tools\PrtToCertmaster.zip -Destination C:\Users\Username\Documents\username –Verbose
Expand-Archive -Path C:\Users\Username\Documents\username\PrtToCert-master.zip -DestinationPath C:\Users\Username\Documents\username\PrtToCert
```
