using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Snake
{
    public class Start
    {
        public ConsoleKeyInfo key;
        public Start()
        {
        }
        int valik = 0;
        public int choice()
        {

            Console.SetCursorPosition(0, 5);
            Console.WriteLine("------------------");
            Console.WriteLine(" Start game - S\n Stop game - Q");
            Console.WriteLine("------------------");
            Console.WriteLine("(\\__/)");
            Console.WriteLine("(='.'=)");
            Console.WriteLine("(\")_(\")");
            key = Console.ReadKey(true);

            if (key.Key == ConsoleKey.S)
            {
                Console.Clear();
                Console.SetCursorPosition(5, 5);
            }
            else if (key.Key == ConsoleKey.Q)
            {
                Console.Clear();
                Console.SetCursorPosition(0, 5);
                Console.WriteLine("GAME");
                Console.WriteLine("OVER");
                Thread.Sleep(1000);
                Environment.Exit(1);
            }
            return valik;
        }
    }
}

