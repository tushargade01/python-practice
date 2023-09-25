guest_list = ['shubham','sandip','anand','vinod']
print(f'{guest_list[0].title()} Please come to dinner')
print(f'{guest_list[1].title()} Please come to dinner')
print(f'{guest_list[2].title()} please come to dinner')
print(f'{guest_list[3].title()} please come to dinner')

#one guest not come then modify list old guest with new guest name

guest_list[2] = 'pratap'
print('\nafter modify list\n')

print(f'{guest_list[0].title()} Please come to dinner')
print(f'{guest_list[1].title()} Please come to dinner')
print(f'{guest_list[2].upper()} please come to dinner')
print(f'{guest_list[3].title()} please come to dinner')

#add more guest

guest_list.insert(0,'ganesh')
guest_list.insert(3,'tushar')
guest_list.append('rohan')

print('\n after adding more geust in list\n')

print(f'{guest_list[0].upper()} Please come to dinner')
print(f'{guest_list[1].title()} Please come to dinner')
print(f'{guest_list[2].upper()} please come to dinner')
print(f'{guest_list[3].upper()} please come to dinner')
print(f'{guest_list[4].title()} please come to dinner')
print(f'{guest_list[5].title()} Please come to dinner')
print(f'{guest_list[6].upper()} please come to dinner')
