from typing import List


def can_partition_k_subsets_dp(nums: List[int], k: int) -> bool:
    if not nums:
        return False

    n = len(nums)
    total = sum(nums)
    if total % k != 0:
        return False
    target = total // k

    dp = [False] * (1 << n)
    subset_sums = [0] * (1 << n)

    dp[0] = True
    nums.sort()

    if nums[-1] > target:
        return False

    # loop over powerset
    for subset in range(1 << n):
        if dp[subset]:
            for num_idx in range(n):
                new_subset = subset | (1 << num_idx) #including num_index th bit
                if new_subset != subset:
                    # if total sum is less than target, store in dp and total array
                    if nums[num_idx] <= target - subset_sums[subset]:
                        dp[new_subset] = True
                        subset_sums[new_subset] = (nums[num_idx] + subset_sums[subset]) % target # mod target since we might have already find a valid group
                    else:
                        break
    return dp[-1]


def can_partition_k_subsets_backtrack(nums, k):
    target, rem = divmod(sum(nums), k)
    if rem:
        return False

    def search(groups):
        if not nums:
            return True
        v = nums.pop()
        for i, group in enumerate(groups):
            if group + v <= target:
                groups[i] += v
                if search(groups):
                    return True
                groups[i] -= v
            if not group:
                break
        nums.append(v)
        return False

    nums.sort()
    if nums[-1] > target:
        return False
    while nums and nums[-1] == target:
        nums.pop()
        k -= 1

    return search([0] * k)


if __name__ == "__main__":
    nums, k = [1, 2, 2, 1, 3], 3
    print(can_partition_k_subsets_dp(nums, k))
