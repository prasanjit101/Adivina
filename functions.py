import random
import string

n=5

res=''.join(random.choices(string.ascii_uppercase+string.ascii_lowercase+string.digits,k=n))

print(str(res))