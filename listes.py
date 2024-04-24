Guest = ['Seb' , 'Keara' , 'Alfie' ]
#          0        1         2
print(f'{Guest[0]} you are invited to dinner with Sam')
print(f'{Guest[1]} you are invited to dinner with Sam')
print(f'{Guest[2]} you are invited to dinner with Sam')
Guest = ['Seb' , 'Keara' , 'Alfie']
Guest[2] = 'Aeris'
print(Guest)
print(f'{Guest[2]} you are invited to Sam\'s dinner because Alfie couldn\'t come')
Guest.append('Leon')
print(Guest)
Guest.append('Anand')
print(Guest)
Guest.insert(3, 'Rex')
print(Guest)
print(f'Sorry {Guest[3]}, {Guest[4]} ,{Guest[5]} ,{Guest[2]} there only allowed 2 which are Seb and Keara')
print(f'{Guest[0]} and {Guest[1]} you are still invited')
popped = []
first_popped = Guest.pop(2)
print(Guest)
second_popped = Guest.pop(2)
print(Guest)
third_popped = Guest.pop(2)
print(Guest)
fourth_popped = Guest.pop(2)
print(Guest)
del Guest[0]
print(Guest)
del Guest[0]
print(Guest)
popped.append(first_popped)

print(f' first popped => {first_popped}')
popped.append(second_popped)
print(f' second popped => {second_popped}')
popped.append(third_popped)
print(f' third popped => {third_popped}')
popped.append(fourth_popped)
print(f' fourth popped => {fourth_popped}')
print(f' Popped - {popped}')
