# test helper
def contains_all(required_members, all_members):
    for item in required_members:
        if item not in all_members:
            return False
    return True
