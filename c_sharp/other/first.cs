Console.WriteLine("Heloo world!");
var nimi = Console.ReadLine();//ReadKey
if (nimi.ToUpper()=="Juku")
{
    Console.WriteLine("Go to cinema");
    int vanus = Convert.ToInt32(Console.ReadLine());
    if (vanus < 0 || vanus > 120)
    {
        Console.WriteLine("You can't be {0} years old", vanus);
    }
    elseif(vanus < 6)
    {
        Console.WriteLine("For you ticket is FREE!");
    }
    elseif (vanus >= 6 && vanus =< 14)
        Console.WriteLine("For you ticket is child ticket!");
    elseif (vanus >= 15 && vanus =< 65)
        Console.WriteLine("For you ticket is adult ticke!");
    elseif (vanus >= 65)
        Console.WriteLine("For you ticket is with discount!");
}
else
{
    Console.WriteLine("I am not at home");
}
Console.Clear()
Console.BackgroundColor = ConsoleColor.Magenta;
Console.ForegroundColor = ConsoleColor.Yellow;
Random rnd = new Random();
int hinne = rnd.Next(1, 5);
Console.WriteLine("Today I got {0}", hinne);
string reaction = "";
switch (hinne)
{
    case 1: reaction = "Worst! Study more!";break;
    case 2: reaction = "Study more!";break;
    case 3: reaction = "Bad, study more!";break;
    case 4: reaction = "Not bad, but more!";break;
    case 5: reaction = "Good show!";break;
    default:
        reaction = "Error!";
        break;
}
for (int i = 0; i < hinne; i++)
{
    Console.WriteLine(reaction);
}
int hinne_test = hinne;
while (hinne>0)
{
    hinne--;//hinne=hinne-1
}
do
{
    Console.WriteLine(reaction);
    hinne_test--;
} while (hinne_test!=0);


//console.WriteLine("Hi, " + nimi);
//Console.WriteLine("Number 1: ");
//int arv1=int.Parse(Console.ReadLine());
//Console.WriteLine("Number 2:");
//int arv2 = int.Parse(Console.ReadLine());
//char tehe=char.ToUpper(Console.ReadLine());
//Console.WriteLine("Doing: ");
//char tehe=Convert.ToChar(Console.ReadLine()[0]);
//double vastus = 0;
//if(tehe == '+')
//{
  //  Console.WriteLine("Calculate {0} ja {1} and {2}", arv1, arv2, arv1 + arv2);
//}
//elseif (tehe == '-')
//{
 //   Console.WriteLine("Calculate {0} ja {1} and {2}", arv1, arv2, arv1 - arv2);
//}
//elseif(tehe == '/')
//{
  //  double vastus = arv1 / arv2;
    
//}
//else
//{
  //  Console.WriteLine("{0} - unknown doing", tehe);
//}
//Console.WriteLine("Calculate {0} ja {1} and {2}", arv1, arv2, vastus);