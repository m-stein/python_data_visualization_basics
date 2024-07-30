from random import randint
import plotly.express as px

export_instead_of_show = False


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides
        self.sides = range(1, self.num_sides + 1)

    def roll(self):
        return randint(1, self.num_sides)


dice = [Die(4), Die(6), Die(12), Die(24)]
num_rolls = 10000
results = [sum([die.roll() for die in dice]) for i in range(num_rolls)]
result_counts = []
possible_results = range(sum([die.sides[0] for die in dice]), sum([die.sides[-1] for die in dice]) + 1)
for result in possible_results:
    result_counts.append(results.count(result))

title = f"Results of rolling {len(dice)} dice {[f'D{die.num_sides}' for die in dice]} {num_rolls} times"
labels = {'x': 'Result', 'y': 'Result count'}
fig = px.bar(x=possible_results, y=result_counts, title=title, labels=labels,
             text=[f"{r*100/num_rolls}%" for r in result_counts])

fig.update_layout(xaxis_dtick=1)
if export_instead_of_show:
    fig.write_html('rolling_dice.html')
else:
    fig.show()
