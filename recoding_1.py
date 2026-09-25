# def ticket_total(price, quantity):
#     total = price * quantity
#     print(total)
#     amount = ticket_total("7", 3)
#     print(amount) 
# Q1 Part A Before running the code, write the exact two output lines and state the value and type of amount. [4 marks]

#solution

def ticket_total(price, quantity):
    total = price * quantity
    return total
    
amount = ticket_total("7", 3)
print(amount)

#-----------------------------------------------------------

# def passing_scores(scores):
#     passed = []
#     for index in range(len(scores) - 1):
#         if scores[index] > 50:
#             passed.append(scores[index])
#     return passed
# print(passing_scores([49, 50, 80, 65]))

# Q2 Part A

# Predict the current printed output. Identify both independent defects and explain which result each defect loses. [5 marks]

# Q2 Part B

# Correct the function without changing the input list. [6 marks]

# Q2 Part C

# Write three executable assertions: one for the pass boundary 50, one for a single passing score, and one for an empty list. [4 marks])

def passing_scores(scores):
    passed = []
    for index in range(len(scores)):
        if scores[index] >= 50:
            passed.append(scores[index])
    return passed

print(passing_scores([49, 50, 80, 65]))

assert passing_scores([50]) == [50]
assert passing_scores([80]) == [80]
assert passing_scores([]) == []

#---------------------------------------------------------------

# The function should return a new profile with an extra tag. The original profile and its tags must stay unchanged. The profile has only a string name and a list of string tags; both keys always exist.
# def add_tag(profile, tag):
#     updated = profile.copy()
#     updated["tags"].append(tag)
#     return updated
# original = {"name": "Ada", "tags": ["python"]}
# changed = add_tag(original, "testing")
# print(original["tags"])
# print(changed is original)
# print(changed["tags"] is original["tags"])

# Q3 Part A

# Before running the code, predict all three output lines. Explain what copy() copies here and which object is still shared. [7 marks]

# Q3 Part B

# Repair add_tag so its returned dictionary and tags list are independent of the original. Do not change the public function signature. [7 marks]

# Q3 Part C

# Write assertions showing that the original tags remain unchanged and the returned tags contain the new tag. Then append another tag to the returned list and assert that the original still has only its initial tag. [6 marks]

#solution

def add_tag(profile, tag):
    updated = profile.copy()
    updated["tags"] = profile["tags"].copy()
    updated["tags"].append(tag)
    return updated


original = {"name": "Ada", "tags": ["python"]}
changed = add_tag(original, "testing")

print(original["tags"])
print(changed is original)
print(changed["tags"] is original["tags"])


assert original["tags"] == ["python"]
assert changed["tags"] == ["python", "testing"]

changed["tags"].append("linux")

assert original["tags"] == ["python"]

#------------------------------------------------------------

# Question 4 Validate an import

# You receive a list of strings representing whole-unit amounts. Return a dictionary with total and rejected. Use Python int(raw) conversion: surrounding whitespace is accepted. A converted amount of zero or more is valid. Negative amounts and strings that cannot be converted must each increase rejected by one. An empty list returns both values as zero. Do not change the input.

# def summarise_amounts(raw_values):
#     total = 0
#     for raw in raw_values:
#         try:
#             total += int(raw)
#         except:
#             pass
#     return {"total": total, "rejected": 0}
    
# Required example: ["10", " 5 ", "bad", "-3", "0", ""] must return {"total": 15, "rejected": 3}. Inputs are always strings; no other type validation is required.

# Q4 Part A
# Identify three defects or risks in the supplied function. Explain why a bare except can hide an unrelated failure. [6 marks]

# zero is not considered a valid integer
# second rejected is not defined
# thirdly rejected is not incremented
# a bare except can hide failure because it does not consider other edge cases, it is very narrow. For instance it does not take -3 and 0 as numbers

# Q4 Part B
# Rewrite the function to meet every rule. Catch only the expected conversion exception. [11 marks]

# def summarise_amounts(raw_values):
#     total = 0
# rejected = 0
#     for raw in raw_values:
#         try:
#             total += int(raw)
#         except:
#             pass
#     return {"total": total, "rejected": 0}
    
# Q4 Part C
# Write four executable assertions covering the required mixed example, empty input, all rejected input, and a valid zero. State why checking only total could miss a bug. [8 marks]

#solution