from random import *

def add_sportmen(sportmen:list, results:list) -> list:
    """
    Module created for adding new sportman
    :param sportmen:list
    :param results:list
    :rtype sportmen, results:list
    """
    try:
        b = randrange(2, 5)
        ac = int(input('How much sportmen will take part in competitions:'))
        for i in range(ac):
            name = input('Name of sportman:')
            sportmen.append(name)
            results.append((3+b))
            b += b
    except:
        print('Something goes wrong, try again')

    return sportmen, results


def n_results(sportmen:list, results: list):
    """
    Module created for showing results and sportmen by entered value
    :param sportmen:list
    :param results:list
    :rtype abc:str
    :rtype: abcd:int
    """
    q = 0
    ac = int(input('How much results you want:'))

    if ac > len(sportmen):
        print('Sportmen out of range, try again')
    elif ac <= len(sportmen):
        for i in range(ac):
            abc = sportmen[q]
            abcd = results[q]
            q += 1
            print(f'{q} place had: {abc} - {abcd}m ')
    return abc, abcd


def sorted_lists(sportmen:list, results:list) -> list:
    """
    Module created for lists sorting
    :param sportmen:list
    :param results:list
    :rtype sportmen, results:list
    """
    q = 0
    for i in range(len(results)):
        results.sort()
        sportmen[q]
        q += 1
        print(f'{q} place had: {results[q-1]}m - {sportmen[q-1]}')

    print(f'Sorted list is: {results}')
    return sportmen, results

def top3(sportmen:list) -> list:
    """
    Module created for showing top 3 sportmen
    :param sportmen:list
    :rtype top_list:list
    """
    q = 1
    y = 0
    k = 0
    top_list = []
    top = ['the best', 'second', 'not bad']
    for i in range(1, 4):
        print(f'{sportmen[y]} is {top[k]} - {q} place')
        top_list.append(sportmen[y])
        q += 1
        y += 1
        k += 1
    return top_list


def disqualification(sportmen:list, results:list) -> list:
    """
    Module created to disqualify sportmen
    :param sportmen:list
    :param results:list
    :rtype sportmen, results:list
    """
    ac = int(input('Please enter result:'))
    acc = 0
    for i in range (len(results)):
        if results[acc] < ac:
            results.pop(acc)
            sportmen.pop(acc)
        elif results[acc] > ac:
            acc += 1
    print(results)
    print(sportmen)
    return results, sportmen


def find_sportmen_by_name(sportmen:list, results:list, ac:str):
    """
    Module created to find sportmen by name
    :param sportmen:list
    :param results:list
    :rtype abc
    """
    q = 0
    ac = input('Enter the name:')
    while True:
        try:
            i = sportmen.index(ac, q)
            abc = print(f'This {sportmen[i]} had {results[i]}m')
            q = i + 1
        except:
            break
    return abc

def save_data(sportmen:list, results:list):
    """
    Module created for save data
    :param sportmen:list
    :param results:list
    :rtype file, file2:str
    """
    file = open('sportmen.txt', 'w')
    file2 = open('results.txt', 'w')
    results = list(map(str, results))
    for e in sportmen:
        file.write(e)
        file.write('\n')
    file.close()

    for r in results:
        file2.write(r)
        file2.write('\n')
    file2.close()

    return file, file2

