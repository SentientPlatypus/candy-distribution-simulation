import random
import statistics
import matplotlib.pyplot as plt

print("WE OUT")





class PERSON():
    def __init__(self, crusty_n_girls, crusty_n_boys, nice_n_girls, nice_n_boys) -> None:
        self.CRUSTY_N_GIRLS = crusty_n_girls
        self.CRUSTY_N_BOYS = crusty_n_boys
        self.NICE_N_GIRLS = nice_n_girls
        self.NICE_N_BOYS = nice_n_boys
        self.generate_random()

    def generate_random(self):
        self.crustygirls = [PERSON.pickedCandy() for a in range(self.CRUSTY_N_GIRLS)]
        self.crustyboys = [PERSON.pickedCandy() for a in range(self.CRUSTY_N_BOYS)]
        self.nicegirls = [PERSON.pickedCandy() for a in range(self.NICE_N_GIRLS)]
        self.niceboys = [PERSON.pickedCandy() for a in range(self.NICE_N_BOYS)]

    def simulate_gender_diff(self, trials:int) ->float:
        results = []
        for i in range(trials):
            self.generate_random()
            results.append(
                PERSON.getProportionDiff(self.crustyboys, self.niceboys) 
                - PERSON.getProportionDiff(self.crustygirls, self.nicegirls)
            )
        return results

    def pickedCandy() -> bool:
        return random.randint(0, 1) == 1

    def getProportionAccepted(l:list) -> float:
        return (sum(1.0 for element in l if element) / len(l))

    def getProportionDiff(list1:list, list2:list) -> float:
        """RETURNS THE DIFFERENCE IN PROPORTIONS. LIST2-LIST1"""
        return PERSON.getProportionAccepted(list2) - PERSON.getProportionAccepted(list1)

    def simulate_clothing(self, trials:int):
        results = []
        for i in range(trials):
            self.generate_random()
            results.append(
                PERSON.getProportionDiff(
                    self.crustyboys + self.crustygirls, 
                    self.niceboys + self.nicegirls
                )
            )
        return results

    def analyze_trials(self, y, trials:list):
        percent_greater_than_observed = (sum([1.0 for x in trials if x >= y]) / len(trials)) * 100
        if percent_greater_than_observed <= 5:
            print('Statistically significant. Only ' + str(percent_greater_than_observed) + '% of trials achieved a difference greater than ' + str(y))
        else:
            print('falls within natural error. ' + str(percent_greater_than_observed) + '% of trials achieved a difference greater than ' + str(y))
        plt.hist(trials, 100)
        plt.axvline(y, color='k', linestyle='dashed', linewidth=2)
        plt.show()



    
class GIO(PERSON):
    CRUSTY_N_GIRLS = 10
    CRUSTY_N_BOYS = 10
    NICE_N_GIRLS = 10
    NICE_N_BOYS = 10

    def __init__(self) -> None:
        PERSON.__init__(self,
            GIO.CRUSTY_N_GIRLS,
            GIO.CRUSTY_N_BOYS,
            GIO.NICE_N_GIRLS,
            GIO.NICE_N_BOYS
        )

class GENE(PERSON):
    CRUSTY_N_GIRLS = 10
    CRUSTY_N_BOYS = 10
    NICE_N_GIRLS = 10
    NICE_N_BOYS = 10

    def __init__(self) -> None:
        PERSON.__init__(self,
            GENE.CRUSTY_N_GIRLS,
            GENE.CRUSTY_N_BOYS,
            GENE.NICE_N_GIRLS,
            GENE.NICE_N_BOYS
        )

class TEDDY(PERSON):
    CRUSTY_N_GIRLS = 10
    CRUSTY_N_BOYS = 10
    NICE_N_GIRLS = 10
    NICE_N_BOYS = 10

    def __init__(self) -> None:
        PERSON.__init__(self,
            TEDDY.CRUSTY_N_GIRLS,
            TEDDY.CRUSTY_N_BOYS,
            TEDDY.NICE_N_GIRLS,
            TEDDY.NICE_N_BOYS
        )

gio = GIO()
print(gio.simulate_clothing(100))
gio.analyze_trials()








