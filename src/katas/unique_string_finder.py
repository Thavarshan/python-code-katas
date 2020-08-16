class UniqueStringFinder:
    def find_unique(self, list_of_strings: list):
        list_of_strings.sort(key=lambda element: element.lower())
        sorted_list = [set(element.lower()) for element in list_of_strings]

        if sorted_list.count(sorted_list[0]) == 1 and str(sorted_list[0]) != 'set()':
            return list_of_strings[0]
        else:
            return list_of_strings[-1]
