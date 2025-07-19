class Recipe:
    def __init__(self, title, ingredients, steps):
        self.title = title
        self.ingredients = ingredients
        self.steps = steps

    def __str__(self):
        return f"Recipe: {self.title}\n" \
               f"Ingredients: {','.join(self.ingredients)}\n" \
               f"Steps: \n"+"\n".join(f"- {step}" for step in self.steps)

    def to_dict(self):
        return {
            "title": self.title,
            "ingredients": self.ingredients,
            "steps": self.steps
            }

    @classmethod
    def from_dict(cls, data):
        return cls(data["title"], data["ingredients"], data["steps"])
