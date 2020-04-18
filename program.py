from API import API


def get_ids_from_list(users_list):
    ids = []
    for friend in users_list:
        ids.append(friend['id'])
    return ids


def find_user_with_id(users_list, user_id):
    for friend in users_list:
        if friend['id'] == user_id:
            return friend


def get_friends_intersection(first_list: list, second_list: list):
    intersection = list()
    first_ids = get_ids_from_list(first_list)
    second_ids = get_ids_from_list(second_list)
    for user_id in first_ids:
        if user_id in second_ids:
            intersection.append(find_user_with_id(first_list, user_id))
    return intersection


def main_loop(api: API):
    print("Введите id первого пользователя:")
    first_id = input()
    print("Введите id второго пользователя:")
    second_id = input()
    first_friends = api.get_friends(first_id, {'fields': 'name'})['response']['items']
    second_friends = api.get_friends(second_id, {'fields': 'name'})['response']['items']
    intersection = get_friends_intersection(first_friends, second_friends)
    print(f'{len(intersection)} общих друзей!')
    for friend in intersection:
        print(friend['first_name'] + " " + friend['last_name'])
    print('Посмотрим ещё?')
    main_loop(api)


if __name__ == '__main__':
    api = API('efc4caa9efc4caa9efc4caa9b0efb5edf4eefc4efc4caa9b15db1196157aab3aea11d11',
              '5.103')
    main_loop(api)
