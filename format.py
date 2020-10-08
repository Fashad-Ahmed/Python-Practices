pet_name = ['mox','tom','bruno']
pet_type = ['cat','kitten','bulldog']

for i in range(len(pet_name)):
    out = "{} is a {}"
    print(out.format(pet_name[i],pet_type[i]))