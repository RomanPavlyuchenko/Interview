from Stack import Stack


def is_bracket_balance(some_str):
    stack = Stack()
    for i in some_str:
        if i in '({[':
            stack.push(i)
        elif i in ')}]':
            if stack.size() > 0:
                peek_elem = stack.pop()
            else:
                return False
            if i == ')' and peek_elem != '(' or \
                i == '}' and peek_elem != '{' or \
                i == ']' and peek_elem != '[':
                return False

    return True


if __name__ == '__main__':
    some_strings = ['(((([{}]))))',
                    '[([])((([[[]]])))]{()}',
                    '{{[()]}}',
                    '}{}',
                    '{{[(])]}}',
                    '[[{())}]']

    for i in some_strings:
        print(is_bracket_balance(i))