'''
Created on Aug 28, 2017

@author: Chi.Zhang
'''


import os
import linecache

sq_command_id_list = []
cq_command_id_list = []
if __name__ == '__main__':
    
#     a = ['1', '2', '3', '4', '2']
#     b = ['1', '6', '2', '3']
#     for cq_id in b:
#         id = 0
#         while True:
#             if cq_id == a[id]:
#                 del a[id]
#                 break
#             else:
#                 id += 1
#             
#             if id >= len(a):
#                 break
#                 
# 
#     print (a)
#     exit()
    str = open("warming129_8g_trim.txt", 'r')
    
#     buffer = str.readlines(1024 * 1024 * 8)
    buffer = str.readlines()
    print ('lines = ', len(buffer))
    count = 0
    while True:
#         print buffer[count]
        if "Split Tra(" in buffer[count]:
            
#             print ('sq')
#             print buffer[count + 4]
#             print (buffer[count + 4][6:10])
            if ':' in buffer[count + 4][6:10]:
#                 print buffer[count + 4]
                count += 1
            else:
                temp = []
                start = buffer[count].find("(")
                end = buffer[count].find(')')
                temp.append(buffer[count + 4][6:10])
                temp.append(buffer[count][start:end + 1])
#                 sq_command_id_list.append(buffer[count + 4][6:10])
                sq_command_id_list.append(temp)
                count += 4
        elif "Link Tra(" in buffer[count]:     
#             print ('cq')
#             print buffer[count + 3]
#             print (buffer[count + 3][45:49])

            if ':' in buffer[count + 3][45:49]:
#                 print buffer[count + 3]
                count += 1
            else:
                cq_command_id_list.append(buffer[count + 3][45:49])
#                 if buffer[count + 3][45:49] == '00AF':
#                     print 'count = ', count
#                     exit()
                count += 3
#         print line
        else:
            count += 1
        if count >= len(buffer):
#         if count >= 1000:
            break
    str.close()
    print ('cq and sq cid is done.')
    
#     exit()
    len_cq_command_id_list = len(cq_command_id_list)
    print 'num of cq is', len_cq_command_id_list
    print 'num of sq is', len(sq_command_id_list)
    cq_id = 0
    for cq_id in cq_command_id_list:
        id = 0
#         if (cq_id % 100) == 0:
#             print 'status = %d/%d' % (cq_id, len_cq_command_id_list)
        while True:
            if cq_id == sq_command_id_list[id][0]:
                del sq_command_id_list[id]
                break
            else:
                
                id += 1
            
            if id >= len(sq_command_id_list):
                break
                
#         cq_id += 1
    for en in sq_command_id_list:
        print en
#     print (sq_command_id_list)
    
    pass


#     fi = open("test.txt", 'r')
#     buf = fi.readlines()
#     for line in buf:
#         if "__ 0:" in line:
# #             print line[13]
#             if line[13] == '1' or line[13] == '2':
#                 sq_command_id_list.append(line[6:10])
#          
#     fi.close()
#     print 'sq_command is done'
# #     print sq_command_id_list
#     fo = open("test_CQ.txt", 'r')
#     buf = fo.readlines()
#     for line in buf:
#         if "_______| Data" in line:
#             cq_command_id_list.append(line[45:49])
# #             print line[45:49]
#     fo.close()
#     print 'cq_command is done'
#     
#     for sq_id in sq_command_id_list:
#         id = cq_command_id_list.index(sq_id)
#         if id == -1:
#             print sq_id
# #         print id
#     print 'everything is done'
#     fi = open("test_all.txt", 'r')
#     buf = fi.readlines()
#     count = 0
#     for line in buf:
#         print line
#         count += 1
#         if count == 100:
#             break
