# ✅ Example 3: __len__ and __repr__
class Team:
    def __init__(self, members):
        self.members = members

    def __len__(self):
        return len(self.members)

    def __repr__(self):
        return f"Team({self.members})"

t = Team(["Alice", "Bob", "Charlie"])
print(len(t))   # 3
print(t)        # Team(['Alice', 'Bob', 'Charlie'])