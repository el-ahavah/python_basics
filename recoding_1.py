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

def summarise_amounts(raw_values):
    total = 0
    rejected = 0

    for raw in raw_values:
        try:
            amount = int(raw)

            if amount >= 0:
                total += amount
            else:
                rejected += 1

        except ValueError:
            rejected += 1

    return {"total": total, "rejected": rejected}

assert summarise_amounts(["10", " 5 ", "bad", "-3", "0", ""]) == {
    "total": 15,
    "rejected": 3
}

assert summarise_amounts([]) == {
    "total": 0,
    "rejected": 0
}

assert summarise_amounts(["bad", "-3", ""]) == {
    "total": 0,
    "rejected": 3
}

assert summarise_amounts(["0"]) == {
    "total": 0,
    "rejected": 0
}

#---------------------------------------------------------------------------

# Question 5 Make stock reservation reliable

# stock maps item names to available quantities. order is a list of (item, quantity) pairs. Stock values are non-negative integers; order quantities are integers, not booleans. Keys are strings. These shapes and types are guaranteed.

# def reserve_stock(stock, order):
#     remaining = stock.copy()
#     for item, quantity in order:
#         if quantity > stock[item]:
#             raise ValueError("Insufficient stock")
#         remaining[item] = stock[item] - quantity
#     return remaining
   
# Required behaviour:
# Return a new dictionary containing every stock key with its remaining quantity. Never modify stock or order, including when a request fails.

# An item may occur more than once in order. Its combined requested quantity must be reserved. Never allow a negative remaining quantity.

# Raise ValueError for an unknown item, a quantity of zero or less, or insufficient stock. Error message wording is your choice. An empty order returns an equal but separate dictionary.

# You may use try/except with an assertion that fails if ValueError is not raised. Tests must call the function and check a result or failure, not just print it.

# Q5 Part A
# With stock = {"pen": 5}, trace order = [("pen", 3), ("pen", 3)]. Explain why the supplied code incorrectly succeeds, and identify the other validation gaps. [6 marks]

# Q5 Part B
# Repair the function to meet all requirements. Use only in-memory Python; no database or concurrency implementation is needed. [14 marks]

# Q5 Part C
# Write four tests: successful repeated items, repeated items exceeding stock, an unknown item, and zero quantity. In the overselling test, make at least one earlier line valid, then assert the original stock is unchanged after the exception. Explain why editing a local copy protects the caller when a later line fails. [10 marks]

# solution

""" PART A: The supplied function incorrectly succeeds because it checks every requested quantity against the original stock[item]. With stock = {"pen": 5} and order = [("pen", 3), ("pen", 3)], both requests are checked against 5 instead of checking the remaining quantity after the first reservation. The first request leaves 2 pens, so the second request should fail.

Other validation gaps are that it does not properly handle unknown items as ValueError, allows zero quantities, allows negative quantities, and therefore does not enforce all the required validation rules. """

""" PART B: """
def reserve_stock(stock, order):
    remaining = stock.copy()

    for item, quantity in order:
        if item not in stock:
            raise ValueError("Unknown item")

        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if quantity > remaining[item]:
            raise ValueError("Insufficient stock")

        remaining[item] -= quantity

    return remaining

""" PART C: """

# Successful repeated items:

stock = {"pen": 5, "book": 10}
order = [("pen", 2), ("pen", 1)]

result = reserve_stock(stock, order)

assert result == {"pen": 2, "book": 10}
assert stock == {"pen": 5, "book": 10}

# Repeated items exceeding stock:

stock = {"pen": 5}
order = [("pen", 3), ("pen", 3)]

try:
    reserve_stock(stock, order)
    assert False, "Expected ValueError"
except ValueError:
    pass

assert stock == {"pen": 5}

# unknown item:

stock = {"pen": 5}
order = [("book", 1)]

try:
    reserve_stock(stock, order)
    assert False, "Expected ValueError"
except ValueError:
    pass

# Zero quantity:

stock = {"pen": 5}
order = [("pen", 0)]

try:
    reserve_stock(stock, order)
    assert False, "Expected ValueError"
except ValueError:
    pass