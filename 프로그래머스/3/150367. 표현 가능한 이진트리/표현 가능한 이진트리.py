def solution(numbers):
    answer = []

    def is_possible(binary_str):
        n = len(binary_str)
        if n == 1:
            return True

        mid = n // 2
        root = binary_str[mid]
        left = binary_str[:mid]
        right = binary_str[mid + 1:]

        if root == '0' and ('1' in left or '1' in right):
            return False

        return is_possible(left) and is_possible(right)

    for number in numbers:
        binary_str = bin(number)[2:]
        k = 0
        while 2**k - 1 < len(binary_str):
            k += 1
        padded_len = 2**k - 1
        padded_binary_str = '0' * (padded_len - len(binary_str)) + binary_str

        if is_possible(padded_binary_str):
            answer.append(1)
        else:
            answer.append(0)

    return answer