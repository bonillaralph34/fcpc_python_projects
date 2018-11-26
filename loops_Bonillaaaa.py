print("Multlipication Table")

print ("\tBy 2's")
for a in range (2,25,2):
    print(a)
print ("\tBy 3's")
for x in range (3,37,3):
    print(x)
print ("\tBy 4's")
for y in range (4,49,4):
    print(y)
print ("\tBy 12's")
for z in range (12,145,12):
    print(z)

#nested loop sample
print("\nMultliplication Table by 10 to 20!")
for a in range(10,21):
    for b in range(1,11):
        print(a*b,end='\t')
    print()
