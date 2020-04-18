class Finder:
    def __init__(self, api):
        self.__api = api

    def __get_ids_from_list(self, users_list):
        ids = []
        for friend in users_list:
            ids.append(friend['id'])
        return ids

    def __find_user_with_id(self, users_list, user_id):
        for friend in users_list:
            if friend['id'] == user_id:
                return friend

    def __get_friends_intersection(self, first_list: list, second_list: list):
        intersection = list()
        first_ids = self.__get_ids_from_list(first_list)
        second_ids = self.__get_ids_from_list(second_list)
        for user_id in first_ids:
            if user_id in second_ids:
                intersection.append(self.__find_user_with_id(first_list, user_id))
        return intersection

    def find_friends_intersection(self, first_id, second_id):
        first_response = self.__api.get_friends(first_id, {'fields': 'name'})
        first_friends = first_response['response']['items']
        second_response = self.__api.get_friends(second_id, {'fields': 'name'})
        second_friends = second_response['response']['items']
        return self.__get_friends_intersection(first_friends, second_friends)
