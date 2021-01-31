from typing import List


def find_friend_circles(friends_matrix: List[List[int]]) -> int:
    visited = [False] * len(friends_matrix)
    ans = 0
    for i in range(len(friends_matrix)):
        if not visited[i]:
            dfs(friends_matrix, i, visited)
            ans += 1

    return ans


def dfs(friends_matrix: List[List[int]], i: int, visited: List[bool]):
    for j in range(len(friends_matrix)):
        if friends_matrix[i][j] == 1 and not visited[j]:
            visited[j] = True
            dfs(friends_matrix, j, visited)


def longest_str_chain(words: List[str]) -> int:
    def dfs(word, memo):

        if word not in memo:
            return 0

        if not memo[word]:
            memo[word] = max(
                [dfs(word[:i] + word[i + 1:], memo) + 1 for i in range(len(word))]
            )
        return memo[word]

    if not words:
        return 0

    memo = {w: None for w in words}

    return max([dfs(w, memo) for w in memo if not memo[w]])


def longest_str_chain(words: List[str]) -> int:
    if not words:
        return 0
    # sort in ascending order O(nlog(n))
    words = sorted(words, key=lambda x: len(x))
    dp = {w: 0 for w in words}
    for w in words:
        dp[w] = max([dp.get(w[:i] + w[i + 1 :], 0) + 1 for i in range(len(w))])

    return max(dp.values())


if __name__ == "__main__":
    M1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
    M2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]
    print(find_friend_circles(M1))
    print(find_friend_circles(M2))
