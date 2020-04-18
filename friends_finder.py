import sys
import argparse
from API import API
from finder import Finder


def create_parser():
    parser = argparse.ArgumentParser(description=
                                     'Программа для поиска общих друзей у пользователей ВКонтакте.',
                                     epilog=
                                     'Данил Панков КН-201 МЕН-280206')

    parser.add_argument('first_id', help='ID первого пользователя')
    parser.add_argument('second_id', help='ID второго пользователя')

    return parser


def main():
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    api = API(
        'efc4caa9efc4caa9efc4caa9b0efb5edf4eefc4efc4caa9b15db1196157aab3aea11d11',
        '5.103')
    first_id = namespace.first_id
    second_id = namespace.second_id
    finder = Finder(api)
    intersection = finder.find_friends_intersection(first_id, second_id)
    print(f'{len(intersection)} общих друзей!')
    for friend in intersection:
        print(friend['first_name'] + " " + friend['last_name'])


if __name__ == "__main__":
    main()
