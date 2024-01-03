from faker import Faker
import random
f=Faker()
def get_user():
    return {
        'user_name':f.name(),
        'address': f.address(),
        'phone_number': random.randint(1111111111,9999999999),
        'age': random.randint(15,90),
        'Birthday': str(random.randint(1,13))+'-'+str(random.randint(1,29)),
        'email': f.email(),
        'region': random.randint(1,8),
        'Rating': random.randint(1,5)
    }
if __name__=='__main__':
    print(get_user())