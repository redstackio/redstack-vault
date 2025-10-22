---
id: 3ad52d85-86ec-4ed1-ac32-b5df603e8dc4
name: Filtering Data using MongoDB Query Operators
type: command
executor: bash
data: 'username[$ne]=toto&password[$ne]=toto

  login[$regex]=a.*&pass[$ne]=lol

  login[$gt]=admin&login[$lt]=test&pass[$ne]=1

  login[$nin][]=admin&login[$nin][]=test&pass[$ne]=toto'
output: null
created_at: '2023-04-06T03:56:31.414995+00:00'
updated_at: '2023-04-10T20:23:01.283847+00:00'
---

# Filtering Data using MongoDB Query Operators

```bash
username[$ne]=toto&password[$ne]=toto
login[$regex]=a.*&pass[$ne]=lol
login[$gt]=admin&login[$lt]=test&pass[$ne]=1
login[$nin][]=admin&login[$nin][]=test&pass[$ne]=toto
```
