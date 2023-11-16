# Added to Comp Proyect

def recursive(grammar, string, nonterminal_array, current_string_index,first):

    # current_nonterminal = nonterminal_array[current_nonterminal_index]

    if first in grammar:

        for grammar_rule in grammar[first]:
            non_current = current_string_index  # Save in case it doesn't work
            is_valid = True
            # remaining_string = string  # Think line can be removed - it's a duplicate from string

            for symbol in grammar_rule:  # symbol == a
                if symbol in nonterminal_array:
                    is_valid, current_string_index = recursive(grammar, string, nonterminal_array, current_string_index, symbol)
                elif current_string_index < len(string) and symbol == string[current_string_index]:
                    current_string_index += 1
                else:
                    is_valid = False
                    break

            if is_valid:
                if non_current == current_string_index:
                    is_valid = False
                return is_valid, current_string_index

            current_string_index = non_current

    return False, current_string_index


def main():
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
        is_valid, finished = recursive(grammar, string, nonterminals_array, 0, 'S')
        print("yes" if is_valid and finished == len(string) else "no")

    print("The program has finished.")

main()
