from scapy.all import *
import scapy

offers = []


def options(dhcp_options, key):
    try:
        return filter(lambda x: x[0] == key, dhcp_options)[0][1]
    except:
        pass


def on_packet(packet):
    if DHCP in packet and packet[BOOTP].xid == client_xid:
        message_type = packet[DHCP].options[0][1]
        if message_type == 2:
            offer = {
                "server_mac": packet[Ether].src,
                "server_ip": packet[IP].src,
                "offered_ip": packet[BOOTP].yiaddr,
            }
            offers.append(offer)



if __name__ == '__main__':
    conf.iface = 'eth1'
    conf.checkIPaddr = False
    mac = get_if_hwaddr(conf.iface)
    fam, hw = get_if_raw_hwaddr(conf.iface)
    client_xid = 100
    print(mac, fam, hw)


    ethernet = Ether(dst='ff:ff:ff:ff:ff:ff', src=hw, type=0x800)
    ip = IP(src='0.0.0.0', dst='255.255.255.255')
    udp = UDP(sport=68, dport=67)
    bootp = BOOTP(xid=client_xid, flags=32768, op=1, chaddr=hw)
    dhcp = DHCP(options=[("message-type", "discover"), ("hostname", "server-01"), ('end')])
    packet = ethernet / ip / udp / bootp / dhcp

    sendp(packet, iface=conf.iface)

    sniff(prn=on_packet, store=0, count=1, timeout=10, iface=conf.iface, filter="udp and src port 67 and dst port 68")

    if len(offers) != 0:
        print(offers[0])

