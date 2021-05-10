# Day Three Class Notes
# Hash Tables can be useful in problems that need a quick searches with large amounts of data
# The sorting (or something else) can be done ahead of time just once instead of each time

records = [
    ('Alice', 'Engineering'),
    ('Bob', 'Sales'),
    ('Carol', 'Sales'),
    ('Sarah', 'Sales'),
    ('Pranjal', 'Sales'),
    ('Dave', 'Engineering'),
    ('Erin', 'Engineering'),
    ('Frank', 'Engineering'),
    ('Grace', 'Marketing'),
    ('Charles', 'Marketing'),
    ('Brian', 'Marketing'),
    ('Jordan', 'Marketing')
]

# Need to print all departments
# Need to print everyone in Engineering

# Proposed Dictionary
#   Keys: Departments
#   Values: Array of names

# This function is O(n)
#
def build_index(recs):
    index = {}

    for record in recs:
        name, dept = record

        # Check if department is already in index
        if dept in index:
            # If it is, add name to list
            index[dept].append(name)
        # If not create new key with list with the name in it
        else:
            index[dept] = [name]

    return index

department_index = build_index(records)

print(department_index.keys())
print(department_index["Engineering"])  # This will be O(1) no matter what key is used (but uses more space)




# Your code here


def slowfun_too_slow(x, y):
    v = math.pow(x, y)
    v = math.factorial(v)
    v //= (x + y)
    v %= 982451653

    return v

def slowfun(x, y):
    """
    Rewrite slowfun_too_slow() in here so that the program produces the same
    output, but completes quickly instead of taking ages to run.
    """
    # Your code here



# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
