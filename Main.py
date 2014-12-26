from Game import Game
import Graphics
import Turn
import threading

def main():
   game = Game()
   #Turn.run(game)
   thread = threading.Thread(target=Turn.run, args=(game,))
   thread.start()
   
   Graphics.run()


if __name__ == "__main__":
   main()
