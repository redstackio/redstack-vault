---
id: fe0d997c-add6-4445-8067-b5d9e8e9c2fd
name: The Harvester
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:22.633845+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# The Harvester

**Command** ([[Perform lookup against with additional DNS reverse on all ranges discovered]]):

```bash
theharvester -d -c -n -b google -l 1000 [-f output]

```

**Command** ([[Example commands]]):

```bash
theharvester -d microsoft.com -l 500 -b google
theharvester -d microsoft.com -b pgp
theharvester -d microsoft -l 200 -b linkedin
theharvester -d apple.com -b googleCSE -l 500 -s 300

```
