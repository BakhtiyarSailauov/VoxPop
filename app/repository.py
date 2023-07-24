class CommentsRepository:
    def __init__(self):
        self.comments = [
            {"id": 1, "text": "Мен ойлаймын, бұл өте керемет!", "category": "positive"},
            {"id": 2, "text": "Мен ойлаймын, бұл өте керемет!", "category": "positive"},
            {"id": 3, "text": "Мен ойлаймын, бұл өте керемет!", "category": "positive"},
            {"id": 4, "text": "Мен ойлаймын, бұл өте керемет!", "category": "positive"},
            {"id": 5, "text": "Мен ойлаймын, бұл өте керемет!", "category": "positive"},
            {"id": 6, "text": "Мен ойлаймын, бұл өте керемет!", "category": "positive"},
            {"id": 7, "text": "Мен ойлаймын, бұл өте керемет!", "category": "positive"},
            {"id": 8, "text": "Мен ойлаймын, бұл өте керемет!", "category": "positive"},
            {"id": 9, "text": "Мен ойлаймын, бұл өте керемет!", "category": "positive"},
            {"id": 10, "text": "Мен ойлаймын, бұл өте нашар!", "category": "negative"},
            {"id": 11, "text": "Мен ойлаймын, бұл өте нашар!", "category": "negative"},
            {"id": 12, "text": "Мен ойлаймын, бұл өте нашар!", "category": "negative"},
            {"id": 13, "text": "Мен ойлаймын, бұл өте нашар!", "category": "negative"},
            {"id": 14, "text": "Мен ойлаймын, бұл өте нашар!", "category": "negative"},
            {"id": 15, "text": "Мен ойлаймын, бұл өте нашар!", "category": "negative"},

        ]

    def get_all(self):
        return self.comments

    def get_one(self, user_id):
        for user in self.comments:
            if user["id"] == user_id:
                return user
        return None

    def save(self, comment):
        if "id" not in comment or not comment["id"]:
            comment["id"] = self.get_next_id()
        self.comments.append(comment)
        return comment

    def get_next_id(self):
        return len(self.comments) + 1
