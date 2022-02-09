class SuperList(list):
    def __len__(self):
        return 1000


super_list1 = SuperList()
super_list1.extend([1, 2, 3, 4, 5, 6])
print(len(super_list1))
print(super_list1)
