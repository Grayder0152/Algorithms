from LB_7.hash_table import HashTable

if __name__ == '__main__':
    hash_table = HashTable()
    print(hash_table)

    while True:
        print("-" * 50)
        inp = input(
            """
    Оберіть опперацію з хеш-таблицею('q' - вийти):
        1 - додавання нової пари «ключ-значення»;
        2 - видалення пари «ключ-значення» за ключем;
        3 - пошук значення за ключем.
            """
        )
        match inp:
            case '1':
                key = int(input("Ключ: "))
                value = int(input("Значення: "))
                hash_table[key] = value
            case '2':
                key = int(input("Ключ: "))
                del hash_table[key]
            case '3':
                key = int(input("Ключ: "))
                print(f'value = {hash_table[key]}')
            case 'q':
                break
            case _:
                print("Номер не вірний!")
        print("-" * 50)
        print(hash_table)
