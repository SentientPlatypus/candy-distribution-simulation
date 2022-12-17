import random
import statistics

print("WE OUT")

def pickedCandy() -> bool:
    return random.randint(0, 1) == 1

def getProportionAccepted(l:list) -> float:
    return (sum(1.0 for element in l if element) / len(l))

def getProportionDiff(list1:list, list2:list) -> float:
    return getProportionAccepted(list2) - getProportionAccepted(list1)

class GIO():
    CRUSTY_N_GIRLS = 10
    CRUSTY_N_BOYS = 10
    NICE_N_GIRLS = 10
    NICE_N_BOYS = 10

    def __init__(self) -> None:
        self.crustygirls = [pickedCandy() for a in range(GIO.CRUSTY_N_GIRLS)]
        self.crustyboys = [pickedCandy() for a in range(GIO.CRUSTY_N_BOYS)]
        self.nicegirls = [pickedCandy() for a in range(GIO.NICE_N_GIRLS)]
        self.niceboys = [pickedCandy() for a in range(GIO.NICE_N_BOYS)]

    def compare_proportion_differences(self) ->float:
        return getProportionDiff(self.crustyboys, self.niceboys) - getProportionDiff(self.crustygirls, self.nicegirls)
   

class GENE():
    CRUSTY_N_GIRLS = 10
    CRUSTY_N_BOYS = 10
    NICE_N_GIRLS = 10
    NICE_N_BOYS = 10

    def __init__(self) -> None:
        self.crustygirls = [pickedCandy() for a in range(GIO.CRUSTY_N_GIRLS)]
        self.crustyboys = [pickedCandy() for a in range(GIO.CRUSTY_N_BOYS)]
        self.nicegirls = [pickedCandy() for a in range(GIO.NICE_N_GIRLS)]
        self.niceboys = [pickedCandy() for a in range(GIO.NICE_N_BOYS)]

    def compare_proportion_differences(self) ->float:
        return getProportionDiff(self.crustyboys, self.niceboys) - getProportionDiff(self.crustygirls, self.nicegirls)


class TEDDY():
    CRUSTY_N_GIRLS = 10
    CRUSTY_N_BOYS = 10
    NICE_N_GIRLS = 10
    NICE_N_BOYS = 10

    def __init__(self) -> None:
        self.crustygirls = [pickedCandy() for a in range(GIO.CRUSTY_N_GIRLS)]
        self.crustyboys = [pickedCandy() for a in range(GIO.CRUSTY_N_BOYS)]
        self.nicegirls = [pickedCandy() for a in range(GIO.NICE_N_GIRLS)]
        self.niceboys = [pickedCandy() for a in range(GIO.NICE_N_BOYS)]

    def compare_proportion_differences(self) ->float:
        return getProportionDiff(self.crustyboys, self.niceboys) - getProportionDiff(self.crustygirls, self.nicegirls)

HOW_MANY_RUNS = 50000
def initial_sim():
    results = []
    for x in range(HOW_MANY_RUNS):

        ##Take the difference in proportion accepted between crusty and nice for each persion, ignoring whether they are boys or girls. 
        ##then, take the average difference
        differences = []
        gio = GIO()
        differences.append(
            getProportionAccepted(gio.crustyboys + gio.crustygirls) 
            - getProportionAccepted(gio.niceboys + gio.nicegirls)
        )

        gene = GENE()
        differences.append(
            getProportionAccepted(gene.crustyboys + gene.crustygirls) 
            - getProportionAccepted(gene.niceboys + gene.nicegirls)
        )

        teddy = TEDDY()
        differences.append(
            getProportionAccepted(teddy.crustyboys + teddy.crustygirls) 
            - getProportionAccepted(teddy.niceboys + teddy.nicegirls)
        )

        results.append(statistics.mean(differences))

    return results



def sim_for_gender_diff():
    results = []
    for x in range(HOW_MANY_RUNS):
        gio = GIO()
        gio_diff = gio.compare_proportion_differences()

        gene = GENE()
        gene_diff = gene.compare_proportion_differences()

        teddy = TEDDY()
        teddy_diff = teddy.compare_proportion_differences()

        results.append(statistics.mean([gio_diff, gene_diff, teddy_diff]))
    return results


def analyze_initial(our_average_difference):
    trials = initial_sim()
    percent_greater_than_observed = (sum([1.0 for x in trials if x >= our_average_difference]) / len(trials)) * 100
    if percent_greater_than_observed <= 5:
        print('Statistically significant. Only ' + str(percent_greater_than_observed) + '% of trials achieved a difference greater than ' + str(our_average_difference))
    else:
        print('falls within natural error. ' + str(percent_greater_than_observed) + '% of trials achieved a difference greater than ' + str(our_average_difference))

def analyze_gender_diff(our_average_gender_proportion_difference):
    trials = sim_for_gender_diff()
    percent_greater_than_observed = (sum([1.0 for x in trials if x >= our_average_gender_proportion_difference]) / len(trials)) * 100
    if percent_greater_than_observed <= 5:
        print('Statistically significant. Only ' + str(percent_greater_than_observed) + '% of trials achieved a difference greater than ' + str(our_average_gender_proportion_difference))
    else:
        print('falls within natural error. ' + str(percent_greater_than_observed) + '% of trials achieved a difference greater than ' + str(our_average_gender_proportion_difference))

analyze_gender_diff(.32)


        









