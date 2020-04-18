from API import API
from finder import Finder


def main_loop(api: API):
    print("Введите id первого пользователя:")
    first_id = input()
    print("Введите id второго пользователя:")
    second_id = input()
    finder = Finder(api)
    intersection = finder.find_friends_intersection(first_id, second_id)
    print(f'{len(intersection)} общих друзей!')
    for friend in intersection:
        print(friend['first_name'] + " " + friend['last_name'])
    print('Посмотрим ещё?')
    main_loop(api)


if __name__ == '__main__':
    api = API('efc4caa9efc4caa9efc4caa9b0efb5edf4eefc4efc4caa9b15db1196157aab3aea11d11',
              '5.103')
    main_loop(api)
