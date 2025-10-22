---
id: 467be8cb-1432-4e67-86da-07cf059db230
name: Metasploit Payload Options
type: command
executor: bash
data: 'OPTIONS:

  -A        Automatically start a matching exploit/multi/handler to connect to the
  agent

  -L <opt>  Location in target host to write payload to, if none %TEMP% will be used.

  -P <opt>  Payload to use, default is windows/meterpreter/reverse_tcp.

  -S        Automatically start the agent on boot as a service (with SYSTEM privileges)

  -T <opt>  Alternate executable template to use

  -U        Automatically start the agent when the User logs on

  -X        Automatically start the agent when the system boots

  -h        This help menu

  -i <opt>  The interval in seconds between each connection attempt

  -p <opt>  The port on which the system running Metasploit is listening

  -r <opt>  The IP of the system running Metasploit listening for the connect back

  '
output: null
created_at: '2023-04-06T03:56:21.394004+00:00'
updated_at: '2023-04-10T20:24:58.396020+00:00'
---

# Metasploit Payload Options

```bash
OPTIONS:

-A        Automatically start a matching exploit/multi/handler to connect to the agent
-L <opt>  Location in target host to write payload to, if none %TEMP% will be used.
-P <opt>  Payload to use, default is windows/meterpreter/reverse_tcp.
-S        Automatically start the agent on boot as a service (with SYSTEM privileges)
-T <opt>  Alternate executable template to use
-U        Automatically start the agent when the User logs on
-X        Automatically start the agent when the system boots
-h        This help menu
-i <opt>  The interval in seconds between each connection attempt
-p <opt>  The port on which the system running Metasploit is listening
-r <opt>  The IP of the system running Metasploit listening for the connect back

```
