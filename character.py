class Character:
    def __init__(self, name, role, health=100):
        self.name = name
        self.role = role
        self.health = health

    def take_damage(self, amount):
        self.health -= amount
        if self.health < 0:
            self.health = 0

    def heal(self, amount):
        self.health += amount
        if self.health > 100:
            self.health = 100

    def is_alive(self):
        return self.health > 0

    def __str__(self):
        return f"{self.name} ({self.role}) - Health: {self.health}"

# Example usage
if __name__ == "__main__":
    hero = Character("Arjun", "Warrior")
    villain = Character("Duryodhan", "Enemy", 120)

    print(hero)
    print(villain)

    villain.take_damage(30)
    print(f"After attack: {villain}")

    hero.heal(10)
    print(f"After healing: {hero}")