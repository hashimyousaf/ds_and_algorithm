def string_compression(str):
    if len(str) > 1:
        count = 1
        compress_list = []
        for i in range(len(str)):                # O(N)
            if i+1 < len(str) and str[i] == str[i+1]:
                count += 1
            else:
                compress_list.append(f'{str[i]}{count}')   #O(1)
                count = 1
        compressed_str = "".join(compress_list)
        return compressed_str if len(compressed_str) < len(str) else str
    else:
        return None


print(string_compression("aabcccccaaa"))