'''
Created on Sep 13, 2018

@author: Chi.Zhang
'''
################################################################
filename = r"AQ_WRR.txt"
SQ1_base_adr = 0x40e149000
################################################################
SQ2_base_adr = SQ1_base_adr + 0x10000
SQ3_base_adr = SQ2_base_adr + 0x10000
SQ4_base_adr = SQ3_base_adr + 0x10000
SQ5_base_adr = SQ4_base_adr + 0x10000
SQ6_base_adr = SQ5_base_adr + 0x10000
SQ7_base_adr = SQ6_base_adr + 0x10000
SQ8_base_adr = SQ7_base_adr + 0x10000
SQ9_base_adr = SQ8_base_adr + 0x10000
################################################################
packets_array = list()
if __name__ == '__main__':
    fi = open(filename, 'r')
    buf = fi.readlines()
    fi.close()
    count = 0
    line_id = 0
#     for line in buf:
    while line_id < len(buf):
#     while line_id < 10000:
        if 'Upstream' in buf[line_id] and 'Mem MRd' in buf[line_id] and 'Split Tra' in buf[line_id]:
            print(buf[line_id])
            Split_ID = 0
            SQ_ID = 0
            number_of_cmds_in_packet = 0
            try:
                start = buf[line_id].index('Split Tra(') + len('Split Tra(')
            except ValueError:
                print(buf[line_id])
                exit(-1)
            end = buf[line_id].index(')', start + 1)
            Split_ID = int(buf[line_id][start:end], 10)
            for i in range(10):
                if 'Address' in buf[line_id + i]:
                    address = 0x0
                    start = buf[line_id + i].index('Address(') + len('Address(')
                    end = buf[line_id + i].index(')', start + 1)
                    if ':' in buf[line_id + i][start:end]:
                        temp = buf[line_id + i][start:end].split(':')
                        high_adr = int(temp[0], 16)
                        low_adr = int(temp[1], 16)
                        address = (high_adr << 32) | low_adr
                    else:
                        address = int(buf[line_id + i][start:end], 16)
                    
#                     print 'address = 0x%x' % address
                    break
            if address & 0xFFFFFFFFFFFF0000 == SQ1_base_adr:
                SQ_ID = 1
            elif address & 0xFFFFFFFFFFFF0000 == SQ2_base_adr:
                SQ_ID = 2
            elif address & 0xFFFFFFFFFFFF0000 == SQ3_base_adr:
                SQ_ID = 3
            elif address & 0xFFFFFFFFFFFF0000 == SQ4_base_adr:
                SQ_ID = 4
            elif address & 0xFFFFFFFFFFFF0000 == SQ5_base_adr:
                SQ_ID = 5
            elif address & 0xFFFFFFFFFFFF0000 == SQ6_base_adr:
                SQ_ID = 6
            elif address & 0xFFFFFFFFFFFF0000 == SQ7_base_adr:
                SQ_ID = 7
            elif address & 0xFFFFFFFFFFFF0000 == SQ8_base_adr:
                SQ_ID = 8
            elif address & 0xFFFFFFFFFFFF0000 == SQ9_base_adr:
                SQ_ID = 9
            else:
                SQ_ID = None
#                 print 'unknown adrress = 0x%x' % address
#                 exit(-1)
            if SQ_ID != None:
                for i in range(10):
#                     print buf[line_id + i]
                    if 'Data(' in buf[line_id + i]:
                        start = buf[line_id + i].index('Data(') + len('Data(')
                        end = buf[line_id + i].index('B', start + 1)
                        number_of_cmds_in_packet = (int(buf[line_id + i][start:end], 10) / 64)
                        break
                for i in range(number_of_cmds_in_packet):
                    packet = {'split_id':Split_ID, 'sq_id':SQ_ID}
                    packets_array.append(packet)
#             print buf[line_id]
#             print buf[line_id + 1]
#             print buf[line_id + 2]
#             print buf[line_id + 3]
#             print buf[line_id + 4]
#             print buf[line_id + 5]
#             print buf[line_id + 6]
#             print buf[line_id + 7]
            
        line_id += 1
    for packet in packets_array:
        print(packet)
    fo = open(r'results_%s' % filename, 'w')
    fo.write("split_id\tSQID\n")
    for packet in packets_array:
        fo.write("%d\t%d\n" % (packet['split_id'], packet['sq_id']))
    fo.close()
    print('DONE')
