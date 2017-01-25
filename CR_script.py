#!/usr/bin/env python3

# external modules
import re

# my modules
import DCC
import Config as CF
import Tree
import MyUtil

s = DCC.login(CF.dcc_url + CF.dcc_login)

top_collection = 'Collection-4325'

while True:
    cr_coll = input('\n>>>> Enter a Collection number (e.g. 1234) or Q to quit: ')

    if 'Q' in cr_coll.upper():
        print('\n\n....Quitting')
        exit(0)
        
#     if 'L' in cr_coll.upper():
#         print('\n\n....Listing Collections')
#         tree = Tree.get_tree(s, top_collection)
#         Tree.print_tree(s,tree)
#         break

    cr_coll = 'Collection-' + cr_coll
    print('\n')
    fd = DCC.prop_get(s, cr_coll, InfoSet = 'CollData')
    fd['parents'] = DCC.prop_get(s, cr_coll, InfoSet = 'Parents')
    DCC.print_coll_data(fd)
    DCC.print_parents(fd['parents'])
    
    print('\n')    
    ans = input('>>>> Is this the correct collection? (Y/N):')
    if ans.upper() == 'Y':        
        p = re.compile('CR\d+')
        # print(p.match(fd['title']))
        crnum = p.match(fd['title'])
        crnum = crnum.group()
        print(crnum)

        list = [{'chandle':'Collection-14278', 'cname':'0.0 Change Control Requests - CR Pre-SE Acceptance','keyword':'CR - Pre-SE Acceptance'},
                {'chandle':'Collection-14086', 'cname':'1.1 Change Control Requests - CR Initiated - CCB','keyword':'CR - Initiated - CCB'},
                {'chandle':'Collection-14087', 'cname':'1.2 Change Control Requests - CR Initiated - No CCB','keyword':'CR - Initiated - No CCB'},
                {'chandle':'Collection-12030', 'cname':'2.0 Change Control Requests - CR Evaluation','keyword':'CR - Evaluation'},
                {'chandle':'Collection-12032', 'cname':'3.0 Change Control Requests - CCB','keyword':'CR - CCB'},
                {'chandle':'Collection-12033', 'cname':'4.0 Change Control Requests - CR Implementation ','keyword':'CR - Implementation'},     
                {'chandle':'Collection-1004', 'cname':'5.0 Change Control Requests - CR Archive','keyword':'CR - Archived'},      
                ]
        
        idx = 0   
        for l in list:
            print('[',idx,'] : ', l['cname'])
            idx = idx + 1
   
        ans = input('\n>>>> Choose a new location for the Collection [1-6] or Q:')
        if 'Q' in ans.upper():
            print('\n\n....Not making any changes')  
        else:
            # Remove collection from all change control collections
            ansnum = int(ans)
            dest = list[ansnum]['chandle']
            for l in list:
                for p in fd['parents']:
                    if p[0] == l['chandle']:
                        if dest != l['chandle']: # don't move if it's already in the desired collection
                            DCC.dcc_move(s, cr_coll, l['chandle'], dest)
            # Set keywords
            DCC.set_metadata(s, cr_coll, Keywords = crnum + ': ' + list[ansnum]['keyword'])        
            DCC.set_metadata(s, cr_coll, Summary = crnum + ': ' + list[ansnum]['keyword'])   
        
        print('\n')
        fd = DCC.prop_get(s, cr_coll, InfoSet = 'CollData')
        fd['parents'] = DCC.prop_get(s, cr_coll, InfoSet = 'Parents')
        DCC.print_coll_data(fd)
        DCC.print_parents(fd['parents'])

                  