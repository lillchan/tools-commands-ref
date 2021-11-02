# cidr notation
* https://serverfault.com/questions/12854/cidr-for-dummies
* 8 bit (octet) boundaries
    * 2 ^ 8 = 256 IPs per octet
    * 4 octets * 8 bits = 32 bit integer (IPv4 address)
* calculate the # of IPs for /27:
    * 32 - 27 = 5
    * 2 ^ 5 = 224
    * 256 - 224 = 32 IPs available
* /32 means 1 IP available

```
CIDR    Dotted Quad
/24     255.255.255.0
/25     255.255.255.128
/26     255.255.255.192
/27     255.255.255.224
/28     255.255.255.240
/29     255.255.255.248
/30     255.255.255.252
/31     255.255.255.254
/32     255.255.255.255
```