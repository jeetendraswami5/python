if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    import builtins
    print(hash(integer_list))
