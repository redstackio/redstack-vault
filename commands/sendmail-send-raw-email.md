---
data: /usr/sbin/sendmail -t < email.txt
tags:
  - email
  - sendmail
type: command
executor: bash
platforms:
  - Linux
id: 25030657-225c-465f-b6b9-53ce030be555
created_at: '2025-12-14T00:11:16.810Z'
updated_at: '2025-12-14T00:11:16.810Z'
verified: false
validated: true
submitted: true
---
# sendmail-send-raw-email

## Command

```bash
/usr/sbin/sendmail -t < email.txt
```

## Description

This command sends a raw email from a text file using sendmail, extracting recipients from the message headers. It's used to deliver malicious raw HTML emails without modification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-t` | Extract recipients from message headers | Yes |
| `< email.txt` | Input redirection to read from email.txt file | Yes |

## Examples

### Basic Usage

```bash
/usr/sbin/sendmail -t < email.txt
```

### Advanced Usage

```bash
/usr/sbin/sendmail -t -f attacker@example.com < email.txt
```

## Expected Output

No output if successful; the email is sent to the recipient.

## Related

- [[procedures/Send-Raw-Email-Using-Sendmail]]
- [[tools/sendmail]]
