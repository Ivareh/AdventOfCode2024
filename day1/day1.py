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


def main() -> int:
    left_nums, right_nums = read_loc_ids_and_create_lists()

    longest_length_nums = max(len(left_nums), len(right_nums))

    total_dist = 0
    for _ in range(longest_length_nums):
        total_dist += find_distance_two_smallest_loc_ids(left_nums, right_nums)

    print(f"Total distance: {total_dist}")


main()
