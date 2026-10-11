"""Sistema de recomendaciones de películas por género y año."""

from __future__ import annotations

import argparse
from dataclasses import dataclass


@dataclass(frozen=True)
class Movie:
    """Representa una película disponible para recomendar."""

    title: str
    year: int
    rating: float
    genres: tuple[str, ...]


MOVIES: tuple[Movie, ...] = (
    Movie("Interestelar", 2014, 8.7, ("Ciencia ficción", "Aventura", "Drama")),
    Movie("El viaje de Chihiro", 2001, 8.6, ("Animación", "Aventura", "Fantasía")),
    Movie("Parásitos", 2019, 8.5, ("Suspenso", "Drama", "Comedia")),
    Movie("La La Land", 2016, 8.0, ("Romance", "Drama", "Comedia")),
    Movie("El origen", 2010, 8.8, ("Ciencia ficción", "Acción", "Suspenso")),
    Movie("Coco", 2017, 8.4, ("Animación", "Aventura", "Fantasía")),
    Movie("Mad Max: Furia en el camino", 2015, 8.1, ("Acción", "Aventura", "Ciencia ficción")),
    Movie("Amélie", 2001, 8.3, ("Romance", "Comedia")),
    Movie("El gran hotel Budapest", 2014, 8.1, ("Comedia", "Aventura", "Drama")),
    Movie(
        "Spider-Man: Un nuevo universo",
        2018,
        8.4,
        ("Animación", "Acción", "Aventura"),
    ),
    Movie("El silencio de los inocentes", 1991, 8.6, ("Suspenso", "Drama")),
    Movie("Orgullo y prejuicio", 2005, 7.8, ("Romance", "Drama")),
)

GENRES = frozenset(genre for movie in MOVIES for genre in movie.genres)


def recommend_movies(
    genre: str | None = None,
    year_from: int | None = None,
    year_to: int | None = None,
    limit: int = 5,
) -> list[Movie]:
    """Devuelve las películas mejor calificadas que coinciden con los filtros.

    Los años de inicio y fin son inclusivos. Si no se especifica un género o
    límite de año, ese filtro no se aplica.
    """
    if genre is not None and genre not in GENRES:
        raise ValueError(f"Género no disponible: {genre}")
    if year_from is not None and (not isinstance(year_from, int) or isinstance(year_from, bool)):
        raise ValueError("El año inicial debe ser un número entero.")
    if year_to is not None and (not isinstance(year_to, int) or isinstance(year_to, bool)):
        raise ValueError("El año final debe ser un número entero.")
    if year_from is not None and year_to is not None and year_from > year_to:
        raise ValueError("El año inicial no puede ser posterior al año final.")
    if not isinstance(limit, int) or isinstance(limit, bool) or limit < 1:
        raise ValueError("El límite debe ser un número entero mayor que cero.")

    matching_movies = (
        movie
        for movie in MOVIES
        if (genre is None or genre in movie.genres)
        and (year_from is None or movie.year >= year_from)
        and (year_to is None or movie.year <= year_to)
    )
    return sorted(matching_movies, key=lambda movie: (-movie.rating, movie.title))[:limit]


def main() -> None:
    """Lee filtros de la terminal y muestra las recomendaciones."""
    parser = argparse.ArgumentParser(
        description="Recomienda películas por género y rango de años."
    )
    parser.add_argument("--genero", choices=sorted(GENRES), help="Género de la película")
    parser.add_argument("--desde", type=int, help="Año inicial, inclusive")
    parser.add_argument("--hasta", type=int, help="Año final, inclusive")
    parser.add_argument("--limite", type=int, default=5, help="Cantidad máxima (por defecto: 5)")
    args = parser.parse_args()

    try:
        recommendations = recommend_movies(
            genre=args.genero,
            year_from=args.desde,
            year_to=args.hasta,
            limit=args.limite,
        )
    except ValueError as error:
        parser.error(str(error))

    if not recommendations:
        print("No se encontraron películas con esos filtros.")
        return

    print("Recomendaciones:")
    for movie in recommendations:
        genres = ", ".join(movie.genres)
        print(f"- {movie.title} ({movie.year}) | ★ {movie.rating:.1f} | {genres}")


if __name__ == "__main__":
    main()
