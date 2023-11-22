import random


def generate_password(length: int) -> str:
    password_list = []

    for i in range(length):
        pick_index = random.randrange(0, 3)

        match pick_index:
            case 0:
                char = random.choice('abcdefghijklmnopqrstuvwxyz')

                if random.randrange(1, 3) == 1:
                    char = char.upper()
                else:
                    char = char.lower()

                password_list.append(char)

            case 1:
                password_list.append(f"{random.randint(0, 10)}")

            case 2:
                password_list.append(random.choice(' _-@#$%^&*!?.,=+'))

    return ''.join(password_list)


# run
print(f"{generate_password(26)}")