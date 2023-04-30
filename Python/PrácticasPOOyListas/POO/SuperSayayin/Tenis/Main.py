from ClasesTenis import * 


if __name__ == '__main__':
    # Crear dos jugadores
    player1 = Player("Roger Federer")
    player2 = Player("Rafael Nadal")

    # Crear un partido
    match = Match(player1, player2)

    # Agregar puntos al jugador 1
    player1.add_score(15)
    player1.add_score(15)
    player1.add_score(15)
    player1.add_score(15)
    player1.add_score(10) # Deuce
    player1.add_score(10) # Advantage
    player1.add_score(10) # Game

    # Agregar puntos al jugador 2
    player2.add_score(15)
    player2.add_score(15)
    player2.add_score(30)
    player2.add_score(30)
    player2.add_score(30)
    player2.add_score(30) # Deuce
    player2.add_score(10) # Advantage
    player2.add_score(10) # Game

    # Imprimir el ganador del partido y la puntuación final
    winner = match.get_winner()
    if winner:
        print(f"Ganador: {winner.name}")
    else:
        print("Empate")
    print(f"Puntuación final: {match.get_score()}")
