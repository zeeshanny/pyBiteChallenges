"""
In this bite you will work with a list of names.
First you will write a function to take out duplicates and title case them.
Then you will sort the list in alphabetical descending order by surname and
lastly determine what the shortest first name is. For this exercise you can
assume there is always one name and one surname.
"""

NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of names, each name appears only once"""
    return list({name.title() for name in names})


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""
    names = dedup_and_title_case_names(names)
    return sorted(names,
                  key=lambda x: x.split()[-1],
                  reverse=True)


def shortest_first_name(names):
    """Returns the shortest first name (str)"""
    names = dedup_and_title_case_names(names)
    names = [name.split()[0] for name in names]
    return min(names, key=len)


if __name__ == "__main__":
    list = sort_by_surname_desc(NAMES)
    print(list)
