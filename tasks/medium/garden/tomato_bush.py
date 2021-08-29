from tomato import Tomato

class TomatoBush:
    tomato_list: list

    def __init__(self, *args):
        self.tomato_list = list(args)

    def grow_all(self):
        for i in self.tomato_list:
            i.grow()

    def all_are_ripe(self):
        list_size = len(self.tomato_list)
        true_counter = 0
        for i in self.tomato_list:
            if i.is_ripe():
                true_counter += 1
        return list_size == true_counter

    def give_away_all(self):
        tomato_list_2 = self.tomato_list.copy()
        self.tomato_list.clear()
        return tomato_list_2

#
# if __name__ == '__main__':
#     pomidor1 = Tomato(1)
#     pomidor2 = Tomato(2)
#     tomato1 = Tomato(3)
#     tomato2 = Tomato(4)
#     tomatobush1 = TomatoBush(pomidor1, pomidor2)
#     tomatobush2 = TomatoBush(tomato1, tomato2)
#     tomatobush1.give_away_all()
#     tomatobush1.grow_all()
#     tomatobush1.grow_all()
#     tomatobush1.grow_all()



