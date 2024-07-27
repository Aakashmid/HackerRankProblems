
'''
Filtering emails which are valide , creating function to validate email
'''

import re
def fun(s):
    if '@' in s and '.' in s.split('@')[1]:
        username=s.split('@')[0]
        websitename,extension =s.split('@')[1].split('.')
        username_pattern = r'^[a-zA-Z0-9_-]+$'
        websitename_pattern = r'^[a-zA-Z0-9]+$'
        extension_pattern = r'^[a-zA-Z]+$'
        if re.match(username_pattern,username) and re.match(websitename_pattern,websitename) and re.match(extension_pattern,extension) and len(extension)<=3:
            return True
        else:
            return False
    else:
        return False
        
    
    
    
    # return True if s is a valid email, else return False

def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(filtered_emails)


# 5
# dheeraj-234@gmail.com
# itsallcrap
# harsh_1234@rediff.in
# kunal_shin@iop.az
# matt23@@india.in