from ring import RingList as ring_list


def unique():
    new_lst = ring_list()
    for i in range(len(a)):
        if not new_lst.find(a[i]):
            new_lst.append(a[i])
    return len(new_lst)


a = ring_list()
a.append(1)
a.append(2)
a.append(1)
a.append(3)
a.append(4)
a.append(2)
print(a[2], len(a))
print(unique())
