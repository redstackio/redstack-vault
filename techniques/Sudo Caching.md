---
id: 8ab18f3c-6e8b-4bce-a008-082e6bbf8d53
name: Sudo Caching
type: technique
mitre_id: T1206
mitre_url: null
created_at: '2019-08-28T21:17:26.509112+00:00'
updated_at: '2023-05-29T16:48:53.672970+00:00'
tactics:
- '[[Privilege Escalation|TA0004 - Privilege Escalation]]'
procedures:
- '[[HQL List Columns Injection]]'
---

# Sudo Caching

**MITRE ID**: T1206

## Description

The sudo command "allows a system administrator to delegate authority to give certain users (or groups of users) the ability to run some (or all) commands as root or another user while providing an audit trail of the commands and their arguments." [1] Since sudo was made for the system administrator, it has some useful configuration features such as a timestamp_timeout that is the amount of time in minutes between instances of sudo before it will re-prompt for a password. This is because sudo has the ability to cache credentials for a period of time. Sudo creates (or touches) a file at /var/db/sudo with a timestamp of when sudo was last run to determine this timeout. Additionally, there is a tty_tickets variable that treats each new tty (terminal session) in isolation. This means that, for example, the sudo timeout of one tty will not affect another tty (you will have to type the password again).Adversaries can abuse poor configurations of this to escalate privileges without needing the user's password. /var/db/sudo's timestamp can be monitored to see if it falls within the timestamp_timeout range. If it does, then malware can execute sudo commands without needing to supply the user's password. When tty_tickets is disabled, adversaries can do this from any tty for that user. The OSX Proton Malware has disabled tty_tickets to potentially make scripting easier by issuing echo \'Defaults !tty_tickets\' >> /etc/sudoers  [2]. In order for this change to be reflected, the Proton malware also must issue killall Terminal. As of macOS Sierra, the sudoers file has tty_tickets enabled by default.

# Detection

This technique is abusing normal functionality in macOS and Linux systems, but sudo has the ability to log all input and output based on the LOG_INPUT and LOG_OUTPUT directives in the /etc/sudoers file.

# Mitigation

Setting the timestamp_timeout to 0 will require the user to input their password every time sudo is executed. Similarly, ensuring that the tty_tickets setting is enabled will prevent this leakage across tty sessions.

# Footnotes

[1] Todd C. Miller. (2018). Sudo Man Page. Retrieved March 19, 2018.

[2] Amit Serper. (2018, May 10). ProtonB What this Mac Malware Actually Does. Retrieved March 19, 2018.

[3] Patrick Wardle. (n.d.). Mac Malware of 2017. Retrieved September 21, 2018.

## Defense

Setting the <code>timestamp_timeout</code> to 0 will require the user to input their password every time <code>sudo</code> is executed. Similarly, ensuring that the <code>tty_tickets</code> setting is enabled will prevent this leakage across tty sessions.

## Tactics

- [[Privilege Escalation|TA0004 - Privilege Escalation]]

## Related Procedures (1)

- [[HQL List Columns Injection]]
