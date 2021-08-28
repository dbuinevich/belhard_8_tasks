from tomato import Tomato
from tomato_bush import TomatoBush
from gardener import Gardener


if __name__ == '__main__':
    tomatobush1 = TomatoBush("pomidor1-1", "pomidor1-2")
    tomatobush2 = TomatoBush("tomato1-1", "tomato1-2")
    gardener = Gardener("Vasyan", tomatobush1, tomatobush2)
    gardener.work()
    gardener.harvest()


