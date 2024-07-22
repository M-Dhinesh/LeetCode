def sort_people_by_height(names, heights):
    return [name for _, name in sorted(zip(heights, names), reverse=True, key=lambda x: x[0])]
