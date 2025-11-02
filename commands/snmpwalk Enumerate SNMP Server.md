---
id: 7236f3bd-a6a2-4df0-9604-c3b517eb9a2c
name: snmpwalk Enumerate SNMP Server
type: command
executor: bash
data: snmpwalk -c $_COMMUNITY_STRING -v $_VERSION $_TARGET_IP
output: "root@kali:~# snmpwalk -c public -v1 10.10.10.10\nCreated directory: /var/lib/snmp/mib_indexes\n\
  SNMPv2-MIB::sysDescr.0 = STRING: Linux Host 4.4.0-75-generic #96~14.04.1-Ubuntu\
  \ SMP Thu Apr 20 11:\n06:56 UTC 2017 i686                               \nSNMPv2-MIB::sysObjectID.0\
  \ = OID: NET-SNMP-MIB::netSnmpAgentOIDs.10\nDISMAN-EVENT-MIB::sysUpTimeInstance\
  \ = Timeticks: (38145) 0:06:21.45\nSNMPv2-MIB::sysContact.0 = STRING: root\n...\n\
  ...\nDISMAN-EVENT-MIB::mteEventNotificationObjects.\"_snmpd\".'_linkUp' = STRING:\
  \ _linkUpDown\nDISMAN-EVENT-MIB::mteEventNotificationObjects.\"_snmpd\".'_mteTriggerFailure'\
  \ = STRING: _triggerFail\nDISMAN-EVENT-MIB::mteEventNotificationObjects.\"_snmpd\"\
  .'_mteTriggerFalling' = STRING: _triggerFire\nDISMAN-EVENT-MIB::mteEventNotificationObjects.\"\
  _snmpd\".'_mteTriggerFired' = STRING: _triggerFire\nDISMAN-EVENT-MIB::mteEventNotificationObjects.\"\
  _snmpd\".'_mteTriggerRising' = STRING: _triggerFire\nNOTIFICATION-LOG-MIB::nlmConfigGlobalEntryLimit.0\
  \ = Gauge32: 1000\nNOTIFICATION-LOG-MIB::nlmConfigGlobalAgeOut.0 = Gauge32: 1440\
  \ minutes\nNOTIFICATION-LOG-MIB::nlmStatsGlobalNotificationsLogged.0 = Counter32:\
  \ 0 notifications\nNOTIFICATION-LOG-MIB::nlmStatsGlobalNotificationsBumped.0 = Counter32:\
  \ 0 notifications"
created_at: '2019-09-17T00:51:23.953583+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
tools:
- '[[host]]'
- '[[snmpwalk]]'
---

# snmpwalk Enumerate SNMP Server

```bash
snmpwalk -c $_COMMUNITY_STRING -v $_VERSION $_TARGET_IP
```

## Expected Output

```
root@kali:~# snmpwalk -c public -v1 10.10.10.10
Created directory: /var/lib/snmp/mib_indexes
SNMPv2-MIB::sysDescr.0 = STRING: Linux Host 4.4.0-75-generic #96~14.04.1-Ubuntu SMP Thu Apr 20 11:
06:56 UTC 2017 i686                               
SNMPv2-MIB::sysObjectID.0 = OID: NET-SNMP-MIB::netSnmpAgentOIDs.10
DISMAN-EVENT-MIB::sysUpTimeInstance = Timeticks: (38145) 0:06:21.45
SNMPv2-MIB::sysContact.0 = STRING: root
...
...
DISMAN-EVENT-MIB::mteEventNotificationObjects."_snmpd".'_linkUp' = STRING: _linkUpDown
DISMAN-EVENT-MIB::mteEventNotificationObjects."_snmpd".'_mteTriggerFailure' = STRING: _triggerFail
DISMAN-EVENT-MIB::mteEventNotificationObjects."_snmpd".'_mteTriggerFalling' = STRING: _triggerFire
DISMAN-EVENT-MIB::mteEventNotificationObjects."_snmpd".'_mteTriggerFired' = STRING: _triggerFire
DISMAN-EVENT-MIB::mteEventNotificationObjects."_snmpd".'_mteTriggerRising' = STRING: _triggerFire
NOTIFICATION-LOG-MIB::nlmConfigGlobalEntryLimit.0 = Gauge32: 1000
NOTIFICATION-LOG-MIB::nlmConfigGlobalAgeOut.0 = Gauge32: 1440 minutes
NOTIFICATION-LOG-MIB::nlmStatsGlobalNotificationsLogged.0 = Counter32: 0 notifications
NOTIFICATION-LOG-MIB::nlmStatsGlobalNotificationsBumped.0 = Counter32: 0 notifications
```


