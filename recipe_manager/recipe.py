class Recipe:
    def __init__(self, title, ingredients, steps):
        self.title = title
        self.ingredients = ingredients
        self.steps = steps

    def __str__(self):
        return f"Recipe: {self.title}\n" \
               f"Ingredients: {','.join(self.ingredients)}\n" \
               f"Steps: \n"+"\n".join(f"- {step}" for step in self.steps)

if __name__ == "__main__":
    r= Recipe(
        title="Pasta",
        ingredients=["pasta","tomato sauce","cheese"],
        steps=["Boil Pasta","Add sauce", "Sprinkle cheese"]
        )
    print(r)
