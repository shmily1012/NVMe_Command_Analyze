'''
Created on Sep 20, 2017

@author: Chi.Zhang
'''
nvme_cmd_id = []
command_list = []
filename = r"ePhoenix_WRR_256Cmds_8_8_4_4_2_2_AB=1_2.txt"
if __name__ == '__main__':
    fi = open(filename, 'r')
    buf = fi.readlines()
    count = 0
    for line in buf:
        if "NVMe Cmd" in line and \
        ("OPC(Write)" in line or \
         "OPC(Read)" in line) and \
         "SQID" in line and \
         "CQID" in line and \
         "CID" in line:
            print line
            sign = 'Cmd('
            start = line.find(sign) + len(sign)
            end = line.find(')', start)
            nvme_command_id = int(line[start:end], 10)
            sign = 'SQID('
            start = line.find(sign) + len(sign)
            end = line.find(')', start)
            sqid = int(line[start:end], 10)
            sign = 'CQID('
            start = line.find(sign) + len(sign)
            end = line.find(')', start)
            cqid = int(line[start:end], 10)
            sign = 'CID('
            start = line.find(sign) + len(sign)
            end = line.find(')', start)
            cid = int(line[start:end], 10)

            command = [nvme_command_id, [sqid, cid]]
            command_list.append(command)
#             exit()
#             sqid = line[line.find('SQID('):line.find]
        elif "NVMe Cmd" in line and \
        ("OPC(Write)" in line or \
         "OPC(Read)" in line) and \
         "SQID" in line and \
         "CQID" in line:
            print line
            sign = 'Cmd('
            start = line.find(sign) + len(sign)
            end = line.find(')', start)
            nvme_command_id = int(line[start:end], 10)
            sign = 'SQID('
            start = line.find(sign) + len(sign)
            end = line.find(')', start)
            sqid = int(line[start:end], 10)
            sign = 'CQID('
            start = line.find(sign) + len(sign)
            end = line.find(')', start)
            cqid = int(line[start:end], 10)
            sign = 'CID('
            start = buf[count + 1].find(sign) + len(sign)
            end = buf[count + 1].find(')', start)
            cid = int(buf[count + 1][start:end], 10)
            
            command = [nvme_command_id, [sqid, cid]]
            command_list.append(command)

            pass
        
        count += 1
    fi.close()
    fo = open(r'C:\Users\chi.zhang\workspace\NVMe_Command_Analyze\results_%s' % filename, 'w')
    fo.write("NVM COM ID\tSQID\tCID\n")
    for com in command_list:
        fo.write("%d\t%d\t%d\n" % (com[0], com[1][0], com[1][1]))
#         print com
    fo.close()
    print 'DONE'
