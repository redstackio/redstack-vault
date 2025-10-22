---
id: 0666723e-a2f9-4418-9f98-e700bf16be89
name: Bash History
type: technique
mitre_id: T1139
mitre_url: null
created_at: '2019-08-28T21:17:41.178725+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Credential Access|TA0006 - Credential Access]]'
procedures:
- '[[DB2 Injection with Comment Filtering]]'
- '[[NoSQL Injection Password Length Extraction]]'
- '[[SQLite Schema Extraction]]'
---

# Bash History

**MITRE ID**: T1139

## Description

Bash keeps track of the commands users type on the command-line with the "history" utility. Once a user logs out, the history is flushed to the user’s .bash_history file. For each user, this file resides at the same location: ~/.bash_history. Typically, this file keeps track of the user’s last 500 commands. Users often type usernames and passwords on the command-line as parameters to programs, which then get saved to this file when they log out. Attackers can abuse this by looking through the file for potential credentials. [1]

# Detection

Monitoring when the user's .bash_history is read can help alert to suspicious activity. While users do typically rely on their history of commands, they often access this history through other utilities like "history" instead of commands like cat ~/.bash_history.

# Mitigation

There are multiple methods of preventing a user's command history from being flushed to their .bash_history file, including use of the following commands:set +o history and set -o history to start logging again;unset HISTFILE being added to a user's .bash_rc file; andln -s /dev/null ~/.bash_history to write commands to /dev/nullinstead.

# Footnotes

[1] Alex Rymdeko-Harvey, Steve Borosh. (2016, May 14). External to DA, the OS X Way. Retrieved July 3, 2017.

## Defense

There are multiple methods of preventing a user's command history from being flushed to their .bash_history file, including use of the following commands:
<code>set +o history</code> and <code>set -o history</code> to start logging again;
<code>unset HIST

## Tactics

- [[Credential Access|TA0006 - Credential Access]]

## Related Procedures (3)

- [[DB2 Injection with Comment Filtering]]
- [[NoSQL Injection Password Length Extraction]]
- [[SQLite Schema Extraction]]
