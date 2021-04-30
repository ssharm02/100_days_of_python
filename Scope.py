################### Scope ####################

enemies = 1


def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")


player_health = 10


def game():
    # drink potion is local scope of game
    def drink_potion():
        potion_strength = 2
        print("Player health ")
        print(player_health)
        print(potion_strength)


# print(drink_potion())


"""Global space applies to functions as - namespace"""

game_level = 3


def create_enemy():
    enemies = ["Skeleton", "Zombie", "Alien"]
    if game_level < 5:
        new_enemy = enemies[0]

    # print(new_enemy)


# modifying global scope - dont call local and global variables the same name

enemies = 1


def increase_enemies():
    # this is a new variable
    # modifying global variables
    global enemies
    enemies += 1
    print(f"enemies inside function {enemies}")
    # can also return
    return enemies + 1


enemies = increase_enemies()
increase_enemies()
print(f"enemies outside function {enemies}")


"""Global constants """


PI = 3.14159

def calculate():
    # do something with PI
    PI
