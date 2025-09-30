class Movie:
    def __init__(self, title, year, director, description, poster_path):
        self.title = title
        self.year = year
        self.director = director
        self.description = description
        self.poster_path = poster_path

    def show(self):
        print(f"🎬 {self.title} ({self.year})")
        print(f"Directed by: {self.director}")
        print(f"Poster: {self.poster_path}")
        print("\n" + self.description)


the_last_tomate = Movie(
    title="The Last Tomate",
    year=2024,
    director="HW",
    description=(
        "In a world where all vegetables have vanished, one lone tomato survives. "
        "This humble red fruit—mistaken for a vegetable—holds the secret to restoring Earth's soil. "
        "With the help of a curious squirrel and a retired gardener, it embarks on an epic journey "
        "across abandoned farms and concrete jungles. Along the way, it learns about resilience, "
        "identity, and the true meaning of 'ripe for change.' A heartwarming tale of hope, "
        "botany, and one very brave tomato. Rated G for 'Garden-friendly.'"
    ),
    poster_path="tomato.jpg"
)

rocket_revenge = Movie(
    title="Rocket Raccoon’s Revenge",
    year=2025,
    director="G. Groot",
    description=(
        "After being fired from the Galactic Delivery Service for 'excessive snacking,' "
        "a genius raccoon named Rocket builds his own rocket ship out of pizza boxes and duct tape. "
        "He teams up with a talking toaster and a depressed alien cat to steal back his job—"
        "and accidentally becomes the galaxy’s most wanted hero. "
        "Rated PG for 'space snacks' and 'unauthorized flight.'"
    ),
    poster_path="rocket_raccoon.jpg"
)

soap_opera = Movie(
    title="The Soap Opera",
    year=2024,
    director="Lather M. Suds",
    description=(
        "In a world where every bubble from your morning shower contains a memory, "
        "a lonely barista discovers she can see people’s past lives through soap bubbles. "
        "When she accidentally pops a bubble containing the secret of a missing king, "
        "she must choose: keep quiet… or blow the lid off history. "
        "Rated PG-13 for 'emotional suds' and 'bubble trouble.'"
    ),
    poster_path="soap_bubble.jpg"
)

robo_pet = Movie(
    title="Robo-Pet: The Dog Who Could Code",
    year=2024,
    director="C. Byte",
    description=(
        "When a tech-savvy kid builds a robot dog that can write Python code, "
        "they enter a national robotics competition… only to discover the dog is secretly fixing bugs in the city’s power grid. "
        "Together, they save the town from a digital meltdown — and prove that love isn’t just for humans. "
        "Rated G for 'barking code' and 'tail-wagging algorithms.'"
    ),
    poster_path="robo_dog.jpg"
)

moon_vacation = Movie(
    title="The Moon’s Day Off",
    year=2025,
    director="Orbita Luna",
    description=(
        "Tired of always being up at night, the Moon decides to take a day off — "
        "and chaos ensues. Tides go wild, werewolves nap all day, and astronomers panic. "
        "A brave astronaut and a sleepy sunflower team up to convince the Moon to return… "
        "but only if it gets a new vacation policy. "
        "Rated G for 'lunar lounging' and 'celestial shenanigans.'"
    ),
    poster_path="moon_vacation.jpg"
)

puzzle_planet = Movie(
    title="Puzzle Planet",
    year=2024,
    director="Jigsaw J. Piece",
    description=(
        "On a distant planet, every mountain is a jigsaw puzzle, every river is a crossword, "
        "and the trees grow Sudoku leaves. When a curious child falls through a portal, "
        "they must solve the planet’s greatest mystery before sunset — or get stuck as part of the landscape. "
        "Rated PG for 'brain-bending fun' and 'piece-by-piece survival.'"
    ),
    poster_path="puzzle_planet.jpg"
)

if __name__ == "__main__":
    the_last_tomate.show()
    rocket_revenge.show()
    soap_opera.show()
    robo_pet.show()
    moon_vacation.show()
    puzzle_planet.show()