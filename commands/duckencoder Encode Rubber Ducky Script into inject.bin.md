---
id: 833cc87a-ff3c-4127-b276-cdd7deffe305
name: duckencoder Encode Rubber Ducky Script into inject.bin
type: command
executor: ''
data: java -jar duckencoder.jar -i $PAYLOAD_FILE -o $OUTPUT_FILE
output: 'root@kali:~# java -jar duckencoder.jar -i ../Payloads/AV/EICAR-Test.txt ../Payloads/bin/inject.bin

  Hak5 Duck Encoder 2.6.3

  Loading File ..... [ OK ]

  Loading Keyboard File .... [ OK ]

  Loading Language File .... [ OK ]

  Loading DuckyScript .... [ OK ]

  DuckyScript Complete..... [ OK ]'
created_at: '2023-02-17T02:28:40.027279+00:00'
updated_at: '2023-03-13T19:50:21.945040+00:00'
---

# duckencoder Encode Rubber Ducky Script into inject.bin

```bash
java -jar duckencoder.jar -i $PAYLOAD_FILE -o $OUTPUT_FILE
```

## Expected Output

```
root@kali:~# java -jar duckencoder.jar -i ../Payloads/AV/EICAR-Test.txt ../Payloads/bin/inject.bin

Hak5 Duck Encoder 2.6.3

Loading File ..... [ OK ]
Loading Keyboard File .... [ OK ]
Loading Language File .... [ OK ]
Loading DuckyScript .... [ OK ]
DuckyScript Complete..... [ OK ]
```
