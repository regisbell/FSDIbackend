




def print_name():
    print('Regis')





def list1():
     print("Working wih lists (arrays)")

     names = ['John', 'Juan']

     names.append("Carlos")
     names.append("Charles")



     print(names[0])
     print(names[3])

     print(names)



     for x in names:
        print(x)


def list2():
    print("-" * 30)

    nums = [123,456,123,3456,6,689,23,6,8,7887,123,46,3,89,12,9,9,565,8,33,1,-200,23]


    total = 0
    for n in nums:
        total += n

    print(total)



   
    count = 0
    for num in nums:
        if(num < 50):
            print(num)
            count += 1

    print(f"There are: {count} nums lower than 50")


    for num in nums:
        if(num < 0):
            print(num)
            
    smallest = nums[0]
    for num in nums:
        if num < smallest:
            smallest = num

    print(f"The smallest in the list is: {smallest}")











def dict1():
    print("------------------Dictionary test 1")


    me = {
        "name": "Regis",
        "last": "Bell",
        "age": 32,
        "hobbies": ["reading", "listing to music"],
        "address": {
            "street": "Evergreen",
            "number": 42,
            "city": "Springfield",
        }
    }

    print( me["name"] )

    print (me["name"] + " " + me["last"])

    me['email'] = 'regi.a.bell@gmail.com'

    print( me )
    address = me["address"]
    print(f"{address['number']} {address['street']} {address['city']}")

print_name()

list1()
list2()
dict1()