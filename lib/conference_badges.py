def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    
    l = []

    for name in names:
        l.append(f"Hello, my name is {name}.")

    return l

# batch_badge_creator(names)

def assign_rooms(names):
    
    l = []
    num = 1

    for name in names:
        l.append(f"Hello, {name}! You'll be assigned to room {num}!")
        num += 1
    
    return l

# assign_rooms(names)
# names = ["Guido", "Edsger", "Ada", "Charles", "Alan", "Grace", "Linus", "Matz"]

def printer(names):
    
    for badge in batch_badge_creator(names):
        print(badge)
    
    for assignment in assign_rooms(names):
        print(assignment)


# printer(names)