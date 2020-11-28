import random

action_map = {
    "rock": 1,
    "paper": 2,
    "scissors": 3,
}
inverse_action_map = {v: k for k, v in action_map.items()}


def generate_computer_action() -> int:
    return random.randint(1, 3)


def generate_result(user_input: str, computer_action: int) -> str:
    user_action = action_map.get(user_input)
    computer_input = inverse_action_map.get(computer_action)
    draw_msg = f"User played {user_input} and Computer played {computer_input}. It is a tie"
    user_won_msg = f"User played {user_input} and Computer played {computer_input}. You won."
    user_lost_msg = f"User played {user_input} and Computer played {computer_input}. You lost."

    if user_action is None:
        return f"{user_input} is an invalid option!"

    if user_action == computer_action:
        return draw_msg
    elif user_action == 3 and computer_action == 2:
        return user_won_msg
    elif user_action == 2 and computer_action == 1:
        return user_won_msg
    elif user_action == 1 and computer_action == 3:
        return user_won_msg
    else:
        return user_lost_msg


if __name__ == "__main__":
    # Tests
    # print(generate_result("bad input", action_map.get("rock")))
    # print(generate_result("rock", action_map.get("rock")))
    # print(generate_result("rock", action_map.get("paper")))
    # print(generate_result("rock", action_map.get("scissors")))
    # print(generate_result("paper", action_map.get("rock")))
    # print(generate_result("paper", action_map.get("paper")))
    # print(generate_result("paper", action_map.get("scissors")))
    # print(generate_result("scissors", action_map.get("rock")))
    # print(generate_result("scissors", action_map.get("paper")))
    # print(generate_result("scissors", action_map.get("scissors")))
    print("Welcome to the rock-paper-scissors game, please enter q to quit.")
    while True:
        print("Please enter rock, paper, or scissors:")
        user_input = input()
        if user_input == "q":
            print("Thanks for playing, have a good day!")
            break
        computer_action = generate_computer_action()
        print(generate_result(user_input, computer_action))
