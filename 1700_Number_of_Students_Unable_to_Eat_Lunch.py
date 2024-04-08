class Solution(object):
    def countStudents(self, students, sandwiches):
        counts = [0, 0]
        for student in students:
            counts[student] += 1
        print(counts)
        remaining = len(sandwiches)
        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                break
            if remaining == 0:
                break
            counts[sandwich] -= 1
            remaining -= 1       
        return remaining
