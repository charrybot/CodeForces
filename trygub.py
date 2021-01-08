t = int(input("").rstrip())


for cases in range(t):
    count = 0
    n = int(input("").rstrip())
    a = input("").rstrip()
    index_list = []
    index_list.append(a.find("t"))
    index_list.append(a.find("r"))
    index_list.append(a.find("y"))
    index_list.append(a.find("g"))
    index_list.append(a.find("u"))
    index_list.append(a.find("b"))
    if index_list[0] < index_list[1] < index_list[2] < index_list[3] < index_list[4] < index_list[5]:
        # there is trygub
        num_of_b = a.count("b")
        a = a.replace("b", "")
        for i in range(num_of_b):
            a = "b" + a
        print(a)
    else:
        # there is no trygub
        print(a)

