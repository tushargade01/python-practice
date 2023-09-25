def build_profile(first, last, **user_info):
    user_info['fist_name'] = first
    user_info['last_name'] = last
    
    return user_info


user_profile = build_profile('tushar','gade',age = '20',gender = 'male')
print(user_profile)    