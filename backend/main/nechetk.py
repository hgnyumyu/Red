import numpy as np  # Импорт библиотеки NumPy для работы с числами
from skfuzzy import control as ctrl  # Импорт библиотеки scikit-fuzzy для работы с нечеткой логикой
from skfuzzy import trimf  # Импорт функции trimf для создания треугольных функций принадлежности


# Определение входных переменных
c_sharp = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'c_sharp')
c_plus_plus = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'c_plus_plus')
python = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'python')
js = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'js')
css_html = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'css_html')
sql = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'sql')
b_network = ctrl.Antecedent(np.arange(0, 1.1, 0.1), 'b_network')

# Определение функций принадлежности для каждой входной переменной
c_sharp['novice'] = trimf(c_sharp.universe, [0, 0, 0.3])
c_sharp['intermediate'] = trimf(c_sharp.universe, [0, 0.3, 0.7])
c_sharp['advanced'] = trimf(c_sharp.universe, [0.3, 0.7, 1])
# Аналогичные функции принадлежности для других входных переменных

c_plus_plus['novice'] = trimf(c_plus_plus.universe, [0, 0, 0.3])
c_plus_plus['intermediate'] = trimf(c_plus_plus.universe, [0, 0.3, 0.7])
c_plus_plus['advanced'] = trimf(c_plus_plus.universe, [0.3, 0.7, 1])

python['novice'] = trimf(python.universe, [0, 0, 0.3])
python['intermediate'] = trimf(python.universe, [0, 0.3, 0.7])
python['advanced'] = trimf(python.universe, [0.3, 0.7, 1])

js['novice'] = trimf(js.universe, [0, 0, 0.3])
js['intermediate'] = trimf(js.universe, [0, 0.3, 0.7])
js['advanced'] = trimf(js.universe, [0.3, 0.7, 1])

css_html['novice'] = trimf(css_html.universe, [0, 0, 0.3])
css_html['intermediate'] = trimf(css_html.universe, [0, 0.3, 0.7])
css_html['advanced'] = trimf(css_html.universe, [0.3, 0.7, 1])

sql['novice'] = trimf(sql.universe, [0, 0, 0.3])
sql['intermediate'] =trimf(sql.universe, [0, 0.3, 0.7])
sql['advanced'] = trimf(sql.universe, [0.3, 0.7, 1])

b_network['novice'] = trimf(b_network.universe, [0, 0, 0.3])
b_network['intermediate'] = trimf(b_network.universe, [0, 0.3, 0.7])
b_network['advanced'] = trimf(b_network.universe, [0.3, 0.7, 1])

# Определите выходные переменные
backend = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'backend')
front_end = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'front_end')
linux = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'linux')
unity = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'unity')
subd = ctrl.Consequent(np.arange(0, 1.1, 0.1), 'subd')

# Определите функции принадлежности для каждой выходной переменной.
backend['novice'] = trimf(backend.universe, [0, 0, 0.3])
backend['intermediate'] =trimf(backend.universe, [0, 0.3, 0.7])
backend['advanced'] = trimf(backend.universe, [0.8, 0.9, 1])

front_end['novice'] = trimf(front_end.universe, [0, 0, 0.3])
front_end['intermediate'] = trimf(front_end.universe, [0, 0.3, 0.7])
front_end['advanced'] = trimf(front_end.universe, [0.3, 0.7, 1])

linux['novice'] = trimf(linux.universe, [0, 0, 0.3])
linux['intermediate'] = trimf(linux.universe, [0, 0.3, 0.7])
linux['advanced'] = trimf(linux.universe, [0.3, 0.7, 1])

unity['novice'] = trimf(unity.universe, [0, 0, 0.3])
unity['intermediate'] = trimf(unity.universe, [0, 0.3, 0.7])
unity['advanced'] = trimf(unity.universe, [0.3, 0.7, 1])

subd['novice'] = trimf(subd.universe, [0, 0, 0.3])
subd['intermediate'] = trimf(subd.universe, [0, 0.3, 0.7])
subd['advanced'] = trimf(subd.universe, [0.3, 0.7, 1])

# Define the rules
rule1 = ctrl.Rule(c_sharp['intermediate'], backend['novice'])
rule2 = ctrl.Rule(c_plus_plus['intermediate'], backend['novice'])
rule3 = ctrl.Rule(python['intermediate'], backend['novice'])
rule4 = ctrl.Rule(js['advanced'] | css_html['advanced'], front_end['advanced'])
rule5 = ctrl.Rule(c_sharp['intermediate'] | c_plus_plus['intermediate'] | python['intermediate'], backend['intermediate'])
rule6 = ctrl.Rule(js['advanced'] & css_html['advanced'], front_end['advanced'])
rule7 = ctrl.Rule(sql['advanced'], subd['advanced'])
rule14 = ctrl.Rule(sql['novice'], subd['novice'])
rule15 = ctrl.Rule(sql['intermediate'], subd['intermediate'])
rule8 = ctrl.Rule(b_network['advanced'], linux['advanced'])
rule9 = ctrl.Rule(c_sharp['advanced'], unity['advanced'])
rule10 = ctrl.Rule(c_sharp['intermediate'] & c_plus_plus['intermediate'] & python['intermediate'], backend['advanced'])
rule11 = ctrl.Rule(c_sharp['advanced'] & c_plus_plus['advanced'] & python['advanced'], backend['advanced'])
rule12 = ctrl.Rule(b_network['novice'], linux['novice'])
rule13 = ctrl.Rule(b_network['intermediate'], linux['intermediate'])
rule16 = ctrl.Rule(js['novice'] & css_html['novice'], front_end['novice'])
rule17 = ctrl.Rule(js['intermediate'] & css_html['intermediate'], front_end['intermediate'])
# Create a control system
system = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6,rule7,rule8,rule9,rule10,rule11,rule12,rule13,rule14,rule15,rule16,rule17])
# Create a control system simulation
sim = ctrl.ControlSystemSimulation(system)

def start(val_dict):
    sim.input['c_sharp'] = val_dict[4]
    sim.input['c_plus_plus'] = val_dict[3]
    sim.input['python'] = val_dict[2]
    sim.input['js'] = val_dict[1]
    sim.input['css_html'] = val_dict[0]
    sim.input['sql'] = val_dict[5]
    sim.input['b_network'] = val_dict[6]
    # Run the simulation
    sim.compute()
    # Get the output values
    output_values = sim.output
    print("Backend:", output_values['backend'])
    print("Front End:", output_values['front_end'])
    print("Linux:", output_values['linux'])
    print("Unity:", output_values['unity'])
    print("Subd:", output_values['subd'])
    recommended = {}
    procent={}

    sorted_values = sorted(output_values.items(), key=lambda x: x[1], reverse=True)
    recommended["recommended"] = [key for key, value in sorted_values]
    procent = output_values
    
    result_array = []
    if 'backend' in recommended['recommended']:
        result_array.append(1)
    if 'front_end' in recommended['recommended']:
        result_array.append(0)
    if 'linux' in recommended['recommended']:
        result_array.append(3)
    if 'unity' in recommended['recommended']:
        result_array.append(4)
    if 'subd' in recommended['recommended']:
        result_array.append(2)

    procent = {str(result_array[i]): value for i, (key, value) in enumerate(sorted(output_values.items(), key=lambda x: x[1], reverse=True)) if i < len(result_array)}
    print("Procent")
    print(procent)
    return result_array,procent




output_values = sim.output
# Get the output values
# output_values = sim.output
# print("Backend:", output_values['backend'])
# print("Output values:")
# if 'backend' in output_values:
#     print("Backend:", output_values['backend'])
# else:
#     print("Backend: Not available")

# if 'front_end' in output_values:
#     print("Front End:", output_values['front_end'])
# else:
#     print("Front End: Not available")

# if 'linux' in output_values:
#     print("Linux:", output_values['linux'])
# else:
#     print("Linux: Not available")

# if 'unity' in output_values:
#     print("Unity:", output_values['unity'])
# else:
#     print("Unity: Not available")

# if 'subd' in output_values:
#     print("Subd:", output_values['subd'])
# else:
#     print("Subd: Not available")
