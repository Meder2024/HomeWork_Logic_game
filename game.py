from secret import generate_secret_number
from evaluate import evaluate_guess
from database import create_database, register_player, get_player_id

def play_game(player_id):
    print("Добро пожаловать в игру 'Быки и коровы'!")
    print("Компьютер загадал четырехзначное число с неповторяющимися цифрами.")
    print("Попробуйте угадать его.\n")

    secret_number = generate_secret_number()
    attempts = 0

    while True:
        user_guess = input("Введите ваше предположение: ")

        if not (user_guess.isdigit() and len(user_guess) == 4 and len(set(user_guess)) == 4):
            print("Пожалуйста, введите четырехзначное число с неповторяющимися цифрами.")
            continue

        user_guess = [int(digit) for digit in user_guess]
        attempts += 1

        bulls, cows = evaluate_guess(secret_number, user_guess)

        if bulls == 4:
            print(f"Поздравляем! Вы угадали число {secret_number} за {attempts} попыток.")
            break
        else:
            print(f"Быки: {bulls}, Коровы: {cows}")

def main():
    create_database()
    username = input("Введите ваше имя для регистрации: ")
    register_player(username)
    player_id = get_player_id(username)
    play_game(player_id)

if __name__ == "__main__":
    main()






# За каждую цифру, которая угадана и стоит на правильной позиции, игрок получает "быка".
# За каждую цифру, которая угадана, но стоит на неправильной позиции, игрок получает "корову".