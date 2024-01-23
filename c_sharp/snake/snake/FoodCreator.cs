using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Snake
{
    class FoodCreator
    {
        int mapWidht;
        int mapHeight;
        char sym;
        ConsoleColor color;

        Random random = new Random();

        public FoodCreator(int mapWidht, int mapHeight, char sym)
        {
            this.mapWidht = mapWidht;
            this.mapHeight = mapHeight;
            this.sym = sym;
        }

        public Point CreateFood()
        {
            int x = random.Next(2, mapWidht);
            int y = random.Next(2, mapHeight);
            return new Point(x, y, sym, color);
        }
    }
}

