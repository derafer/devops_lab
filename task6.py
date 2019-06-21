mask_number = int(input("How many mask? "))
masks = []

for i in range(mask_number):
    masks += [input().split(".")]
ip_pairs = int(input("How many addresses pairs? "))

for i in range(ip_pairs):
    commons = 0
    ip_addr1, ip_addr2 = input().split()
    ip_raw1 = ip_addr1.split(".")
    ip_raw2 = ip_addr2.split(".")
    for j in range(mask_number):
        full_leng1 = ("{0}{1}{2}{3}".format(format(int(ip_raw1[0]), '08b'),
                                            format(int(ip_raw1[1]), '08b'),
                                            format(int(ip_raw1[2]), '08b'),
                                            format(int(ip_raw1[3]), '08b')))
        full_leng2 = ("{0}{1}{2}{3}".format(format(int(ip_raw2[0]), '08b'),
                                            format(int(ip_raw2[1]), '08b'),
                                            format(int(ip_raw2[2]), '08b'),
                                            format(int(ip_raw2[3]), '08b')))
        full_mask = ("{0}{1}{2}{3}".format(format(int(masks[j][0]), '08b'),
                                           format(int(masks[j][1]), '08b'),
                                           format(int(masks[j][2]), '08b'),
                                           format(int(masks[j][3]), '08b')))
        lengs = int(full_mask.count("1"))
        full_leng1 = int(full_leng1[0:lengs])
        full_leng2 = int(full_leng2[0:lengs])
        full_mask = int(full_mask[0:lengs])
        if full_leng1 == full_leng2:
            commons += 1
    print(commons)
