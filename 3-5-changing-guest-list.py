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