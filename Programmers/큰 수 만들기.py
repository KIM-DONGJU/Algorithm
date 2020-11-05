def solution(number, k):
    stack = [number[0]]

    for n in number[1:] :
        while stack and k > 0 and n > stack[-1]:
            k -= 1
            stack.pop()

        stack.append(n)

        if k == 0 :
            return "".join(stack)

    return "".join(stack[:-k])

print(solution("1924", 2))