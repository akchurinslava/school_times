using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;  
using System.Threading.Tasks;


namespace Snake
{
    class Program
    {
        static void Main(string[] args)
        {
            Start start = new Start();
            start.choice();
           
            Walls walls = new Walls(80, 25);
            walls.Draw();

            Point p = new Point(4, 5, '*', ConsoleColor.Blue);
            Snake snake = new Snake(p, 4, Direction.RIGHT);
            snake.Draw();

            FoodCreator foodCreator = new FoodCreator(60, 25, '$');
            Point food = foodCreator.CreateFood();
            food.Draw();

            Score score = new Score(0);
            score.ScoreWrite();

            while (true)
            {
                if (walls.IsHit(snake) || snake.IsHitTail())
                {
                    Console.Clear();
                    Console.SetCursorPosition(0, 5);
                    Console.WriteLine("GAME");
                    Console.WriteLine("OVER");
                    Console.Write("Enter your name:");
                    string name = Console.ReadLine();
                    if (name.Length < 3)
                    {
                        Console.WriteLine("Name must be greater then 3 words");
                        continue;
                    }
                    else
                    {
                        FWriter writer = new FWriter();
                        writer.WriteNameToFile(name, score.ScoreUp());
                        writer.ShowResults();
                        Thread.Sleep(6000);
                        break;

                    }
                }
                if (snake.Eat(food))
                {
                    score.ScoreUp();
                    score.ScoreWrite();
                    food = foodCreator.CreateFood();
                    food.Draw();
                }
                else
                {
                    snake.Move();
                }

                Thread.Sleep(300);
                if (Console.KeyAvailable)
                {
                    ConsoleKeyInfo key = Console.ReadKey();
                    snake.HandleKey(key.Key);
                }
            }
        }
    }
}
         
                
