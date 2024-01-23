from datetime import *
def check_of_summ(isikukood:str):
    ik_list=list(isikukood)
    summ = 0
    summ1 = 0
    ikoodid = []
    numbers = []
    for i in range(1,11):
        if i == 10:
            summ += 1 * int(ik_list[i-1])
        else:
            summ += i * int(ik_list[i-1])
    for i in range(1,11):
        if i in [1,2,3]:
            summ1 += i * int(ik_list[i+6])
        else:
            summ1 += i * int(ik_list[i-1])
    summ_res = summ // 11
    summres1 = summ1 // 11
    res = summ - (summ_res * 11)
    res1 = summ1 - (summres1 * 11)
    if int(ik_list[10]) == int(res) or int(ik_list[10]) == int(res1):
        print(f"This is {gender(isikukood)}, his/her birthday {time(isikukood)} and birth place {hospital(isikukood)}")
        ikoodid.append(isikukood)
        #print(f"isikokoodid - {ikoodid}")
        return ikoodid 
    else:
        print("OK10")
        answ = "Last numeber is incorrect"
        numbers.append(isikukood)
        print(f"isikukood - {numbers}")
    return answ


def hospital(isikukood:str):
    ik_list=list(isikukood)
    b = ik_list[7] + ik_list[8] + ik_list[9]
    if int(b) in range(1,11):
        birth_place = "Kuressaare Hospital"
    elif int(b) in range(11,21):
        birth_place = "Tartu University Woman Hospital, Tartumaa, Tartu"
    elif int(b) in range(21,221):
        birth_place = "East Tallinn Central Hospital, Pelgulinna Maternity Hospital, Hiiumaa, Keila, Rapla Hospital, Loksa Hospital"
    elif int(b) in range(221,271):
        birth_place = "Ida-Viru Central Hospital (Kohtla-Järve, former Jõhvi)"
    elif int(b) in range(271,371):
        birth_place = "Maarjamõisa Clinic (Tartu), Jõgeva Hospital"
    elif int(b) in range(371,321):
        birth_place = "Narva Hospital"
    elif int(b) in range(421,471):
        birth_place = "Pärnu Hospital"
    elif int(b) in range(471,491):
        birth_place = "Pelgulinna Maternity Hospital (Tallinn), Haapsalu Hospital"
    elif int(b) in range(491,521):
        birth_place = "Järvamaa Hospital (Paide)"
    elif int(b) in range(521,571):
        birth_place = "Rakvere, Tapa Hospital"
    elif int(b) in range(571,601):
        birth_place = "Valga Hospital"
    elif int(b) in range(601,651):
        birth_place = "Viljandi Hospital"
    else:
        birth_place = "South Estonian Hospital (Võru), Põlva Hospital"
    return birth_place

def gender(isikukood:str):
    ik_list=list(isikukood)
    if int(ik_list[0]) in [1,3,5]:
        gender = "Male"
    else:
        gender = "Female"
    return gender

def time(isikukood:str):
    ik_list = list(isikukood)
    if int(ik_list[0]) in [1,2]:
        a = 1800
    elif int(ik_list[0]) in [3,4]:
        a = 1900
    else:
        a = 2000
    age = a+int(ik_list[1]+ik_list[2])
    month = int(ik_list[3]+ik_list[4])
    day = int(ik_list[5]+ik_list[6])
    return datetime(age, month, day, hour=0, minute=0, second=0)