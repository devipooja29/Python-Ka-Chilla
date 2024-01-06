# # While loops and for loops

# # While loop
# x=0
# while (x<=5):
#     print(x)
#     x=x+1

# # For loop
# for x in range(5,10):
#     print(x)

days = ["Monday", "Tuesday", "Wednesday", "Thrusday", "Friday", "Saturday", "Sunday"]

for d in days:
    # if (d=="Friday"):break #Loop stops
    if (d=="Friday"): continue # Skils friday
    print(d)