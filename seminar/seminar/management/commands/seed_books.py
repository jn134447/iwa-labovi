from django.core.management.base import BaseCommand
from seminar.models import Genre, Author, Book

class Command(BaseCommand):
    help = "Seed 50+ books"

    def handle(self, *args, **kwargs):
        # Create genres
        horror = Genre.objects.get_or_create(name="Horror")[0]
        scifi = Genre.objects.get_or_create(name="Science Fiction")[0]
        drama = Genre.objects.get_or_create(name="Drama")[0]
        fantasy = Genre.objects.get_or_create(name="Fantasy")[0]
        mystery = Genre.objects.get_or_create(name="Mystery")[0]
        romance = Genre.objects.get_or_create(name="Romance")[0]

        # Create authors
        authors = {
            "stephen_king": Author.objects.get_or_create(first_name="Stephen", last_name="King")[0],
            "jk_rowling": Author.objects.get_or_create(first_name="J.K.", last_name="Rowling")[0],
            "tolkien": Author.objects.get_or_create(first_name="J.R.R.", last_name="Tolkien")[0],
            "orwell": Author.objects.get_or_create(first_name="George", last_name="Orwell")[0],
            "austen": Author.objects.get_or_create(first_name="Jane", last_name="Austen")[0],
            "dostoevsky": Author.objects.get_or_create(first_name="Fyodor", last_name="Dostoevsky")[0],
            "hemingway": Author.objects.get_or_create(first_name="Ernest", last_name="Hemingway")[0],
            "christie": Author.objects.get_or_create(first_name="Agatha", last_name="Christie")[0],
            "tolkien": Author.objects.get_or_create(first_name="J.R.R.", last_name="Tolkien")[0],
            "martin": Author.objects.get_or_create(first_name="George R.R.", last_name="Martin")[0],
        }

        books = [
            {"title": "The Shining", "description": "A family heads to an isolated hotel for the winter.", "genre": horror, "authors": ["stephen_king"]},
            {"title": "It", "description": "A group of children face an ancient evil in Derry, Maine.", "genre": horror, "authors": ["stephen_king"]},
            {"title": "Carrie", "description": "A bullied girl discovers telekinetic powers.", "genre": horror, "authors": ["stephen_king"]},
            {"title": "Pet Sematary", "description": "A burial ground brings the dead back... wrong.", "genre": horror, "authors": ["stephen_king"]},
            {"title": "Misery", "description": "An author is held captive by an obsessed fan.", "genre": horror, "authors": ["stephen_king"]},
            {"title": "Harry Potter and the Philosopher's Stone", "description": "A boy discovers he's a wizard.", "genre": fantasy, "authors": ["jk_rowling"]},
            {"title": "Harry Potter and the Chamber of Secrets", "description": "A mysterious chamber opens at Hogwarts.", "genre": fantasy, "authors": ["jk_rowling"]},
            {"title": "Harry Potter and the Prisoner of Azkaban", "description": "A notorious prisoner escapes.", "genre": fantasy, "authors": ["jk_rowling"]},
            {"title": "Harry Potter and the Goblet of Fire", "description": "A dangerous tournament begins.", "genre": fantasy, "authors": ["jk_rowling"]},
            {"title": "Harry Potter and the Order of the Phoenix", "description": "The wizarding world denies Voldemort's return.", "genre": fantasy, "authors": ["jk_rowling"]},
            {"title": "The Hobbit", "description": "A hobbit goes on an unexpected journey.", "genre": fantasy, "authors": ["tolkien"]},
            {"title": "The Fellowship of the Ring", "description": "A fellowship is formed to destroy a ring.", "genre": fantasy, "authors": ["tolkien"]},
            {"title": "The Two Towers", "description": "The fellowship is broken.", "genre": fantasy, "authors": ["tolkien"]},
            {"title": "The Return of the King", "description": "The final battle for Middle-earth.", "genre": fantasy, "authors": ["tolkien"]},
            {"title": "1984", "description": "A dystopian future under constant surveillance.", "genre": scifi, "authors": ["orwell"]},
            {"title": "Animal Farm", "description": "Farm animals revolt against their human farmer.", "genre": drama, "authors": ["orwell"]},
            {"title": "Pride and Prejudice", "description": "A woman navigates love and social standing.", "genre": romance, "authors": ["austen"]},
            {"title": "Sense and Sensibility", "description": "Two sisters navigate love and loss.", "genre": romance, "authors": ["austen"]},
            {"title": "Emma", "description": "A young woman meddles in others' love lives.", "genre": romance, "authors": ["austen"]},
            {"title": "Crime and Punishment", "description": "A man commits murder and faces guilt.", "genre": drama, "authors": ["dostoevsky"]},
            {"title": "The Brothers Karamazov", "description": "A family drama of faith and doubt.", "genre": drama, "authors": ["dostoevsky"]},
            {"title": "The Idiot", "description": "A kind prince returns to Russian society.", "genre": drama, "authors": ["dostoevsky"]},
            {"title": "The Old Man and the Sea", "description": "A fisherman's epic struggle with a marlin.", "genre": drama, "authors": ["hemingway"]},
            {"title": "A Farewell to Arms", "description": "A love story set in World War I.", "genre": drama, "authors": ["hemingway"]},
            {"title": "For Whom the Bell Tolls", "description": "A man fights in the Spanish Civil War.", "genre": drama, "authors": ["hemingway"]},
            {"title": "Murder on the Orient Express", "description": "A detective solves a murder on a train.", "genre": mystery, "authors": ["christie"]},
            {"title": "And Then There Were None", "description": "Ten strangers on an island are killed one by one.", "genre": mystery, "authors": ["christie"]},
            {"title": "The Murder of Roger Ackroyd", "description": "A detective investigates a village murder.", "genre": mystery, "authors": ["christie"]},
            {"title": "Death on the Nile", "description": "A murder on a Nile cruise ship.", "genre": mystery, "authors": ["christie"]},
            {"title": "A Game of Thrones", "description": "Noble families fight for the Iron Throne.", "genre": fantasy, "authors": ["martin"]},
            {"title": "A Clash of Kings", "description": "War consumes the Seven Kingdoms.", "genre": fantasy, "authors": ["martin"]},
            {"title": "A Storm of Swords", "description": "Chaos reigns across the land.", "genre": fantasy, "authors": ["martin"]},
            {"title": "A Feast for Crows", "description": "The aftermath of war unfolds.", "genre": fantasy, "authors": ["martin"]},
            {"title": "A Dance with Dragons", "description": "Dragons stir in the east.", "genre": fantasy, "authors": ["martin"]},
            {"title": "The Stand", "description": "A plague wipes out most of humanity.", "genre": horror, "authors": ["stephen_king"]},
            {"title": "Salem's Lot", "description": "A vampire terrorizes a small town.", "genre": horror, "authors": ["stephen_king"]},
            {"title": "Dune", "description": "A desert planet holds the galaxy's most valuable resource.", "genre": scifi, "authors": ["orwell"]},
            {"title": "Foundation", "description": "A mathematician predicts the fall of the galactic empire.", "genre": scifi, "authors": ["orwell"]},
            {"title": "Brave New World", "description": "A futuristic society of pleasure and control.", "genre": scifi, "authors": ["orwell"]},
            {"title": "The Catcher in the Rye", "description": "A teenager wanders New York City.", "genre": drama, "authors": ["hemingway"]},
            {"title": "The Great Gatsby", "description": "A mysterious millionaire chases a lost love.", "genre": drama, "authors": ["hemingway"]},
            {"title": "Moby Dick", "description": "A captain obsessively hunts a white whale.", "genre": drama, "authors": ["hemingway"]},
            {"title": "The Picture of Dorian Gray", "description": "A man's portrait ages instead of him.", "genre": horror, "authors": ["stephen_king"]},
            {"title": "Dracula", "description": "A vampire comes to England.", "genre": horror, "authors": ["stephen_king"]},
            {"title": "Frankenstein", "description": "A scientist creates life and pays the price.", "genre": horror, "authors": ["stephen_king"]},
            {"title": "The Hobbit 2", "description": "Just kidding, not a real book.", "genre": fantasy, "authors": ["tolkien"]},
            {"title": "Sherlock Holmes: A Study in Scarlet", "description": "Holmes and Watson's first case.", "genre": mystery, "authors": ["christie"]},
            {"title": "The Hound of the Baskervilles", "description": "A supernatural hound haunts a family.", "genre": mystery, "authors": ["christie"]},
            {"title": "Harry Potter and the Half-Blood Prince", "description": "Secrets of Voldemort's past revealed.", "genre": fantasy, "authors": ["jk_rowling"]},
            {"title": "Harry Potter and the Deathly Hallows", "description": "The final battle against Voldemort.", "genre": fantasy, "authors": ["jk_rowling"]},
            {"title": "The Sun Also Rises", "description": "Expatriates in 1920s Europe.", "genre": drama, "authors": ["hemingway"]},
            {"title": "Persuasion", "description": "A woman gets a second chance at love.", "genre": romance, "authors": ["austen"]},
            {"title": "Northanger Abbey", "description": "A gothic parody about a young woman.", "genre": romance, "authors": ["austen"]},
            {"title": "Notes from Underground", "description": "A bitter man's thoughts on society.", "genre": drama, "authors": ["dostoevsky"]},
            {"title": "The Gambler", "description": "A tutor gets addicted to roulette.", "genre": drama, "authors": ["dostoevsky"]},
        ]

        for book_data in books:
            book = Book.objects.create(
                title=book_data["title"],
                description=book_data["description"],
                genre=book_data["genre"],
            )
            for author_key in book_data["authors"]:
                book.authors.add(authors[author_key])

        self.stdout.write(self.style.SUCCESS(f"Seeded {len(books)} books!"))