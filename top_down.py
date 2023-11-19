def first(grammar):
    first = {}
    for i in grammar:
        first[i] = set()

    def calculate_first(i):
        if first[i]:
            return
        non_terminals.add(i)

        for production in grammar[i]:
            for j in production:
                if j in grammar:
                    calculate_first(j)
                    first[i].update(first[j])
                    if 'ε' not in first[j]:
                        break
                elif j.islower() or j == 'ε':
                    first[i].add(j)
                    break

        non_terminals.remove(i)

    non_terminals = set()

    for i in grammar:
        if i not in non_terminals:
            calculate_first(i)
    return first


n, m, k = map(int, input("Enter n m k: ").split())

nonterminals = input("Enter nonterminals: ").split()
nonterminals_array = []
for valor in nonterminals:
    nonterminals_array.append(valor)

print(nonterminals_array)

grammar = {nonterminal: [] for nonterminal in nonterminals}
for i in range(m):
    rule = input("Enter grammar rule: ").strip().split('-')
    nonterminals, production = rule[0].strip(), rule[1].strip()
    grammar[nonterminals].append(production)
    print(grammar)

for i in range(k):
    string = input("Enter string to analyze: ").strip()
    #is_valid, finished = recursive(grammar, string, nonterminals_array, 0, 'S')
    #print("yes" if is_valid and finished == len(string) else "no")

first_set = first(grammar)

for i,j in first_set.items():
    print(f'FIRST({i}): {j}')
