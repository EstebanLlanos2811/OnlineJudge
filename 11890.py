from sys import stdin

def phi(expresion, nums):
    ans, stack, i = 0, ['+'], 0
    while i < len(expresion):
        if expresion[i] == 'x':
            if expresion[i-1] == '-':
                if stack[-1] == '-': ans += nums.pop()
                else: ans -= nums.pop(0)
            else:
                if stack[-1] == '-': ans -= nums.pop(0)
                else: ans += nums.pop()
        elif expresion[i] == '(':
            if expresion[i-1] == '-':
                if stack[-1] == '+': stack.append('-')
                elif stack[-1] == '-': stack.append('+')
            else:
                if stack[-1] == '-': stack.append('-')
                elif stack[-1] == '+': stack.append('+')
        elif expresion[i] == ')':
            if len(stack) > 1: stack.pop()
        i += 1
    return ans

def main():
    cases = int(stdin.readline())
    for _ in range(cases):
        expresion = stdin.readline()
        N = int(stdin.readline())
        nums = list(map(int, stdin.readline().split()))
        nums.sort()
        print(phi(expresion, nums))
    
main()