﻿using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Snake
{
    class Point
    {
        public int x;
        public int y;
        public char sym;
        public ConsoleColor color;
        public Point()
        {
        }

        public Point(int x, int y, char sym, ConsoleColor color)
        {
            this.x = x;
            this.y = y;
            this.sym = sym;
            this.color = color;
        }

        public Point(Point p, ConsoleColor color_)
        {
            x = p.x;
            y = p.y;
            sym = p.sym;
            color = color_;
        }

        public void Move(int offset, Direction direction)
        {
            if (direction == Direction.RIGHT)
            {
                x = x + offset;
            }
            else if (direction == Direction.LEFT)
            {
                x = x - offset;
            }
            else if (direction == Direction.UP)
            {
                y = y - offset;
            }
            else if(direction == Direction.DOWN)
            {
                y = y + offset;
            }
                
        }

        public bool IsHit(Point p)
        {
            return p.x == this.x && p.y == this.y;
        }

        public void Draw()
        {
            Console.SetCursorPosition(x, y);
            Console.Write(sym);
        }

        public void Clear()
        {
            sym = ' ';
            Draw();
        }
         
        public override string ToString()
        {
            return x + ", " + y + ", " + sym;
        }
    }
}