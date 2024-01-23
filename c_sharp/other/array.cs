Random rnd = new Random();
int mass = rnd.Next(1,10);
string[]Named=new string[mass];
string name="";

for (int i = 0; i < mass; i++)
{
    Console.WriteLine("Enter {0} the name: ", i+1);
    Named[i] = Console.ReadLine();

}


for (int i = 0; i < Named.Length; i++)
{
    Console.WriteLine("Hi {0}", Named[i]);
}

int time = 0;
int pc = rnd.Next(1, 100);
int human;
do
{
    human = Convert.ToInt32(Console.ReadLine());
    time++;
} while (human!=pc && time!=5);


for (int i = 0; i < 11; i++)
{
    for (int j = 0; i < 11; j++)
    {
        Console.Write("{0,4}", i * j);
    }
    Console.WriteLine();
}


int[]Numbers = new int[5];
for (int i = 0; i < 5; i++)
{
    Numbers[i] = Convert.ToInt32(Console.ReadLine());
}
int summ = 0, multiple = 1;
double average
foreach (int item in Numbers)
{
    Console.WriteLine("{0,5}", item);
    summ = summ + item;
    multiple = multiple * item;
}

average = summ / Numbers.Length;
Console.WriteLine("Summ={0}, \nMultiple={1}, \nAverage={2}", summ, multiple, average);

















