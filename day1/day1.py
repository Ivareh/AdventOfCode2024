import heapq


def read_loc_ids_and_create_lists() -> tuple[list[int], list[int]]:
    left_nums = []
    right_nums = []

    heapq.heapify(left_nums)
    heapq.heapify(right_nums)
    with open("day1_input.txt") as my_file:
        for line in my_file:
            two_num_list = line.split()
            heapq.heappush(left_nums, int(two_num_list[0]))
            heapq.heappush(right_nums, int(two_num_list[1]))

    return left_nums, right_nums


def find_distance_two_smallest_loc_ids(
    left_nums: list[int], right_nums: list[int]
) -> int:
    smallest_left = 0
    smallest_right = 0
    if left_nums:
        smallest_left = heapq.heappop(left_nums)
    if right_nums:
        smallest_right = heapq.heappop(right_nums)

    distance = abs(smallest_left - smallest_right)
    return distance


def find_total_distance_score(left_nums: list[int], right_nums: list[int]):
    longest_length_nums = max(len(left_nums), len(right_nums))

    total_dist = 0
    for _ in range(longest_length_nums):
        total_dist += find_distance_two_smallest_loc_ids(left_nums, right_nums)

    print(f"Total distance: {total_dist}")


def find_similarity_score(left_nums: list[int], right_nums: list[int]):
    distinct_left_nums = set(left_nums)

    map_left_nums_count: dict[int, int] = {
        num: 0 for num in distinct_left_nums
    }  # number, count

    for right_num in right_nums:
        if right_num in map_left_nums_count.keys():
            map_left_nums_count[right_num] += 1

    left_nums_score = [num * count for num, count in map_left_nums_count.items()]

    total_sim_summed = sum(left_nums_score)
    print(total_sim_summed)


def main():
    left_nums, right_nums = read_loc_ids_and_create_lists()
    find_similarity_score(left_nums, right_nums)


main()
